import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] firstPerson = {1, 2, 3, 4, 5};
        int[] secondPerson = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] thirdPerson = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[][] person = {firstPerson, secondPerson, thirdPerson};
        int[] count = {0, 0, 0};
        
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < 3; j++) {
                if (answers[i] == person[j][i%person[j].length]) count[j]++;
            }
        }
        
        int maxVal = 0;
        for (int i = 0; i < 3; i++) {
            if (maxVal < count[i]) maxVal = count[i];
        }
        List<Integer> result = new ArrayList<>(); 
        for (int i = 0; i < 3; i++) {
            if (maxVal == count[i]) result.add(i);
        }
        int[] ret = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ret[i] = result.get(i) + 1;
        }
        return ret;
    }
}