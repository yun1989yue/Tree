'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
'''
Method: queue O(n) time O(n) space, since the problem asks constant space complexity, need improvement
'''
import Queue
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        currentNodes = Queue.Queue()
        currentNodes.put(root)
        while currentNodes.qsize() != 0:
            nextNodes = Queue.Queue()
            pre = None
            while currentNodes.qsize() != 0:
                node = currentNodes.get()
                if pre:
                    pre.next = node
                if node.left:
                    nextNodes.put(node.left)
                if node.right:
                    nextNodes.put(node.right)
                pre = node
            currentNodes = nextNodes
            
'''
Method: 3 pointers, O(n) time O(1) space
'''
import Queue
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        leftMost = root # start node of each level
        current = root # current node to be explored
        while leftMost.left:
            pre = None # last right child 
            while current:
                if pre:
                    pre.next = current.left
                current.left.next = current.right
                pre = current.right
                current = current.next
            leftMost = leftMost.left
            current = leftMost
