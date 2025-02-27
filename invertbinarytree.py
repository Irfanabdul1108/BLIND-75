# platform - leetcode
#link - https://leetcode.com/problems/invert-binary-tree/description/
# concept - inverting a given binary tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q1=deque([root])
        while(q1):
            size=len(q1)
            for i in range(size):
                first=q1.popleft()
                first.left,first.right=first.right,first.left
                if(first.left):
                    q1.append(first.left)
                if(first.right):
                    q1.append(first.right)
        return root
        