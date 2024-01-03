from typing import Optional, List
from utils import TreeNode, deserialize


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            head = stack.pop()
            ret.append(head.val)
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
        return ret


root = '[1,2,null,3]'


root = deserialize(root)
Solution().preorderTraversal(root)
