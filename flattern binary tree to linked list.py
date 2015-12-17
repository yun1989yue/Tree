'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
'''
Method: O(n) time stack O(n) space
'''
class Solution(object):
    def flatten(self, root): # notice that the original tree is in preorder, and modified linked list is also in preorder
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        current = root
        while current: # when make cases study, analyze each case(l&r,l,r,not l & not r) rigorously
            if current.left:
                if current.right:
                    stack.append(current.right)
                current.right = current.left
                current.left = None
            elif not current.left and not current.right:
                if stack:
                    current.right = stack.pop()
            current = current.right
                
'''
Method: recursion
reverse postorder traversal [6,5,4,3,2,1]
'''
class Solution(object):
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
