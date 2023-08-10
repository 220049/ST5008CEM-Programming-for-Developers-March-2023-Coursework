'''
Question 2
b)
Given an integer value k and an array of integers representing blacklisted ports, create an algorithm 
that outputs a random port (an integer value between 0 and k-1) that is also a whitelisted port 
(meaning it is not in the array of blacklisted ports). The goal is to minimize the number of built-in 
random calls in the algorithm.
The program should have two inputs: k, an integer value, and blacklisted_ports, an array of integers. 
The program should also have a get() function that returns a whitelisted random number between 0 and k-1. 
The algorithm should be optimized to reduce the number of built-in random calls required.
Example 1:
Input
["Program", "get", "get "get", "get", "get"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
Output
[null, 0, 4, 6,1,4]
Explanation
program p = new program(7, [2, 3, 5]);
p.get(); // return 0, any number from [0,1,4,6] should be ok. Note that for every call of pick,
// 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
p.get(); // return 4
'''

import random

class Program:
    """
    A class that generates whitelisted random ports based on blacklisted ports.

    Attributes:
        k (int): The maximum port value (inclusive).
        blacklisted_ports (set): A set of integers representing blacklisted ports.
        whitelisted_ports (list): A list of generated whitelisted ports.
    """
    def __init__(self, k, blacklisted_ports):
        """
        Initialize the Program class with maximum port value (k) and blacklisted ports.

        Args:
            k (int): The maximum port value (inclusive).
            blacklisted_ports (List[int]): A list of integers representing blacklisted ports.
        """
        self.k = k  # Store the maximum port value (k)
        self.blacklisted_ports = set(blacklisted_ports)  # Convert blacklisted_ports to a set for efficient lookup
        self.whitelisted_ports = []  # Initialize an empty list to store whitelisted ports

    def get(self):
        """
        Generate a whitelisted random port between 0 and k-1.

        Returns:
            int or None: A whitelisted random port or None if all whitelisted ports have been generated.
        """
        # Check if all whitelisted ports have been generated
        if len(self.whitelisted_ports) == self.k - len(self.blacklisted_ports):
            return None  # Return None when all whitelisted ports have been generated
        
        while True:
            # Generate a random port between 0 and k-1
            port = random.randint(0, self.k - 1)
            
            # Check if the generated port is not in the blacklisted ports set
            if port not in self.blacklisted_ports:
                # Add the port to the list of whitelisted ports
                self.whitelisted_ports.append(port)
                # Return the generated whitelisted port
                return port

# Example usage:
# Create an instance of the Program class with k=7 and blacklisted_ports=[2, 3, 5]
p = Program(7, [2, 3, 5])

# Call the get method to generate a whitelisted random port and print the result
print(p.get())  # Output: A whitelisted random port (e.g., 0)

# Call the get method again to generate another whitelisted random port and print the result
print(p.get())  # Output: Another whitelisted random port (e.g., 4)
