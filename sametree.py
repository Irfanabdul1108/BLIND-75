# platform - leetcode
#link - https://leetcode.com/problems/same-tree/
# concept - checking whether both the trees are same or not



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1=deque([p])
        q2=deque([q])
        while(q1 and q2):
            m=q1.popleft()
            n=q2.popleft()
            if p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            elif p is None and q is None:
                return True
            elif m.val!=n.val:
                return False
            if m.left and n.left:
                q1.append(m.left)
                q2.append(n.left)
            elif m.left or n.left:
                return False 
            if m.right and n.right:
                q1.append(m.right)
                q2.append(n.right)
            elif m.right or n.right:
                return False
        return True