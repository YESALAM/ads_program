
class LHNode:

    def __init__(self,element):
        self.element = element

    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right
        self.svalue = 0

class LeftistHeap:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None

    def merge(self, leftTree, rightTree):
        if leftTree == None:
            return rightTree
        if rightTree == None:
            return leftTree

        if leftTree.element > rightTree.element:
            temp = leftTree
            leftTree = rightTree
            rightTree = temp

        leftTree.right = self.merge(leftTree.right,rightTree)

        if leftTree.left ==None:
            leftTree.left = leftTree.right
            leftTree.right = None
        else:
            if leftTree.left.svalue < leftTree.right.svalue:
                temp = leftTree.left
                leftTree.left = leftTree.right
                leftTree.right = temp
            leftTree.svalue = leftTree.right.svalue+1
        return leftTree


    def insert(self,x):
        self.root = self.merge(LHNode(x,None,None),self.root)

    # def merge(self,otherTree):
    #     if self==otherTree:
    #         return
    #     root = merge(self.root,otherTree.root)
    #     otherTree.root = None

    def deleteMin(self):
        if self.isEmpty():
            return -1
        else :
            min = self.root.element
            root = self.merge(self.root.left,self.root.right)
            return root

    def print_Tree(self,node, level):
        if node == None:
            return
        else:
            l = level
            value = node.element
            left = node.left
            right = node.right
            print(value)

            if left != None:
                for i in range(0, 5 * l):
                    print(' ', end='')
                print('|__L_', end='')
                self.print_Tree(left, l + 1)
            if right != None:
                for i in range(0, 5 * l):
                    print(' ', end='')
                print('|__R_', end='')
                self.print_Tree(right, l + 1)


x = [50,40,45,35,15,28,15]

x_tree = LeftistHeap()

for i in x:
    x_tree.insert(i)

x_tree.print_Tree(x_tree.root,0)

