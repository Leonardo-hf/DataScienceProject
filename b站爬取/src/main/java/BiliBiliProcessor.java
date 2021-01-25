import org.apache.log4j.Logger;
import org.openqa.selenium.chrome.ChromeOptions;
import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.Site;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.downloader.selenium.SeleniumDownloader;
import us.codecraft.webmagic.processor.PageProcessor;
import us.codecraft.webmagic.scheduler.BloomFilterDuplicateRemover;
import us.codecraft.webmagic.scheduler.QueueScheduler;

import java.io.PrintStream;
import java.util.ArrayList;

public class BiliBiliProcessor implements PageProcessor {
   static Ans thisans;
   // private static int COUNT = 1;
    static PrintStream ps;
    private static Logger logger = Logger.getLogger(BiliBiliProcessor.class.getName());

    private Site site = Site.me().setSleepTime(6000);

    public void process(Page page) {
        //此方法用来处理页面
        ArrayList<String> list=new ArrayList<String>();
        String temp=page.toString();
        char[] t=temp.toCharArray();
        for (int i=0;i<t.length;i++){
            if ((t[i]=='m')&&(t[i+1]=='e')&&(t[i+2]=='s')&&(t[i+3]=='s')&&(t[i+4]=='a')&&(t[i+5]=='g')&&(t[i+6]=='e')){
                String record="";
                i=i+10;
                while (t[i]!='\"'){
                    record+=t[i];
                    i++;
                }
                if (record!=""&&!record.equals("0")) {
                    list.add(record);
                }
            }
        }
        int size=list.size()/2;
        for (int i=1;i<=size;i++){
            list.remove(list.size()-1);
        }
        if (!page.getUrl().toString().contains("pn=1")){
            for (int i=1;i<=40;i++){
                list.remove(list.size()-1);
                if (list.isEmpty()) break;
            }
        }

        while (!list.isEmpty()){
                thisans.ans.add(list.get(0));
                list.remove(0);
        }
    }


    public Site getSite() {
        return site;
    }

    public static void main(String[] args) throws Exception{
        PrintStream beforePrintStream = System.out;
        System.setProperty("selenuim_config", "src/main/java/config/SelenumConfig.ini");
        //设置爬虫配置
        ChromeOptions chromeOptions = new ChromeOptions();
        chromeOptions.addArguments("--headless");
        thisans=new Ans("3.12","钟南山：疫情有望在六月结束 前提是各国重视起来");
        for (int i = 1; i <= 113; i++) {
            Spider.create(new BiliBiliProcessor())
                    .addUrl("http://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn="+i+"&type=1&oid=69054573&sort=0")
                    .setDownloader(new SeleniumDownloader("src/main/java/chromedriver.exe"))
                    .setScheduler(new QueueScheduler().setDuplicateRemover(new BloomFilterDuplicateRemover(10000)))
                    .thread(1) //设置线程数
                    //.addPipeline(mysqlPipeline) //设置持久化
                    .run();

        }
        thisans.print();
        System.setOut(beforePrintStream);

    }
}
