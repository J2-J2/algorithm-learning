class Solution {
    private class Dictionary {
            public static char[] alpha = {'A', 'E', 'I', 'O', 'U'};    

            public static int mul(int n, int rank) {
                int total = 0;
                int ret = 1;
                for (int j = n+1; j < 5; j++) {
                    ret *= 5;
                    total += rank * ret;
                }
                return total;
            }

            public static int check(char c) {
                for (int i = 0; i < 5; i++) {
                    if (alpha[i] == c) return i+1;
                }
                return -1;
            }
        }
    
    public int solution(String word) {
        int answer = 0;
        int rank;
        
        Dictionary dictionary = new Dictionary();
        char[] array = word.toCharArray();
        for (int i = 0; i < array.length; i++) {
            rank = dictionary.check(array[i]);
            answer += dictionary.mul(i, rank - 1);
            answer += rank;
            
        }
        return answer;
    }
}