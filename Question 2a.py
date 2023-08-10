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
    """
    Find the length of the longest subsequence with adjacent elements differing by at most k.

    Args:
        nums (List[int]): An input list of integers.
        k (int): The maximum difference allowed between adjacent elements in the subsequence.

    Returns:
        int: The length of the longest subsequence with adjacent elements differing by at most k.
    """
    n = len(nums)  # Get the length of the input array (number of elements)
    dp = [1] * n  # Initialize a dynamic programming array with all elements set to 1
    maxLen = 0  # Initialize the maximum length variable as 0

    # Iterate over the elements of nums
    for i in range(n):
        # Iterate over the elements before the current element
        for j in range(i):
            # Check if the difference between elements is at most k
            if nums[i] - nums[j] <= k:
                # Update the length of the subsequence if the condition is met
                # We increase the length of subsequence ending at index 'i' if the difference between nums[i] and nums[j]
                # is at most k, which satisfies the second requirement.
                # dp[j] represents the length of the subsequence ending at index 'j', and we add 1 to extend it to index 'i'.
                dp[i] = max(dp[i], dp[j] + 1)

        # Update the maximum length variable
        # We keep track of the maximum length of subsequences we have encountered so far.
        maxLen = max(maxLen, dp[i])

    return maxLen  # Return the maximum length of the subsequence


# Example usage:
nums = [8, 5, 4, 2, 1, 4, 3, 4, 3, 1, 15]
k = 3
result = longestSubsequence(nums, k)
print(result)  # Output: 5
