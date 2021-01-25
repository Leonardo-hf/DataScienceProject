import java.io.PrintStream;
import java.util.ArrayList;

public class Ans {
    public  ArrayList<String> ans=new ArrayList<String>();
    public Ans(String add1,String add2){
        this.time=add1;
        this.title=add2;
    }
    String time;
    String title;
    int count=0;
    public void print() throws Exception{
        //此方法用来定向输出
        while (!ans.isEmpty()){
            String temp=ans.get(0);
            ans.remove(0);
            if (temp.startsWith("回复")) continue;
            count++;
            PrintStream ps=new PrintStream("E:\\static\\作业\\"+time+"\\"+title+"\\"+count+".txt");
            System.setOut(ps);
            System.out.println(temp);
        }
        hash.remove("E:\\static\\作业\\"+time+"\\"+title);
    }

}
