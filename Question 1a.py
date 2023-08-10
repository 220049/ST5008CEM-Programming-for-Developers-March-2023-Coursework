'''
Question 1
a)
A trio of friends planned to purchase clothing from a particular store for an upcoming party, 
intending to wear matching outfits in varying colors - black, blue, and pink. 
The store had three different clothing sets on display, each in a different color. 
The shopkeeper assisted the three friends by selecting a clothing set in the appropriate color for 
each person based on their body shape and size. Given a 2D array, price[][3], where price[i][0], 
price[i][1], and price[i][2] represent the price of each clothing set for a different colored outfit 
for person i, your objective is to determine the minimum cost required to purchase clothing such that 
each person wears have different color clothes if they stand in a row.
It should be noted that any two people can wear the same color cloth, but the third person must wear 
various color cloths, and all three can wear different colored garments.
Input: N = 3, price[][3] = [{14, 4, 11}, {11, 14, 3}, {14, 2, 10}] 
Output: 9 Explanation: Person 1 chooses blue clothing cost=4. Person 2 chooses pink clothing. 
Cost = 3. Person 3 chooses blue clothing. Cost = 2.
As a result, the total cost = 2 + 5 + 3 = 9.
Note: algorithm must take Time Complexity: O(N) Auxiliary Space: O(1)
'''

def findMinimumCost(prices):
    """
    Calculate the minimum cost required to purchase clothing sets for three friends.

    Args:
        prices (List[List[int]]): A 2D array where prices[i][0], prices[i][1], and prices[i][2] represent
                                  the price of each clothing set for a different colored outfit for person i.

    Returns:
        int: The minimum cost required to purchase clothing sets such that each person wears a different color
             and the third person wears a various color cloth.
    """
    # Initialize the minimum costs for the first person wearing each color
    minCost1 = prices[0][0]  # Minimum cost for person 1 wearing the first color
    minCost2 = prices[0][1]  # Minimum cost for person 1 wearing the second color
    minCost3 = prices[0][2]  # Minimum cost for person 1 wearing the third color

    # Iterate over the prices array for each person starting from the second person (index 1)
    for i in range(1, len(prices)):
        # Calculate the new minimum costs for the current person
        
        # Calculate the new minimum cost for the current person wearing the first color.
        newMinCost1 = min(minCost2, minCost3) + prices[i][0]
        
        # Calculate the new minimum cost for the current person wearing the second color.
        newMinCost2 = min(minCost1, minCost3) + prices[i][1]
        
        # Calculate the new minimum cost for the current person wearing the third color.
        newMinCost3 = min(minCost1, minCost2) + prices[i][2]
        
        # Update the minimum costs for the current person.
        minCost1 = newMinCost1
        minCost2 = newMinCost2
        minCost3 = newMinCost3

    # Return the minimum cost among the three persons' costs.
    return min(minCost1, minCost2, minCost3)

# Test the function with sample prices
prices = [[14, 4, 11], [11, 14, 3], [14, 2, 10]]
minCost = findMinimumCost(prices)
print("Minimum cost:", minCost)
