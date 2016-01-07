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
        while currentNodes.qsize() != 0: # can not use while currentNodes, because it is True even there is no elem
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
Method: preorder O(n) time O(logn) space (perfect tree, logn levels)
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root or not root.left: # need to judge whether it is leaf too
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
'''
Method: 3 pointers, O(n) time O(1) space
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        leftMost = root # start node of each level
        while leftMost.left:
            current = leftMost # current node to be explored
            pre = None # last right child, also u can use a if condition to connect current.right and current.next.left, but with pre is more clear to understand 
            while current:
                if pre:
                    pre.next = current.left
                current.left.next = current.right
                pre = current.right
                current = current.next
            leftMost = leftMost.left
            
'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
        1
       / \
      2   3
     / \   \
    4   5   7
After calling your function, the tree should look like:
        1 -> NULL
       / \
      2-> 3 -> NULL
     / \   \
    4-> 5-> 7 -> NULL
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        leftMost = root
        while leftMost:
            current = leftMost
            nextLeftMost = None
            pre = None
            while current:
                if current.left and current.right:
                    current.left.next = current.right
                    if pre:
                        pre.next = current.left
                    if not nextLeftMost:
                        nextLeftMost = current.left
                    pre = current.right
                elif current.left:
                    if pre:
                        pre.next = current.left
                    if not nextLeftMost:
                        nextLeftMost = current.left
                    pre = current.left
                elif current.right:
                    if pre:
                        pre.next = current.right
                    if not nextLeftMost:
                        nextLeftMost = current.right
                    pre = current.right
                current = current.next
            leftMost = nextLeftMost
