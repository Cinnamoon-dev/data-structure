class Fila:
    def __init__(self, dado=None, prox=None) -> None:
        self.dado = dado
        self.prox = prox
    
    def push(self, dado=None):
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

        