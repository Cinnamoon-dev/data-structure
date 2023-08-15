import copy

class Tree:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data=None) -> None:
        if data is None:
            return

        if self.data is None:
            self.data = data
            return
        
        current = self

        while True:
            parent = current
            
            if data > current.data:
                current = current.right

                if current is None:
                    parent.right = Tree(data)
                    return

                continue
            
            if data < current.data:
                current = current.left

                if current is None:
                    parent.left = Tree(data)
                    return

    def printPreOrder(self):
        if self.data is not None:
            print(self.data)
        
        if self.left is not None:
            self.left.preOrder()
        
        if self.right is not None:
            self.right.preOrder()  
    
    def preOrder(self):
        if not self:
            return []
        
        result = [self.data]
        result.append(self.preOrder())
        result.append(self.preOrder())
        return result

def preOrder(node: Tree):
        if not node:
            return []
        
        result = [node.data]
        result += preOrder(node.left)
        result += preOrder(node.right)
        return result

def inOrder(node: Tree):
        if not node:
            return []
        
        result += inOrder(node.left)
        result = [node.data]
        result += inOrder(node.right)
        return result

def postOrder(node: Tree):
    if not node:
        return []
    
    result += postOrder(node.left)
    result += postOrder(node.right)
    result = [node.data]

test = Tree(1)
a = Tree(2)
b = Tree(3)
c = Tree(4)
test.right = a
a.right = b
b.right = c
a = []
d = preOrder(test)

print(d)