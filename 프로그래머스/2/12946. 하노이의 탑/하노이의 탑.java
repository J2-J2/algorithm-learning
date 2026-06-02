import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    
    private static class Hanoi {
        public static List<List<int[]>> possible = new ArrayList<>();
        public static int[] ret;
        public static int n;
        
        public static List<int[]> move(int n, int start, int mid, int end) {
            for (List<int[]> target: possible) {
                if (Arrays.equals(target.get(0), new int[] {n, start, mid, end})) {
                    return target.subList(1, target.size());
                }
            }
            return new ArrayList<>();
        }
        
        public static List<int[]> play(int n, int start, int mid, int end) {
            List<int[]> prev;
            List<int[]> post;
            List<int[]> tempHistory = new ArrayList<>();
            
            if (n - 1 == 0) {
                prev = new ArrayList<>();
                post = new ArrayList<>();
            }
            else {
                List<int[]> next = move(n, start, end, mid);
                if (next.size() != 0) return next;
                prev = play(n-1, start, end, mid);
                post = play(n-1, mid, start, end);
            }
            tempHistory.add(new int[] {n, start, mid, end});
            tempHistory.addAll(prev);
            tempHistory.add(new int[] {start, end});
            tempHistory.addAll(post);
            
            possible.add(tempHistory);
            return tempHistory.subList(1, tempHistory.size());
        }
        
    }
    
    public int[][] solution(int n) {
        List<int[]> hanoi = Hanoi.play(n, 1, 2, 3);
        int[][] array = hanoi.toArray(new int[hanoi.size()][]);
        return array;
    }
}