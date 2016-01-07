Binary Search Tree(BST) == inorder traversal
1. Traversals
  Inorder Traversals:
    self.inorder(root.left)
    do something
    self.inorder(root.right)
  Preorder Traversals:
    do something
    self.preorder()
    self.preorder()
  Postorder Traversals:
    self.postorder()
    self.postorder()
    do something
  Morri's Traversal:
  1) Basic idea:
  move all nodes to the right side of the binary tree, each level has only 1 node, can be recovered after calculated
  * notice that morri's traversl will not add a left child or eliminate a left child, hence if a node has no left child, it will never 
  have a left child, vice versa. Hence node with left child will be explored twice, else once
  2) code:
  cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur: # find rightmost node of left child of original structure
                    pre = pre.right
                if not pre.right: # node has not been explored
                    pre.right = cur
                    cur = cur.left
                else: # node has been explored, recover tree
                    do something
                    pre.right = None
                    cur = cur.right
            else: # node has no left child, it will only be explored once
                do something
                cur = cur.right
  Levelorder Traversals:
  preorder/inorder/queue
  Validate Binary Search Tree，recover BST，balanced binary tree
  
2. Methods:
  1) stack/queue
  flatten binary tree
  2) recursion
  Unique Binary Search Trees ll, same tree, symmetric tree, Maximum Depth of Binary Tree
  3) Dynamic Programming
  Unique Binary Search Trees
  4) DFS, BFS
  balanced binary tree

3. depth()
  1) depth()
    return max(self.depth(root.left), self.depth(root.right)) + 1
  2) 
