class AVLTree:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left: AVLTree = left
        self.right: AVLTree = right

    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        current = self

        while True:
            if current.data < data:
                nextNode = current.right

                if nextNode is None:
                    current.right = AVLTree(data)
                    return

                current = current.right

            else:
                nextNode = current.left

                if nextNode is None:
                    current.left = AVLTree(data)
                    return

                current = current.left

    def searchUnbalancedNode(self):
        def checkUnbalancedNode(node: AVLTree):
            return (node.balanceFactor() == -2 or node.balanceFactor() == 2) and node.depth() == 2 or self.left is None or self.right is None

        if -2 < self.balanceFactor() < 2:
            return 

        current = self

        while True:
            if checkUnbalancedNode(current):
                return current
            
            if current.left:
                if current.left.depth() == current.depth() - 1:
                    current = current.left
                    continue

            if current.right:
                if current.right.depth() == current.depth() - 1:
                    current = current.right
                    continue

    def insertAVL(self, data):
        self.insert(data)
        
        unbalancedNode = self.searchUnbalancedNode()
        if unbalancedNode is None:
            return

        BalanceFactor = unbalancedNode.balanceFactor()
    
        if BalanceFactor == 2:
            if unbalancedNode.left.right:
                unbalancedNode.leftRightRotation()
                return

            unbalancedNode.rightRotation()
            return
        
        if BalanceFactor == -2:
            if unbalancedNode.right.left:
                unbalancedNode.rightLeftRotation()
                return

            unbalancedNode.leftRotation()
            return
        
    def balanceFactor(self):
        left_depth = 0
        right_depth = 0

        if self.left is not None:
            left_depth = self.left.depth() + 1

        if self.right is not None:    
            right_depth = self.right.depth() + 1

        return left_depth - right_depth

    def rightRotation(self):
        newRoot = self.left
        newRoot.right = AVLTree(self.data)

        self.data = newRoot.data
        self.left = newRoot.left
        self.right = newRoot.right
        return
        
    def leftRotation(self):
        newRoot = self.right
        newRoot.left = AVLTree(self.data)

        self.data = newRoot.data
        self.left = newRoot.left
        self.right = newRoot.right
        return
    
    def leftRightRotation(self):
        self.left.leftRotation()
        self.rightRotation()
        return
    
    def rightLeftRotation(self):
        self.right.rightRotation()
        self.leftRotation()
        return

    def listPreOrder(self):
        print(self.data)

        if self.left:
            self.left.listPreOrder()

        if self.right:
            self.right.listPreOrder()

    def listPosOrder(self):
        if self.left:
            self.left.listPosOrder()

        if self.right:
            self.right.listPosOrder()

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
    tree = AVLTree(10)
    tree.insertAVL(15)
    tree.insertAVL(16)
    tree.insertAVL(14)
    tree.insertAVL(11)

    print(f"root: {tree.data}")
    print(f"left: {tree.left}")
    print(f"right: {tree.right}")
    print(f"bf: {tree.balanceFactor()}")
    print(f"depth: {tree.depth()}")