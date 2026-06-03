class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;
        
        for (int c = 3; c <= total / 2; c++) {
            if (total % c == 0) {
                int r = total / c;
                System.out.println('2');
                if ((2*r + 2*c - 4) == brown) return new int[] {r, c}; 
            }
            
        }
        return new int[] {0, 0};
    }
}