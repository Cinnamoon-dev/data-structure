class Pilha:
    def __init__(self, dado=None, prox=None):
        self.dado = dado
        self.prox = prox
    
    def initByArray(self, array=None):
        if array is None or len(array) == 0:
            self.dado = None
            self.prox = None
            return
        
        for i in array:
            self.insert(i)
        
    def insert(self, dado=None):
        if dado is None:
            return
        
        if self.dado is None:
            self.dado = dado
            self.prox = None
            return
        
        pilha = Pilha(self.dado, self.prox)
        self.dado = dado
        self.prox = pilha

    def pop(self):
        if self.dado is None:
            return None
        
        if self.prox is None:
            dado = self.dado
            self.dado = None
            return dado

        dado = self.dado
        self.dado = self.prox.dado
        self.prox = self.prox.prox
        return dado

    def pushWithClassLinkedList(self, dado=None):
        if dado is None:
            return
        
        self.insert(dado)

    def pushWithArray(self, array=None):
        if array is None or len(array) == 0:
            return

        for i in array:
            self.insert(i)