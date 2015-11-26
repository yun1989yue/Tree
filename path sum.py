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
