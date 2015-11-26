'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
'''
Method: stack O(n) time O(n) space 
'''
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [root]
        while stack:
            nextNodes = []
            for node in stack:
                if not node.left and not node.right: # if the leaf's value equals to sum, return True
                    if node.val == sum:
                        return True
                if node.left: # add value of current node to its children
                    node.left.val += node.val
                    nextNodes.append(node.left)
                if node.right:
                    node.right.val += node.val
                    nextNodes.append(node.right)
            stack = nextNodes
        return False
'''
Method: recursion O(n) time O(n) or O(logn) space?
'''
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
'''
Method: recursion O(n) time
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(root, [], sum)
        return self.res
    
    def helper(self, root, current, sum): # current is a list of value of upper nodes on the path, sum is remained sum exclude values of upper nodes
        if not root:
            return 
        if not root.left and not root.right:
            if root.val == sum:
                key = current[:]
                key.append(root.val)
                self.res.append(key)
        if root.left:
            key = current[:]
            key.append(root.val)
            self.helper(root.left, key, sum - root.val)
        if root.right:
            key = current[:]
            key.append(root.val)
            self.helper(root.right, key, sum - root.val)
