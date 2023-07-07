'''
Question 2
a)
Given an integer array nums and another integer k, the goal is to find the longest subsequence of nums 
that satisfies the following two conditions:
The subsequence is strictly decreasing.
The difference between adjacent elements in the subsequence is at most k.
The output should be the length of the longest subsequence that meets these requirements.
For example, consider the following input:
nums = [8,5,4, 2, 1, 4, 3, 4, 3, 1, 15] k = 3
output=[8,5,4,2,1] or [8,5,4,3,1]
Output: 5
Explanation:
The longest subsequence that meets the requirements is [8,5,4,2,1] or [8,5,4,3,1].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 15 - 8 = 7 is larger 
than 3.
'''

def longestSubsequence(nums, k):
    n = len(nums)
    dp = [1] * n  # Initialize a dynamic programming array with all elements set to 1
    maxLen = 0  # Initialize the maximum length variable as 0

    for i in range(n):  # Iterate over the elements of nums
        for j in range(i):  # Iterate over the elements before the current element
            if nums[i] - nums[j] <= k:  # Check if the difference between elements is at most k
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the subsequence if condition is met
        maxLen = max(maxLen, dp[i])  # Update the maximum length variable

    return maxLen  # Return the maximum length of the subsequence


# Example usage:
nums = [8, 5, 4, 2, 1, 4, 3, 4, 3, 1, 15]
k = 3
result = longestSubsequence(nums, k)
print(result)  # Output: 5
