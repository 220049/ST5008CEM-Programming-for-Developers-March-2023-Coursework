'''
Question 1
b)
A group of n Pathao riders stood in a queue, and each rider was assigned a unique integer rating based on their performance over the year. The Pathao company planned to distribute gold coins to each rider in ascending order, starting from count 1. The riders with higher ratings should receive more coins than their neighboring riders. The objective was to determine the minimum number of coins required by Pathao to distribute coins to the selected riders according to their ratings.
Input: ratings = [1,0,2]
Output: 5
Explanation: You can give the first, second, and third rider 2, 1, 2 gold coins, respectively.
'''

def minimumCoins(ratings):
    """
    Calculate the minimum number of coins required to distribute to riders based on their ratings.

    Args:
        ratings (List[int]): A list of unique integer ratings assigned to each rider.

    Returns:
        int: The minimum number of coins required to distribute to riders while maintaining the ascending order of coins based on ratings.
    """
    n = len(ratings)  # Get the number of riders (n)

    # Step 1: Initialize each rider with 1 coin (minimum possible)
    coins = [1] * n  # Create an array to store the number of coins assigned to each rider

    # Step 2: Traverse from left to right to ensure riders with higher ratings get more coins
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            coins[i] = coins[i-1] + 1
        # If the current rider's rating is higher than the previous rider's rating,
        # assign one more coin than the previous rider. This maintains the increasing order of coins.

    # Step 3: Traverse from right to left to adjust coins based on neighboring ratings
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and coins[i] <= coins[i+1]:
            coins[i] = coins[i+1] + 1
        # If the current rider's rating is higher than the next rider's rating and
        # the current rider has fewer or equal coins, adjust the current rider's coins.
        # This ensures that riders with higher ratings than their neighbors get more coins.

    # Step 4: Calculate the total minimum coins required by summing up all assigned coins
    totalCoins = sum(coins)

    # Step 5: Return the total minimum coins required
    return totalCoins

# Example usage:
ratings = [1, 0, 2]
minCoins = minimumCoins(ratings)
print(minCoins)
