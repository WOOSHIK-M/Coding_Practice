"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/


Given the root of a binary tree, return the inorder traversal of its nodes' values.


-> Exmaple 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

-> Example 2:
Input: root = []
Output: []

-> Example 3:
Input: root = [1]
Output: [1]

-> Example 4:
Input: root = [1,2]
Output: [2,1]

-> Example 5:
Input: root = [1,null,2]
Output: [1,2]

Constraints:
1. The number of nodes in the tree is in the range [0, 100].
2. -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    """TreeNode class."""
    
    def __init__(self,
        val: int=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None
    ) -> None:
        """Initialize."""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], inorder: List[int]) -> None:
        """Implement dfs."""
        if root:
            self.dfs(root.left, inorder)
            # in-place operation
            inorder.append(root.val)
            self.dfs(root.right, inorder)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Inorder Traversal."""
        inorder = []
        self.dfs(root, inorder)
        
        return inorder
