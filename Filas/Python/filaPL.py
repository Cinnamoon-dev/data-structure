class Fila: # index 0 = começo , index n = final
    def __init__(self, dado=None, prox=None) -> None:
        self.dado = dado
        self.prox = prox
    
    def push(self, dado=None): # Entra no final
        if dado is None:
            return
        
        if self.dado is None or self.prox is None:
            self.dado = dado
            return
        
        filaAux = Fila(self.dado, self.prox)
        
        while self.prox is not None:
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        self.prox = Fila(dado, None)

        self.dado = filaAux.dado
        self.prox = filaAux.prox

    def pop(self): # Sai do começo
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

    #Q4
    def firstElementar(self):
        filaAux = Fila(self.dado, self.prox)
        return filaAux.pop()
    
    def firstDiverso(self):
        return self.dado
    
    #Q5
    def isEmptyElementar(self):
        dadoAtual = Fila(self.dado, self.prox)

        if dadoAtual.pop() is None:
            return True
        
        return False
    
    def isEmptyDiverso(self):
        if self.dado is None:
            return True
        
        return False
    
    #Q6
    def lengthElementar(self):
        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while filaAux.dado is not None:
            filaAux.pop()
            counter += 1
        
        return counter
        
    def lengthDiverso(self):
        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while filaAux.dado is not None:
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1
        
        return counter
    
    #Q7
    def lastElementar(self):
        filaAux = Fila(self.dado, self.prox)
        
        while filaAux.prox is not None:
            filaAux.pop()
        
        return filaAux.pop()
    
    def lastDiverso(self):
        filaAux = Fila(self.dado, self.prox)
        
        while filaAux.prox is not None:
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
        
        return filaAux.dado