'''
1. Definition of Tree Toplology:
  1) If a tree has more than one node, there is a special node root without parent
  2) each other node has a unique parent node and 0 or several children nodes
  1.1 Binary Tree:
    1) root
    2) each other node has a unique parent and 0-2 children nodes
  1.2 Binary search Tree:
    Binary tree with data restored in Inorder Traversal
    
2. Traversals
  2.1 inorder Traversal
  2.11 Definition
  2.22 Realization:
    1) recursion:
      self.inorder(root.left)
      do somthing
      self.inorder(root.right)
    2) stack:
      while current or stack:
        while current:
          stack.append(current)
          current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
  
