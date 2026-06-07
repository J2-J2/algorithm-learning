import java.util.stream.IntStream;
import java.util.Set;
import java.util.HashSet;


class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        int[] answer = set.stream().mapToInt(Integer::intValue).sorted().toArray();
        // IntStream.range(0, numbers.length)
        //     .map(i -> IntStream.range(i, numbers.length).)
        return answer;
    }
}