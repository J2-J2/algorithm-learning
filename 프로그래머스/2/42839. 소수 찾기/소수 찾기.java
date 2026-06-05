import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;

class Solution {
    
    private List<String> makeNums(int[] visited, StringBuilder sb, char[] nums) {
        
        List<String> ret = new ArrayList<>();
        if (sb.length() != 0) ret.add(sb.toString());
        if (sb.length() == nums.length) {
            return ret;
        }
        
        for (int i = 0; i < visited.length; i++) {
            if (visited[i] == 1) continue;
            
            visited[i] = 1;
            sb.append(nums[i]);
            ret.addAll(makeNums(visited, sb, nums));
            sb.deleteCharAt(sb.length() - 1);
            visited[i] = 0;
        }
        
        return ret;
    }
    
    private int check(int num) {
        if (num == 0 || num == 1) return 0;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return 0;
        }
        return 1;
    }
    
    public int solution(String numbers) {
        int answer = 0;
        char[] nums = numbers.toCharArray();
        int[] visited = new int[numbers.length()];
        Set<Integer> totalNums = new HashSet<>();
        
        List<String> madeList = makeNums(visited, new StringBuilder(), nums);
        for (String str: madeList) {
            totalNums.add(Integer.parseInt(str));
        }
        for (Integer i: totalNums) {
            answer += check(i);
        }
        
        return answer;
    }
}