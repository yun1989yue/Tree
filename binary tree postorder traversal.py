'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,2,3,4,5,6,7},
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
return [4,5,2,6,7,3,1].
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        leftTra = self.postorderTraversal(root.left)
        rightTra = self.postorderTraversal(root.right)
        return leftTra + rightTra +[root.val]
'''
Method: stack, use preorder traverses from right to left, then reverse the answer
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        current = root
        stack = []
        while current or stack:
            while current:
                res = [current.val] + res
                stack.append(current)
                current = current.right
            current = stack.pop()
            current = current.left
        return res
