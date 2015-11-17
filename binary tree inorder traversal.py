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
        #boundary cases are considered in the code
        stack = []
        res = []
        cur = root
        while cur:
            if cur.left:
                stack.append(cur)
                cur = cur.left
            else:
                res.append(cur.val)
                if cur.right:
                    cur = cur.right
                else:
                    flag = 0
                    while stack:
                        cur = stack.pop()
                        res.append(cur.val)
                        if cur.right:
                            cur = cur.right
                            flag = 1
                            break
                        else:
                            cur = None
                    if flag == 0:
                        break
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
recurtion
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
morri's traversal O(n) time O(1) space
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:# if a node has left node, move the node to the rightmost child of its left node
                pre =cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur
                cur = cur.left
                pre.right.left = None
        return res
