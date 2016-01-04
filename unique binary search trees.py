'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
'''
Method:
D.P. O(n^2) time O(n) space
Basic idea: 
1) subtree of BST is still BST 
2) for root with val i, there are i-1 nodes at left subtree and n - i nodes at right subtree
3) for n nodes BST, numTrees[n] = sum(numTrees[i-1]*numTrees[n-i]), i from 1 to n
* notice that numTrees[0] = 1 should be used for latter cases
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        res = [1,1,2] # when n = 0, [None] should be calculated rather than []
        for i in xrange(3, n+1):
            tempRes = 0
            for j in xrange(1, i+1):
                tempRes += res[j-1]*res[i-j]
            res.append(tempRes)
        return res[-1]
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
'''
Method: recursion
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(n, 0)# need another parameter to add a base number to each node if it's right subtree of a node 
        
    def helper(self, n, base): 
        if n == 0:
            return [None] # return [None] rather than [] can simplify the code
        if n == 1:
            return [TreeNode(1 + base)] 
        res = []
        for i in xrange(1, n+1):
            leftNodes = self.helper(i-1, base) # important, this is the left subtree of current node, but base comes from higher level
            rightNodes = self.helper(n-i, i + base) # base !!!
            for l in leftNodes:
                for r in rightNodes:
                    cur = TreeNode(i + base) # base !!! not only i
                    res.append(cur)
                    cur.left = l
                    cur.right = r
        return res
'''
Another recursion
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)
        
    def helper(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        res = []
        for i in xrange(start, end+1):
            leftNodes = self.helper(start, i-1)
            rightNodes = self.helper(i+1, end)
            for l in leftNodes:
                for r in rightNodes:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
