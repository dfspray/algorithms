class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right

def height(root):
    if root is None:
        return 0

    else:
        rheight = height(root.right)
        lheight = height(root.left)
        if rheight > lheight:
            return rheight + 1
        else:
            return lheight + 1

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.left.left = Node(6)

print height(root)