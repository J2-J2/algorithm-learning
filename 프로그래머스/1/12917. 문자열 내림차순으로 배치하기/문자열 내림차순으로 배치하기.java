import java.util.Arrays;
class Solution {
    public String solution(String s) {
        StringBuilder up = new StringBuilder();
        StringBuilder lo = new StringBuilder();
        
        for (char c: s.toCharArray()) {
            if (Character.isUpperCase(c)) up.append(c);
            else lo.append(c);
        }
        char[] up1 = up.toString().toCharArray();
        char[] lo1 = lo.toString().toCharArray();
        
        Arrays.sort(up1);
        Arrays.sort(lo1);
        StringBuilder ret = new StringBuilder();
        for (int i = lo1.length-1; i >= 0; i--) {
            ret.append(lo1[i]);
        }
        for (int i = up1.length-1; i >= 0; i--) {
            ret.append(up1[i]);
        }
        
        
        return ret.toString();
    }
}