class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None

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
root.left.right.right = Node(7)
root.right.right = Node(10)

print(height(root)-1)

#Important points:
#Recusion allows you to work from the bottom up. The height of the highest point will always return a number higher
#Than the height of an unimportant node
#We are storing a class in a class in a class in order to build the tree
#Data, or info in this example is just storing the value that node is.


def level_order(root):
    traversal_dict = {}
    level = 0

    def level_lookup(root, level):
        if root is None:
            print(None)
        traversal_dict.setdefault(level, []).append(str(root.info))
        level += 1
        if root.left:
            level_lookup(root.left, level)
        if root.right:
            level_lookup(root.right, level)

    level_lookup(root, level)
    list_of_lists = [value for value in traversal_dict.values()]
    ordered_list = []
    for item in list_of_lists:
        for thing in item:
            ordered_list.append(thing)

    print(' '.join(ordered_list))

#Important points:
#Dictionaries can be used to index the levels of a binary tree

def is_balanced(brackets):
    message = None
    for index in range(0, int(len(brackets)/2)):
        print(index)
        brackets_dict = {']': '[', ')': '(', '}': '{'}
        opposite = brackets[len(brackets) - index - 1]
        if brackets[index] != brackets_dict.get(opposite):
            message = "NO"
    if message is None:
        message = "YES"
    print(message)

test1 = '{[()]}'
test2 = '{[(])}'
test3 = '{{[[(())]]}}'

#k is the levels you want to swap in the queries input array
#indexes contains the nodes of the tree, the first being the root

class flipBinaryTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            if root.left or root.right:
                root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
        return root

class findLongestPath:
    def __init__(self):
        self.longest = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def recursion(node, level = 1):
            if node:
                left = recursion(node.left, level + 1)
                right = recursion(node.right, level + 1)
                self.longest = max(self.longest, left - level + right - level)
                return max(left, right)
            else:
                return level - 1
        recursion(root)
        return self.longest



if __name__ == '__main__':
    level_order(root)
    is_balanced(test1)
    is_balanced(test2)
    is_balanced(test3)

