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
    n = len(a)
    dp = [[0] * (n+2) for _ in range(n+2)]  # Initialize dp matrix to store maximum points at each target position
    pad = [[0] * (n+2) for _ in range(n+2)]  # Initialize pad matrix to store padded targets with value 1

    # Populate the pad matrix with padded targets
    for i in range(1, n+1):
        pad[i][i] = a[i-1]
    pad[0][0] = pad[n+1][n+1] = 1

    # Iterate over target positions
    for l in range(1, n+1):  # l denotes the length of subarray
        for i in range(1, n-l+2):  # i denotes the starting index of subarray
            r = i + l - 1  # r denotes the ending index of subarray
            for k in range(i, r+1):  # k denotes the partition point
                points = dp[i][k-1] + dp[k+1][r] + pad[i][k-1] * a[k-1] * pad[k+1][r]
                dp[i][r] = max(dp[i][r], points)

    return dp[1][n]  # Return the maximum points obtained by shooting all the targets


# Example usage
a = [3, 1, 5, 8]
result = maxPoints(a)
print(result)  # Output: 167
