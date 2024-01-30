import java.util.Arrays;

public class Counting_sort {
    public static void main(String[] args) {
        int[] arr = {0, 4, 1, 3, 1, 2, 4, 1};
        int maxNum = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > maxNum) {
                maxNum = arr[i]; // 배열의 값 중에서 최댓값 찾기
            }
        }

        int[] counts = new int[maxNum+1]; // 배열의 개수 세기
        for (int i = 0; i < arr.length; i++) {
            counts[arr[i]] ++;
        }
//        System.out.println(Arrays.toString(counts));


        int[] prefix = new int[maxNum+1]; // 누적합 배열 만들기
        prefix[0] = counts[0];
        for (int i = 1; i < maxNum+1; i++) {
            prefix[i] += prefix[i-1] + counts[i];
        }
//        System.out.println(Arrays.toString(prefix));

        int[] res = new int[arr.length]; // 위치 찾기 (뒤에서부터)
        for (int i = arr.length - 1; i >= 0; i--) {
            res[--prefix[arr[i]]] = arr[i];
        }
        System.out.println(Arrays.toString(res));

    }
}
