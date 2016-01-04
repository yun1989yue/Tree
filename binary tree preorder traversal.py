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
'''
Queue: O(n) time O(n) space
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
        
'''
Method: recursion
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.helper(root.left)
        self.helper(root.right)

'''
Morri's O(n) time O(1) space
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
            else: # node has no left child, it will only be explored once
                res.append(cur.val)
                cur = cur.right
        return res
