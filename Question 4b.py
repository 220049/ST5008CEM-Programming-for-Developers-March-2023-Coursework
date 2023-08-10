'''
b)
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are brothers, or false otherwise.
Two nodes of a binary tree are brothers if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode with the given value and optional left and right children.

        Args:
            val (int): The value of the node.
            left (TreeNode, optional): The left child of the node. Defaults to None.
            right (TreeNode, optional): The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


def dfs(node, parent, x, y, depth, results):
    """
    Performs a depth-first search traversal of the binary tree.
    Stores the depth and parent of the target nodes in the results list.

    Args:
        node (TreeNode): The current node being visited.
        parent (TreeNode): The parent of the current node.
        x (int): The value of the first target node.
        y (int): The value of the second target node.
        depth (int): The current depth in the tree.
        results (list): A list to store the results.

    Returns:
        None
    """
    if node is None:
        return

    if node.val == x or node.val == y:
        results.append((node.val, depth, parent))

    dfs(node.left, node, x, y, depth + 1, results)
    dfs(node.right, node, x, y, depth + 1, results)


def areBrothers(root, x, y):
    """
    Checks if the nodes corresponding to values x and y in the binary tree are brothers.
    Returns True if they are brothers, False otherwise.

    Args:
        root (TreeNode): The root of the binary tree.
        x (int): The value of the first target node.
        y (int): The value of the second target node.

    Returns:
        bool: True if the nodes are brothers, False otherwise.
    """
    results = []
    dfs(root, None, x, y, 0, results)

    if len(results) == 2 and results[0][1] == results[1][1] and results[0][2] != results[1][2]:
        return True

    return False


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

x = 4
y = 3
result = areBrothers(root, x, y)
print(result)  # Output: False
