import java.util.Arrays;

public class ProcessUtil {

    public static String unicodeToCn(String unicode) {
        unicode = preProcess(unicode);
        /** 以 \ u 分割，因为java注释也能识别unicode，因此中间加了一个空格*/
        String[] strs = unicode.split("\\\\u");
        String returnStr = "";
        System.err.println(Arrays.toString(strs));
        // 由于unicode字符串以 \ u 开头，因此分割出的第一个字符是""。
        for (int i = 1; i < strs.length; i++) {
            returnStr += (char) Integer.valueOf(strs[i], 16).intValue();
        }
        return returnStr;
    }

    private static String preProcess(String unicode) {
        int index = unicode.lastIndexOf("\\u");
        String result = "";
        while (index != -1) {
            result = unicode.substring(index, index + 6) + result;
            unicode = unicode.substring(0, index);
            index = unicode.lastIndexOf("\\u");
        }
        return result;
    }

    public static void main(String[] args) {
    }

}
