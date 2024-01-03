# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils import TreeNode, deserialize


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx + 1:]
        if left_inorder:
            root.left = self.buildTree(preorder, left_inorder)
        if right_inorder:
            root.right = self.buildTree(preorder, right_inorder)
        return root