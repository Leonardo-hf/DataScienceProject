import org.apache.commons.io.FileUtils;

import java.io.File;

public class hash {
    private static final int mod = 1000000007;
    public static boolean[] h=new boolean[mod+1];
    public static int cal(String temp){
        char[] c=temp.toCharArray();
        int ans=0;
        for (int i=0;i<c.length;i++){
            int m=(int) c[i];
            ans=(ans+(m*(i+1)%mod))%mod;
        }
        ans=(ans+c.length)%mod;
        return ans;
    }
    public static void remove(String path)throws Exception{
    // 用来去重
        int count=0;
        File folder = new File(path);
        File[] listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            File file = listOfFiles[i];
            if (file.isFile() && file.getName().endsWith(".txt")) {
                String content = FileUtils.readFileToString(file);
                if (content.length()<=5) continue;;
                if (h[cal(content)]==false){
                    h[cal(content)]=true;
                }else{
                    file.delete();
                }

            }
        }
    }
}
