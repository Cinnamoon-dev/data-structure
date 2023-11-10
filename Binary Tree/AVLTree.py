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

    def balanceFactor(self):
        left_depth = self.left.depth()
        right_depth = self.right.depth()

        return left_depth - right_depth

    def leftRotation(self):
        newRoot = self.left
        aux = newRoot.right

        newRoot.right = self
        self.left = aux
        self = newRoot
        return
        
    def rightRotation(self):
        newRoot = self.right
        aux = newRoot.left

        newRoot.left = self
        self.right = aux
        self = newRoot
        return
    
    def doubleRotation(self):
        if self.left is None:
            aux1 = self.right
            aux2 = aux1.left

            aux = self.data
            self.data = aux2.data
            self.left = BinaryTree(aux)
            self.right.left = None
            return
        
        aux1 = self.left
        aux2 = aux1.right

        aux = self.data
        self.data = aux2.data
        self.right = BinaryTree(aux)
        self.left.right = None
        return

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

    def depth(self):
        if self.left is None and self.right is None:
            return 0

        left_depth = 0
        right_depth = 0

        if self.left is not None:
            left_depth = self.left.depth()
        
        if self.right is not None:
            right_depth = self.right.depth()

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(9)
    tree.doubleRotation()
    print(tree)
    print(tree.left)
    print(tree.right)
    # tree.insert(10)
    # tree.insert(5)
    # tree.insert(9)
    # tree.insert(7)
    # tree.insert(23)
    # tree.insert(35)
    # tree.insert(36)
    
    # tree.insert(24)
    # tree.insert(25)
    # tree.insert(26)
    # tree.insert(27)
    # tree.insert(28)
    # tree.insert(29)

    # print(tree.depth())