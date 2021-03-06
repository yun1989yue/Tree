'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.first = None
        self.second = None
        self.last = None
        self.depth = 0 
        self.LCA = None # the node with smallest depth along the path between p and q is LCA
        self.helper(root, p, q, 0)
        return self.LCA
        
    def helper(self, root, p, q, depth):
        if not root:
            return
        self.helper(root.left, p, q, depth + 1)
        if not self.first:
            if (root == p or root == q):
                self.first = root
                if root == p:
                    self.last = q
                else:
                    self.last = p
                self.LCA = root
                self.depth = depth
        else:
            if not self.second:
                if depth < self.depth:
                    self.LCA = root
                    self.depth = depth
                if root == self.last:
                    self.second = root
        self.helper(root.right, p, q, depth + 1)
