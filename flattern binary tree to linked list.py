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
class Solution(object):
    def flatten(self, root): # notice that the original tree is in preorder, and modified linked list is also in preorder
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        current = root
        stack = []
        while current:
            if current.left and current.right:
                stack.append(current.right)
                current.right = current.left
                current.left = None
                current = current.right
            elif current.left:
                current.right = current.left
                current.left = None
                current = current.right
            elif current.right:
                current = current.right
            else:
                if stack:
                    current.right = stack.pop()
                current = current.right
