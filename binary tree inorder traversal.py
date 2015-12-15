'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

'''
m1:
1) if current node has left node, it can not be added to the res at current time, put it into the stack and explore the left 
node
2) if current node is leaf, add it to the res and check its right, if not exists, pop node from the stack, add to the res until 
the stack exhausts or poped node has right node
*notice that 2) has two braches, need to right node or exhaust, need case study
'''

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #base cases are considered in the code
        stack = []
        res = []
        cur = root
        while cur:
            if cur.left:
                stack.append(cur)
                cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right
                while not cur and stack: # if cur.right == None, explore node in stack
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
        return res
'''
m2:
DFS? explore all the left nodes, then explore its right nodes
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
'''
m3:
recurtion1 O(n) time O(logn) space
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
'''
m4:
recursion2 O(n) time O(logn) space
'''
class Solution(object):
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #base cases are considered in the code
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)

'''
m5:
morri's traversal O(n) time O(1) space
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #base cases are considered in the code
        res = []
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur: # find rightmost node of left child in terms of original structure
                    pre = pre.right
                if not pre.right: # node has not been explored
                    pre.right = cur
                    cur = cur.left
                else: # node has been explored, recover tree
                    res.append(cur.val)
                    pre.right = None
                    cur = cur.right
            else: # node doesnt have left child in original structure
                res.append(cur.val)
                cur = cur.right
        return res
