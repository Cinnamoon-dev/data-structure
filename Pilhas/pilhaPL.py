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
    
    #Q4
    def peakElementar(self):
        peak = self.pop()
        self.insert(peak)
        
        return peak

    def peakDiverso(self):
        return self.dado
    
    #Q5
    def isEmptyElementar(self):
        dadoAtual = self.pop()

        if dadoAtual is None:
            return True
        
        self.insert(dadoAtual)
        return False
    
    def isEmptyDiverso(self):
        if self.dado is None:
            return True
        
        return False
    
    #Q6
    def lengthElementar(self):
        pilhaAux = Pilha(self.dado, self.prox)
        counter = 0

        while pilhaAux.dado is not None:
            pilhaAux.pop()
            counter += 1
        
        return counter
    
    def lengthDiverso(self):
        pilhaAux = Pilha(self.dado, self.prox)
        counter = 0

        while pilhaAux.dado is not None:
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            counter += 1
        
        return counter

    #Q7
    def lastElementar(self):
        last = self.pop()
        self.insert(last)
        return last
    
    def lastDiverso(self):
        return self.dado
    
    #Q8
    def getValueByIndex(self, value=None):
        if value == None:
            return None
        
        