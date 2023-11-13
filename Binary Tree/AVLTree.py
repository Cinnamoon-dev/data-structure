import copy

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
        # TODO
        # Create an iterative solution based on search method
        if (self.balanceFactor() == -2 or self.balanceFactor() == 2) and self.depth() == 2:
            return self

        if self.left:
            self.left.searchUnbalancedNode()

        if self.right:
            self.right.searchUnbalancedNode()

    def insertAVL(self, data):
        self.insert(data)
        
        unbalancedNode = self.searchUnbalancedNode()
        if unbalancedNode is None:
            return
        print(f"unba: {unbalancedNode.data}")
        print(f"unbaF: {unbalancedNode.balanceFactor()}")

        BalanceFactor = unbalancedNode.balanceFactor()
    
        if BalanceFactor == 2:
            unbalancedNode.rightRotation()

            if unbalancedNode.balanceFactor() == 2:
                unbalancedNode.leftRightRotation()

            return
        
        if BalanceFactor == -2:
            unbalancedNode.leftRotation()

            if unbalancedNode.balanceFactor == -2:
                unbalancedNode.rightLeftRotation()

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

    def doubleRotation(self):
        if self.left is None:
            aux1 = self.right
            aux2 = aux1.left

            aux = self.data
            self.data = aux2.data
            self.left = AVLTree(aux)
            self.right.left = None
            return
        
        aux1 = self.left
        aux2 = aux1.right

        aux = self.data
        self.data = aux2.data
        self.right = AVLTree(aux)
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
    
    def searchAVL(self, value):
        current = self
        BalanceFactor = self.balanceFactor()

        while True:
            if current.depth() < 2:
                return None

            if (current.balanceFactor() == -2 or current.balanceFactor() == 2) and current.depth() == 2:
                return current
            
            # CASO POSITIVO
            if current.left is not None:
                if current.left.depth() >= 2:
                    current = current.left
                    continue

            if current.right is not None:
                if current.right.depth() >= 2:
                    current = current.right
                    continue


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
    print(15)
    tree.insertAVL(15)
    print(16)
    tree.insertAVL(16)
    print(14)
    tree.insertAVL(14)
    print(11)
    tree.insertAVL(11)

    print(f"root: {tree.data}")
    print(f"left: {tree.left}")
    print(f"right: {tree.right}")
    print(f"bf: {tree.balanceFactor()}")
    print(f"depth: {tree.left.depth()}")
    # print(tree.left)
    # print(tree.left)
    # print(tree.right)
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