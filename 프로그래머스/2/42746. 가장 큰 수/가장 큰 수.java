import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] numbers) {
        boolean zero = false;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] != 0) zero = true;
        }
        if (!zero) return "0";
        
        String answer = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted((n1, n2) -> {
                return n2.repeat(3).compareTo(n1.repeat(3));
            })
            .collect(Collectors.joining());
        return answer;
    }
}