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
Queue O(n) time O(n) space
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
        queue = [root]
        while queue:
            nextNodes = [] # nodes for next level
            level = [] # current level vals
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            res.append(level)
            queue = nextNodes
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

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
'''
Queue/Stack O(n) time O(n) space
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
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
            if len(res) % 2 == 1: # reverse the level for zigzag
                start = 0
                end = len(level)
                while start < end:
                    key = level[start]
                    level[start] = level[end]
                    level[end] = key
                    start += 1
                    end -= 1
            res.append(level)
            stack = nextNodes
        return res
        
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        stack = [root]
        while stack:
            nextNodes = [] # nodes for next level
            level = [] # current level vals
            while stack:
                node = stack.pop()
                if len(res) % 2 == 0:
                    if node.left:
                        nextNodes.append(node.left)
                        level.append(node.left.val)
                    if node.right:
                        nextNodes.append(node.right)
                        level.append(node.right.val)
                else:
                    if node.right:
                        nextNodes.append(node.right)
                        level.append(node.right.val)
                    if node.left:
                        nextNodes.append(node.left)
                        level.append(node.left.val)
            if level:
                res.append(level)
            stack = nextNodes
        return res    
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            current = []
            nextNodes = []
            for node in stack:
                current.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            res = [current] + res
            stack = nextNodes
        return res
