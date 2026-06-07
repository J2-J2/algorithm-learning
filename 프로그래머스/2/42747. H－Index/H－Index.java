import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int answer = 0;
        int idx = 0;
        for (int i = 1; i < 1001; i++) {
            while (idx < citations.length && citations[idx] < i) idx++; 
            if (idx == citations.length) break;
            if (i <= (citations.length - idx)) answer = i;
        }
        return answer;
    }
}