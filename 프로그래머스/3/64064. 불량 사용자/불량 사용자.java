import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class Solution {
    
    private List<List<Integer>> searchId(String[] user_id, String[] banned_id) {
        List<List<Integer>> ret = new ArrayList<>();
        for (int i = 0; i < banned_id.length; i++) {
            ret.add(new ArrayList<>());
        }
        
        for (int i = 0; i < banned_id.length; i++){
            for (int j = 0; j < user_id.length; j++) {
                if (banned_id[i].length() != user_id[j].length()) continue;
                if (check(banned_id[i], user_id[j])) ret.get(i).add(j);
            }
        }        
        return ret;
    }
    
    private boolean check(String ban, String user) {
        char[] s1 = ban.toCharArray();
        char[] s2 = user.toCharArray();
        for (int i = 0; i < ban.length(); i++) {
            if (s1[i] != '*' && s1[i] != s2[i]) return false;
        }
        return true;
    }
    
    private Set<String> matching(List<List<Integer>> ret, int[] visited, int idx) {
        Set<String> set = new HashSet<>();
        if (idx == ret.size()) {
            set.add(Arrays.toString(visited));
            return set;
        }
        List<Integer> temp = ret.get(idx);
        int sum = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (visited[temp.get(i)] == 0) {
                visited[temp.get(i)] = 1;
                set.addAll(matching(ret, visited, idx+1));
                visited[temp.get(i)] = 0;
            }
        }
        return set;
    }
    
    public int solution(String[] user_id, String[] banned_id) {
        int[] visited = new int[user_id.length];
        List<List<Integer>> ret = searchId(user_id, banned_id);
        Set<String> answer = matching(ret, visited, 0);
        return answer.size();
    }
}