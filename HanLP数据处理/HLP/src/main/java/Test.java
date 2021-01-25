import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.classification.classifiers.IClassifier;
import com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier;
import com.hankcs.hanlp.classification.models.NaiveBayesModel;
import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.seg.common.Term;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Test {
    public static final String CORPUS_FOLDER = "data\\ourdata\\心态词典";
    public static final String MODEL_PATH = "data/ourdata/classification-model.ser";
    private static IClassifier classifier;
    private static int num1=0,num2=0,num3=0,num4=0,num5=0;
    public static void main(String[] args) throws IOException {
        System.out.println(System.currentTimeMillis());
        classifier=new NaiveBayesClassifier(trainOrLoadModel());
        openFile("data/ourdata/阶段四");
        System.out.println(num1+"  "+num2+"  "+num3+"  "+num4+"  "+num5);
        System.out.println(num1+num2+num3+num4+num5);
        System.out.println(System.currentTimeMillis());
    }

    private static void openFile(String path) throws IOException {
        //递归打开文件，对其进行predict
        File file=new File(path);
        BufferedReader reader;
        String[] filelist=file.list();
        for (int i = 0; i < filelist.length; i++) {
            String str="",tempStr;
            File readfile = new File(path + "\\" + filelist[i]);
            if (!readfile.isDirectory()) {
                reader=new BufferedReader(new FileReader(readfile));
                while ((tempStr=reader.readLine())!=null)
                    str=str+tempStr;
                String predict=predict(classifier,str);
                //if (predict.equals("乐观镇定防疫小知识"))
                //System.out.println(str+"属于"+predict);
                if ("乐观镇定防疫小知识".equals(predict)) {
                    num1++;
                } else if ("愤怒".equals(predict)) {
                    num2++;
                } else if ("担忧疑问".equals(predict)) {
                    num3++;
                } else if ("鼓励感谢夸奖祝福感动".equals(predict)) {
                    num4++;
                } else {
                    num5++;
                }
            } else if (readfile.isDirectory()) {
                openFile(path + "\\" + filelist[i]);
            }
        }
    }
    private static String predict(IClassifier classifier, String text) {
        //情绪预测
        return classifier.classify(text);
    }

    private static NaiveBayesModel trainOrLoadModel() throws IOException
    {  //训练模型用
        NaiveBayesModel model = (NaiveBayesModel) IOUtil.readObjectFrom(MODEL_PATH);
        if (model != null) return model;
        IClassifier classifier = new NaiveBayesClassifier();
        classifier.train(CORPUS_FOLDER);
        model = (NaiveBayesModel) classifier.getModel();
        IOUtil.saveObjectTo(model, MODEL_PATH);
        return model;
    }
    private static final int mod = 1000007;

    public static int hash(String temp){
        //此方法提供了hash值
        char[] c=temp.toCharArray();
        int ans=0;
        for (int i=0;i<c.length;i++){
            int m=(int) c[i];
            ans=(ans+(m*(i+1)%mod))%mod;
        }
        ans=(ans+c.length)%mod;
        return ans;
    }

    public static void totalfreq(String path) throws Exception {
        //此方法用来统计某文件夹中所有txt文件里出现频数最多的100个词语
        File reading=new File(path);
        File[] f=reading.listFiles();
        int[] freq=new int[mod];
        String[] words=new String[mod];
        for (int i=0;i<freq.length;i++){
            freq[i]=0;
        }
        for (File ff:f){
            FileReader fileReaderr=new FileReader(ff.getPath());
            BufferedReader readerr=new BufferedReader(fileReaderr);
            String content=readerr.readLine();
            List<Term> keywordList = HanLP.segment(content);
            for (Term t:keywordList){
                String s=t.word;
                if (freq[hash(s)]!=0&&words[hash(s)].equals(s)) continue;
                int count=0;
                for (File fff:f){
                    FileReader fileReader=new FileReader(fff.getPath());
                    BufferedReader reader=new BufferedReader(fileReader);
                    String con=reader.readLine();
                    if (con.contains(s)) count++;
                }
                if (count>freq[hash(s)]){
                    words[hash(s)]=s;
                    freq[hash(s)]=count;
                }

             //   System.out.println(s+count+"**"+ff.getPath());
            }
        }
       for (int i=0;i<100;i++){
           for (int j=i+1;j<mod;j++){
               if (freq[i]<freq[j]){
                   int t=freq[i];
                   freq[i]=freq[j];
                   freq[j]=t;
                   String tt=words[i];
                   words[i]=words[j];
                   words[j]=tt;
               }
           }
       }
       for (int i=0;i<100;i++){
           System.out.println(words[i]+" "+freq[i]);
       }
    }

    public static void keyword(String frompath,String topath)throws Exception{
        //此方法用来找出frompath下每一个文档的关键词，总文库为所有的文档
        File reading = new File(frompath);
        File[] files = reading.listFiles();
        PrintStream ps = new PrintStream(topath);
        System.setOut(ps);
        for (File read : files) {
            FileReader fileReaderr = new FileReader(read.getPath());
            BufferedReader readerr = new BufferedReader(fileReaderr);
            String content = readerr.readLine();
            System.out.print(read.getPath().substring(15,20)+":");
            List<Term> keywordList = HanLP.segment(content);
            double[] value = new double[keywordList.size()];
            String[] words = new String[keywordList.size()];
            int[] freq = new int[keywordList.size()];
            int[] count = new int[keywordList.size()];
            for (int i = 0; i < keywordList.size(); i++) {
                Term tt = keywordList.get(i);
                words[i] = tt.word;
                count[i] = 0;
                freq[i] = 0;
                for (Term j : keywordList) {
                    if (j.word.equals(words[i])) {
                        count[i]++;
                    }
                }
            }
            int total = 0;
            File folder = new File(frompath);
            File[] f = folder.listFiles();
            for (int i = 0; i < f.length; i++) {
                File ff = f[i];
                FileReader fileReader = new FileReader(ff.getPath());
                BufferedReader reader = new BufferedReader(fileReader);
                String s = reader.readLine();
                total++;
                for (int j = 0; j < keywordList.size(); j++) {
                    if (s.contains(words[j])) {
                        freq[j]++;
                    }
                }
            }
            for (int i = 0; i < keywordList.size(); i++) {
                double tf = (double) count[i] / keywordList.size();
                double idf = Math.log(total / (freq[i] + 1));
                value[i] = tf * idf;
            }
            for (int i = 0; i < keywordList.size() - 1; i++) {
                for (int j = i + 1; j < keywordList.size(); j++) {
                    if (value[i] < value[j]||value[i]==value[j]&&words[i].charAt(0)>words[j].charAt(0)) {
                        String temp;
                        temp = words[i];
                        words[i] = words[j];
                        words[j] = temp;
                        double e;
                        e = value[i];
                        value[i] = value[j];
                        value[j] = e;
                    }
                }
            }
            ArrayList<String> ans = new ArrayList<String>();
            String last = "";
            for (int i = 0; i < keywordList.size(); i++) {
                if (!last.equals(words[i])) {
                    ans.add(words[i]);
                    last = words[i];
                }
            }
            int c = 0;
            for (String word : ans) {
                if (!word.equals("~")&&!word.equals("#") && !word.equals("[") && !word.equals("]") && !word.equals("例")&&(word.charAt(0)<'a'||word.charAt(0)>'z')&&(word.charAt(0)<'0'||word.charAt(0)>'9')) {
                    System.out.print(word + " ");
                    c++;
                }
                if (c == 5) break;
            }
            System.out.println();
        }
    }




}
