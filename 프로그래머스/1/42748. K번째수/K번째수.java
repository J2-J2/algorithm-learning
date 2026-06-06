import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < commands.length; i++) {
            int[] target = commands[i];
            List<Integer> list = IntStream.range(target[0]-1, target[1])
                .map(p -> array[p])
                .sorted()
                .boxed()
                .collect(Collectors.toList());
            answer.add(list.get(target[2] - 1));
        }
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}