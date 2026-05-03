class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #langkah 1
        new = Node(data)

        #langkah 2
        if self.root == None:
            self.root = new
            return
            
        #langkah 3
        P = self.root
        Q = self.root

        #langkah 4 
        while Q != None and new.data != P.data:
            
            #langkah 5
            P = Q

            #langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        #langkah 7
        if new.data == P.data:
            print('woi datanya duplikat')
            return
        
        #langkah 8
        if new.data < P.data:
            P.left = new
        else:
            P.right = new

        #selesai

#mem-validasi
bst = BinarySearchTree()

bst.insert(18)
bst.insert(286)
bst.insert(30)
bst.insert(41)
bst.insert(5)

def in_order(node):
    if node is not None :
        in_order(node.left)
        print(node.data, end =" ")
        in_order(node.right)

in_order(bst.root)
