'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = []
        current = root
        while current or stack:
            while current: # add the value to the res when u put it into stack, for inorder, add the value when u pop it out
                res.append(current.val)
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right
        return res
