'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''
'''
Method: recursion O(n) time O(logn) space
'''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = -float('Inf')
        self.helper(root)
        return self.res
        
    def helper(self, root): # function returns max sum contains root with at most 1 branch of root, while tempRes contains root and at most 2 branches
        if not root.left and not root.right: # notice that if only root exists, need to update res too
            if self.res < root.val:
                self.res = root.val
            return root.val
        leftMax = 0
        rightMax = 0
        if root.left: # current node may have only 0,1 child
            leftMax = self.helper(root.left)
        if root.right:
            rightMax = self.helper(root.right)
        tempMax = max(root.val, root.val + leftMax) # attention, path can start from any node to any node, not leaf to leaf
        tempMax = max(tempMax, root.val + rightMax)
        tempMax = max(tempMax, root.val + leftMax + rightMax)
        if tempMax > self.res:
            self.res = tempMax
        curMax = max(root.val, root.val + leftMax)
        curMax = max(curMax, root.val + rightMax)
        return curMax # remember to return
        
'''
Simplify
'''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -float('Inf')
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if not root:
            return 0
        leftMax = max(0, self.helper(root.left))
        rightMax = max(0, self.helper(root.right))
        if self.res < root.val + leftMax + rightMax:
            self.res = root.val + leftMax + rightMax
        return max(leftMax, rightMax) + root.val
