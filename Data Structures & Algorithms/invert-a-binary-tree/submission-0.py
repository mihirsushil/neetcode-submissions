# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None

        q = deque()

        q.append(root)

        
        lvl = 0 

        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                print(curr.val)
                
                curr.left, curr.right = curr.right, curr.left

                if curr.left: 
                    q.append(curr.left)
                if curr.right:
                     q.append(curr.right)
            lvl +=1 
        return root 





        