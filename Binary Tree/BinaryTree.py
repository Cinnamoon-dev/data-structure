class BinaryTree:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left: BinaryTree = left
        self.right: BinaryTree = right

    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        current = self

        while True:
            if current.data < data:
                nextNode = current.right

                if nextNode is None:
                    current.right = BinaryTree(data)
                    return

                current = current.right

            else:
                nextNode = current.left

                if nextNode is None:
                    current.left = BinaryTree(data)
                    return

                current = current.left

    def listPreOrder(self):
        print(self.data)

        if self.left:
            self.left.listInOrder()

        if self.right:
            self.right.listInOrder()

    def listPosOrder(self):
        if self.left:
            self.left.listInOrder()

        if self.right:
            self.right.listInOrder()

        print(self.data)

    def listInOrder(self):
        if self.left:
            self.left.listInOrder()

        print(self.data)

        if self.right:
            self.right.listInOrder()
 
    def search(self, value):
        current = self

        while True:
            if current.data != value and current.left is None and current.right is None:
                return None

            if current.data == value:
                return current

            if current.data > value:
                nextNode = current.left

                if nextNode is None:
                    return None

                current = current.left

            else:
                nextNode = current.right

                if nextNode is None:
                    return None

                current = current.right

    def delete(self, value):
        subTree = self.search(value)

        if subTree is None:
            return

        ONE_NODE_TREE = subTree.left is None and subTree.right is None
        if ONE_NODE_TREE:
            subTree = None
            return
        
        RIGHT_BRANCH_ONLY = subTree.left is None
        if RIGHT_BRANCH_ONLY:
            subTree.data = subTree.right.data
            subTree.left = subTree.right.left
            subTree.right = subTree.right.right
            return
        
        ONE_NODE_ON_LEFT_BRANCH = subTree.left.right is None
        if ONE_NODE_ON_LEFT_BRANCH:
            subTree.data = subTree.left.data
            subTree.left = subTree.left.left
            return

        aux = subTree.left
        nextAux = aux.right

        while nextAux.right is not None:
            aux = nextAux
            nextAux = nextAux.right
        
        subTree.data = nextAux.data
        
        if nextAux.left is not None:
            aux.left = nextAux.left
        
        aux.right = None
        return

    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    tree = BinaryTree(19)
    tree.insert(10)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    tree.insert(23)
    tree.insert(35)

    tree.listInOrder()