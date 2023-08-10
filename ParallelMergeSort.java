// // Task 6 

// Write a Java program that uses multithreading to implement a parallel merge sort algorithm. 
// Your program should meet the following requirements: 
// 1. Input: Your program should accept an array of integers as input. 
// 2. Output: Your program should output the sorted array. 
// 3. Algorithm: Your program should use a parallel merge sort algorithm to sort the input array. 
// The algorithm should divide the input array into subarrays, sort the subarrays in parallel using multiple threads, 
// and then merge the sorted subarrays to produce the final sorted array. 
// 4. Performance: Your program should be optimized for performance, such that it sorts the input array as quickly as possible. 
// You should experiment with different thread counts and input array sizes to find the optimal settings. 
// 5. Error handling: Your program should handle errors and exceptions gracefully, such as by providing informative error messages 
// and exiting gracefully. 
// 6. Testing: Your program should be thoroughly tested to ensure that it correctly sorts the input array and produces the expected output.
// To complete this assignment, you will need to implement the parallel merge sort algorithm in Java using multithreading. 
// You should also experiment with different thread counts and input array sizes to find the optimal settings for performance. 
// You can use Java's built-in threading and synchronization features, such as the Thread class and synchronized keyword, 
// to implement the parallel merge sort algorithm. 
// import java.util.Arrays;

import java.util.Arrays;



import java.util.Arrays;

public class ParallelMergeSort {

    public static void main(String[] args) {
        int[] inputArray = {9, 4, 7, 1, 3, 6, 8, 2, 5};
        int threadCount = 4; // Experiment with different thread counts

        System.out.println("Input Array: " + Arrays.toString(inputArray));
        parallelMergeSort(inputArray, threadCount);
        System.out.println("Sorted Array: " + Arrays.toString(inputArray));
    }

    // Entry point for the parallel merge sort algorithm
    public static void parallelMergeSort(int[] arr, int threadCount) {
        if (threadCount <= 1) {
            // If the thread count is 1 or less, fall back to sequential merge sort
            mergeSort(arr);
        } else {
            int mid = arr.length / 2;

            // Divide the array into two subarrays
            int[] leftSubarray = Arrays.copyOfRange(arr, 0, mid);
            int[] rightSubarray = Arrays.copyOfRange(arr, mid, arr.length);

            // Create two threads to sort the subarrays in parallel
            Thread leftSorter = new Thread(() -> parallelMergeSort(leftSubarray, threadCount / 2));
            Thread rightSorter = new Thread(() -> parallelMergeSort(rightSubarray, threadCount / 2));

            leftSorter.start();
            rightSorter.start();

            try {
                // Wait for the threads to finish
                leftSorter.join();
                rightSorter.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // Merge the sorted subarrays
            merge(leftSubarray, rightSubarray, arr);
        }
    }

    // Sequential merge sort algorithm
    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) return;

        int mid = arr.length / 2;
        int[] leftSubarray = Arrays.copyOfRange(arr, 0, mid);
        int[] rightSubarray = Arrays.copyOfRange(arr, mid, arr.length);

        mergeSort(leftSubarray);
        mergeSort(rightSubarray);

        merge(leftSubarray, rightSubarray, arr);
    }

    // Merge two sorted subarrays into the original array
    public static void merge(int[] left, int[] right, int[] arr) {
        int leftLength = left.length;
        int rightLength = right.length;
        int i = 0, j = 0, k = 0;

        while (i < leftLength && j < rightLength) {
            if (left[i] < right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < leftLength) {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < rightLength) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }
}
