/*
Question 6

Write a Java program that uses multithreading to implement a parallel merge sort algorithm. Your program should meet the following requirements:
1. Input: Your program should accept an array of integers as input.
2. Output: Your program should output the sorted array.
3. Algorithm: Your program should use a parallel merge sort algorithm to sort the input array. The algorithm should divide the input array into subarrays, sort the subarrays in parallel using multiple threads, and then merge the sorted subarrays to produce the final sorted array.
4. Performance: Your program should be optimized for performance, such that it sorts the input array as quickly as possible. You should experiment with different thread counts and input array sizes to find the optimal settings.
5. Error handling: Your program should handle errors and exceptions gracefully, such as by providing informative error messages and exiting gracefully.
6. Testing: Your program should be thoroughly tested to ensure that it correctly sorts the input array and produces the expected output.
To complete this assignment, you will need to implement the parallel merge sort algorithm in Java using multithreading. You should also experiment with different thread counts and input array sizes to find the optimal settings for performance. You can use Java's built-in threading and synchronization features, such as the Thread class and synchronized keyword, to implement the parallel merge sort algorithm. 
*/

import java.util.Arrays;

public class ParallelMergeSort {
    private static final int NUM_THREADS = Runtime.getRuntime().availableProcessors(); // Use all available cores

    // Entry point for parallel merge sort
    public static void parallelMergeSort(int[] arr) {
        parallelMergeSort(arr, 0, arr.length - 1, NUM_THREADS);
    }

    // Recursive function for parallel merge sort
    private static void parallelMergeSort(int[] arr, int left, int right, int numThreads) {
        if (numThreads <= 1) {
            // If only one thread available or reached the threshold, perform sequential merge sort
            mergeSort(arr, left, right);
            return;
        }

        // Divide the array into two halves
        int mid = left + (right - left) / 2;

        // Create and start threads to sort each half in parallel
        Thread leftThread = new Thread(() -> parallelMergeSort(arr, left, mid, numThreads / 2));
        Thread rightThread = new Thread(() -> parallelMergeSort(arr, mid + 1, right, numThreads - numThreads / 2));
        leftThread.start();
        rightThread.start();

        // Wait for both threads to complete
        try {
            leftThread.join();
            rightThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }

    // Sequential merge sort function
    private static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            // Recursively divide and sort the array
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            // Merge the two sorted halves
            merge(arr, left, mid, right);
        }
    }

    // Merge two sorted subarrays
    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        // Copy data to temporary arrays
        System.arraycopy(arr, left, leftArray, 0, n1);
        System.arraycopy(arr, mid + 1, rightArray, 0, n2);

        int i = 0, j = 0, k = left;
        // Merge the two subarrays
        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k++] = leftArray[i++];
            } else {
                arr[k++] = rightArray[j++];
            }
        }

        // Copy remaining elements of leftArray if any
        while (i < n1) {
            arr[k++] = leftArray[i++];
        }

        // Copy remaining elements of rightArray if any
        while (j < n2) {
            arr[k++] = rightArray[j++];
        }
    }

    public static void main(String[] args) {
        int[] arr = {6, 4, 3, 2, 8, 5, 1, 7};

        System.out.println("Original Array: " + Arrays.toString(arr));
        parallelMergeSort(arr);
        System.out.println("Sorted Array: " + Arrays.toString(arr));
    }
}
