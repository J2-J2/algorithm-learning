import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = Arrays.stream(strings)
            .sorted((s1, s2) -> {
                if (s1.charAt(n) != s2.charAt(n)) {
                    return s1.charAt(n) - s2.charAt(n);}
                return s1.compareTo(s2);
                }
                   )
            .toArray(String[]::new);
        return answer;
    }
}