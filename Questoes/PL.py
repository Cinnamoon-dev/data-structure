#Q4 - Pilha
def peakElementar(self):
    peak = self.pop()
    self.insert(peak)
    
    return peak

def peakDiverso(self):
    return self.dado

#Q4 - Fila
def firstElementar(self):
    filaAux = Fila(self.dado, self.prox)
    return filaAux.pop()

def firstDiverso(self):
    return self.dado

#Q5 - Pilha
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

#Q5 - Fila
def isEmptyElementar(self):
    dadoAtual = Fila(self.dado, self.prox)

    if dadoAtual.pop() is None:
        return True
    
    return False

def isEmptyDiverso(self):
    if self.dado is None:
        return True
    
    return False

#Q6 - Pilha
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

#Q6 - Fila
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

#Q7 - Pilha
def lastElementar(self):
    last = self.pop()
    self.insert(last)
    return last

def lastDiverso(self):
    return self.dado

#Q7 - Fila
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