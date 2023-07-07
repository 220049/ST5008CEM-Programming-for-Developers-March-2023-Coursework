'''
Question 1
b)
A group of n Pathao riders stood in a queue, and each rider was assigned a unique integer rating based on their performance over the year. The Pathao company planned to distribute gold coins to each rider in ascending order, starting from count 1. The riders with higher ratings should receive more coins than their neighboring riders. The objective was to determine the minimum number of coins required by Pathao to distribute coins to the selected riders according to their ratings.
Input: ratings = [1,0,2]
Output: 5
Explanation: You can give the first, second, and third rider 2, 1, 2 gold coins, respectively.
'''

def minimumCoins(ratings):
    n = len(ratings)
    coins = [1] * n  # Initialize the coins assigned to each rider with 1

    # Traverse from left to right to assign coins based on increasing ratings
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            coins[i] = coins[i-1] + 1

    # Traverse from right to left to adjust coins based on decreasing ratings
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and coins[i] <= coins[i+1]:
            coins[i] = coins[i+1] + 1

    # Return the sum of all the coins assigned
    return sum(coins)

# Example usage:
ratings = [1, 0, 2]
minCoins = minimumCoins(ratings)
print(minCoins)
