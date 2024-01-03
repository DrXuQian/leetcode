'''
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
'''
from typing import Optional

from utils import deserialize, TreeNode


# Definition for a binary tree node.


class Solution:
    def flatten_as_list(self, root: TreeNode):
        if root.left is None and root.right is None:
            return root, root
        elif root.right is None:
            left_head, left_tail = self.flatten_as_list(root.left)
            root.right = left_head
            root.left = None
            left_tail.right = None
            return root, left_tail
        elif root.left is None:
            right_head, right_tail = self.flatten_as_list(root.right)
            root.right = right_head
            root.left = None
            return root, right_tail
        else:
            left_head, left_tail = self.flatten_as_list(root.left)
            right_head, right_tail = self.flatten_as_list(root.right)
            root.right = left_head
            root.left = None
            left_tail.right = right_head
            return root, right_tail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten_as_list(root)
        return

root = '[0]'

root = deserialize(root)
Solution().flatten(root)
