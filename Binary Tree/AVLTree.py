class AVLTree:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left: AVLTree = left
        self.right: AVLTree = right

    def newInsert(self, data):
        """
            Inserts the node, the function used to insert returns a "grandpa" subtree (two nodes up)
            the grandpa subtree is used to check the balance factor after the insertion, as the search
            for the grandpa subtree occurs during the search for the branch to insert the node it is
            faster than the normal method (searching the entire tree again, for the unbalanced node).

            It makes sense returning the grandpa node because the balance factor needed to unbalance
            the tree is 2 or -2 so returning a subtree with the depth of 2 is sufficient to check
            the balance factor.
        """

        def insert(self, data) -> "AVLTree":
            def checkParentalLeftNode(node, value):
                leftValue = None
                rightValue = None

                if node.left:
                    if node.left.left:
                        leftValue = node.left.left.data
                    
                    if node.left.right:
                        rightValue = node.left.right.data
                return value in [leftValue, rightValue]

            if self.data is None:
                self.data = data
                return self

            current = self

            grandpa = self
            count = 1

            while True:
                if count > 2:
                    if checkParentalLeftNode(grandpa, current.data):
                        grandpa = grandpa.left
                    
                    grandpa = grandpa.right

                if current.data < data:
                    count += 1
                    nextNode = current.right

                    if nextNode is None:
                        current.right = AVLTree(data)
                        return grandpa

                    current = current.right

                else:
                    count += 1
                    nextNode = current.left

                    if nextNode is None:
                        current.left = AVLTree(data)
                        return grandpa

                    current = current.left

        unbalancedNode = insert(self, data)

        if -2 < unbalancedNode.balanceFactor() < 2:
            return

        unbalancedNode.balanceNode()

    def searchUnbalancedNode(self):
        """
            The search for an unbalanced node follows a simple logic. There is an invariant when
            looking for a unbalanced subtree: this subtree has more 2 nodes in comparison to every
            other subtree starting from the root. So, when looking for the node you want to descend 
            the difference in depth of the current node and the next node for the deepest subtree 
            is exactly 1, but for every other node the difference in depth is 2.
        """

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

    def balanceNode(self):
        if self.balanceFactor() == 2:
            if self.left.right:
                self.leftRightRotation()
                return

            self.rightRotation()
            return
        
        if self.balanceFactor() == -2:
            if self.right.left:
                self.rightLeftRotation()
                return

            self.leftRotation()
            return

    def insert(self, data):
        """
            Inserts the new node, after the insertion it searches for an unbalanced subtree
            and then rotates the subtree to balance it. It is pretty logical and straightfoward, but
            it is not the faster method available, check newInsert for upgrades.
        """

        def insert(data):
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
        
        insert(data)
        
        unbalancedNode = self.searchUnbalancedNode()
        if unbalancedNode is None:
            return

        unbalancedNode.balanceNode()
        
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
            NOT_FOUND = current.data != value and current.left is None and current.right is None
            if NOT_FOUND:
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

    def search_children(self, value):
        """
            Method create to find a parental node of a node
        """
        current = self

        while True:
            NOT_FOUND = current.left is None and current.right is None
            if NOT_FOUND:
                return None

            if current.left.data == value or current.right.data == value:
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
            parent = self.search_children(value)

            if value > parent.data:
                parent.right = None
                return
            
            parent.left = None
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

        unbalancedNode = self.searchUnbalancedNode()
        unbalancedNode.balanceNode()
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
    tree.insert(15)
    tree.insert(16)
    tree.insert(14)
    tree.insert(11)

    tree.delete(11)
    tree.delete(10)
    tree.delete(14)

    print(f"root: {tree.data}")
    print(f"left: {tree.left}")
    print(f"right: {tree.right}")
    print(f"bf: {tree.balanceFactor()}")
    print(f"depth: {tree.depth()}")