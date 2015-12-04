'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
'''
Method: recursion O(n) time O(logn) space
'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.left and root.right:
            key = root.left
            root.left = root.right
            root.right = key
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        return root
        
'''
simplify
'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root
        
'''
Method: BFS, queue used
'''
public class Solution {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) {
            return null;
        }

        final Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            final TreeNode node = queue.poll();
            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if(node.left != null) {
                queue.offer(node.left);
            }
            if(node.right != null) {
                queue.offer(node.right);
            }
        }
        return root;
    }
}
