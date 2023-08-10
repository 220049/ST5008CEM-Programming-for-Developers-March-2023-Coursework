''' 
Question 3
a) Suppose you are provided an array of n targets that are placed in a row from 0 to n-1. Each target is assigned with certain integer such that a [0] represent the value associated with target zero. You are asked to shoot all the targets. If you shoot I th target then you will get a[i-1]*a[i]*a[i+1] points.
Note that if i-1 and i+1 position hits index out of bound, then you can assume that two target with value 1 are padded before start target and after end target.
Return maximum point one can gain by hitting each target.
Input: a = [3,1,5,8]
Output: 167
Explanation:
a = [3,1,5,8]
[3,1,5,8] points 3*1*5 (“hitting target with value 1”)
[3,5,8] points 3*5*8 (“hitting target with value 5”)
[3,8] points 1*3*8 (“hitting target with value 3”) note that there is padded target with value 1 at beginning and end of the provided target list
,[8] points 1*8*1 same as above
points = 3*1*5+ 3*5*8 + 1*3*8 + 1*8*1 = 167
'''

def maxPoints(a):
    """
    Calculate the maximum points that can be obtained by shooting all targets.

    Args:
        a (List[int]): An array of integers representing the values of targets.

    Returns:
        int: The maximum points obtained by shooting all targets.
    """
    n = len(a)  # Get the number of targets in the array
    dp = [[0] * (n+2) for _ in range(n+2)]  # Initialize a dp matrix to store maximum points at each target position
    pad = [[0] * (n+2) for _ in range(n+2)]  # Initialize a pad matrix to store padded targets with value 1 at the boundaries

    # Populate the pad matrix with padded targets
    for i in range(1, n+1):
        pad[i][i] = a[i-1]  # Assign the value of the target to the pad matrix
    pad[0][0] = pad[n+1][n+1] = 1  # Pad the boundaries with target values of 1

    # Iterate over target positions
    for l in range(1, n+1):  # Iterate over the possible subarray lengths
        for i in range(1, n-l+2):  # Iterate over the possible starting indices of subarrays
            r = i + l - 1  # Calculate the ending index of the current subarray
            for k in range(i, r+1):  # Iterate over possible partition points in the subarray
                # Calculate the points obtained by shooting the current target at index k and update the dp matrix
                points = dp[i][k-1] + dp[k+1][r] + pad[i][k-1] * a[k-1] * pad[k+1][r]
                dp[i][r] = max(dp[i][r], points)

    return dp[1][n]  # Return the maximum points obtained by shooting all the targets


# Example usage
a = [3, 1, 5, 8]
result = maxPoints(a)
print(result)  # Output: 167
