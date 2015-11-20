'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
'''
Method:
Stack O(n) time O(n) space
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            nextNodes = [] # nodes for next level
            level = [] # current level vals
            for node in stack:
                level.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            res.append(level)
            stack = nextNodes
        return res
'''
Method:
recursion:
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(root, 0)
        return self.res
        
    
    def helper(self, root, depth):
        if not root:
            return
        if len(self.res) == depth: # if the new depth reached, assign a space for this level
            self.res.append([])
        self.res[depth].append(root.val)
        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)
