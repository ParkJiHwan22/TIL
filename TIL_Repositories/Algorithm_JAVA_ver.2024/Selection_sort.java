import java.util.Arrays;

public class selection_sort {
    public static void main(String[] args) {
        int[] arr = {32, 17, 83, 43, 49, 22};

        for (int i = 0; i < arr.length - 1; i++) {
            int minNum = 100, minIdx = 0;
            for (int j = i; j < arr.length; j++) {
                if (minNum > arr[j]) {
                    minNum = arr[j];
                    minIdx = j;
                }
            }
            if (minIdx != 0) {
                arr[minIdx] = arr[i];
                arr[i] = minNum;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}