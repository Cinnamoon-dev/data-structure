class Fila: # index 0 = começo , index n = final
    def __init__(self, dado=None, prox=None) -> None:
        self.dado = dado
        self.prox = prox
    
    def push(self, dado=None):
        if dado is None:
            return
        
        if self.dado is None:
            self.dado = dado
            self.prox = None
            return

        f = Fila(dado, None)

        filaAux = self #copia
        while filaAux.prox is not None:
            filaAux = filaAux.prox

        filaAux.prox = f

    def pushWithArray(self, array=None):
        if array is None or len(array) == 0:
            return
        
        for i in array:
            self.push(i)

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

    def print(self):
        array = self.toArray([])
        print(array)

    def toArray(self, array=[]):
        if self is None:
            return

        array.append(self.dado)

        if self.prox is not None and self.prox.dado is not None:
            self.prox.toArray(array)

        return array

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
        
    def lengthDiverso(self, pilha=None, counter=0):
        if pilha is None or pilha.dado is None:
            return 0
        
        counter += 1
        aux = pilha
        
        return self.lengthDiverso(aux.prox, counter)
    
    #Q7
    def lastElementar(self):
        filaAux = Fila(self.dado, self.prox)
        
        while filaAux.prox is not None:
            filaAux.pop()
        
        return filaAux.pop()
    
    def lastDiverso(self):
        filaAux = self
        
        while filaAux.prox is not None:
            filaAux = filaAux.prox
        
        return filaAux.dado

    #Q8
    def getValueByIndexElementar(self, index):
        if self.dado is None:
            return None
        
        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while filaAux.dado is not None:
            value = filaAux.pop()
            if counter == index:
                return value
            counter += 1
        
        return None
    
    def getValueByIndexDiverso(self, index):
        if self.dado is None:
            return None
        
        filaAux = self
        listAux = []
        
        while filaAux is not None:
            listAux.append(filaAux.dado)
            filaAux = filaAux.prox
        
        for i,e in enumerate(listAux):
            if i == index:
                return e
        
        return None
    
    #Q9
    def getIndexByValueElementar(self, value=None):
        if value == None:
            return None

        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while filaAux.dado is not None:
            if filaAux.pop() == value:
                return counter
            counter += 1

        return None
    
    def getIndexByValueDiverso(self, value=None):
        if value == None:
            return None

        filaAux = self
        listAux = []

        while filaAux is not None:
            listAux.append(filaAux.dado)
            filaAux = filaAux.prox

        for i, e in enumerate(listAux):
            if e == value:
                return i

        return None
    
    #Q10
    def getAllIndexByValueElementar(self, value):
        if value == None:
            return []

        filaAux = Fila(self.dado, self.prox)
        indexes = []
        counter = 0

        while filaAux.dado is not None:
            aux = filaAux.pop()
            if aux == value:
                indexes.append(counter)
            counter += 1
        
        return indexes
    
    def getAllIndexByValueDiverso(self, value):
        if value == None:
            return []

        filaAux = Fila(self.dado, self.prox)
        indexes = []
        counter = 0

        while filaAux.dado is not None:
            aux = filaAux.dado
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            if aux == value:
                indexes.append(counter)
            counter += 1
        
        return indexes

    #Q11
    def getValuesByIndexsElementar(self, indexes=None):
        if indexes is None:
            return []

        filaAux = Fila(self.dado, self.prox)
        values = []
        counter = 0

        while filaAux.dado is not None:
            dado = filaAux.pop()
            if compareEqualsValueWithListOfValues(counter, indexes):
                values.append(dado)
            counter += 1
        
        return values

    def getValuesByIndexsDiverso(self, indexes=None):
        if indexes is None:
            return []

        filaAux = Fila(self.dado, self.prox)
        values = []
        counter = 0

        while filaAux.dado is not None:
            dado = filaAux.dado
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            if compareEqualsValueWithListOfValues(counter, indexes):
                values.append(dado)
            counter += 1
        
        return values
    
    #Q12
    def getValuesBySliceElementar(self, begin: int, end: int) -> list: 
        queueSize = self.lengthElementar()
        if queueSize < (end + 1) or queueSize < (begin + 1):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)     
        counter = 0
        slice = []
        
        while counter != begin:
            filaAux.pop()
            counter += 1
        
        while counter != (end + 1):
            value = filaAux.pop()
            slice.append(value)
            counter += 1
        
        return slice

    def getValuesBySliceDiverso(self, begin: int, end: int) -> list:
        queueSize = self.lengthElementar
        if queueSize < (end + 1) or queueSize < (begin + 1):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)
        counter = 0
        slice = []
        
        while counter != begin:
            filaAux.dado = filaAux.prox.dado
            filaAux.prox - filaAux.prox.prox
            counter += 1
        
        while counter != (end + 1):
            value = filaAux.dado
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            slice.append(value)
            counter += 1
        
        return slice
    
    #Q13
    def removeAllElementar(self):
        while self.dado is not None:
            self.pop()
    
    def removeAllDiverso(self):
        self.dado = None
        self.prox = None
    
    #Q14
    def removeByIndexElementar(self, index):
        filaAux = Fila(self.dado, self.prox)
        counter = -1 # Para contar de 0 até n - 1, como indices

        while filaAux.dado is not None:
            filaAux.pop()
            counter += 1
        
        filaAux = Fila(self.dado, self.prox)
        filaAux2 = Fila()

        while counter != index:
            value = self.pop()
            filaAux2.push(value) 
            counter -= 1
        
        self.pop()

        while filaAux2.dado is not None:
            value = filaAux2.pop()
            self.push(value)

    def removeByIndexDiverso(self, index):
        filaAux = Fila(self.dado, self.prox)
        counter = -1 # Para contar de 0 até n - 1, como indices

        while filaAux is not None:
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1
        
        filaAux = Fila(self.dado, self.prox)
        filaAux2 = Fila()

        while counter != index:
            value = self.dado
            self.dado = self.prox.dado
            self.prox = self.prox.prox
            filaAux2.push(value) 
            counter -= 1
        
        self.pop()

        while filaAux2.dado is not None:
            value = filaAux2.dado
            filaAux2.dado = filaAux2.prox.dado
            filaAux2.prox = filaAux2.prox.prox
            self.push(value)

    #Q15
    def removeByValueElementar(self, value=None):
        if value is None:
            return
        
        filaAux = Fila()

        while self.dado != value and self.dado is not None:
            filaAux.push(self.pop())
        
        self.pop()

        while filaAux.dado is not None:
            self.push(filaAux.pop())
    
    def removeByValueDiverso(self, value=None):
        if value is None:
            return
        
        filaAux = Fila()

        while self.dado != value and self.dado is not None:
            filaAux.push(self.dado)
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        self.pop()

        while filaAux.dado is not None:
            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
    
    #Q16
    def removeAllByValueElementar(self, value=None):
        if value is None:
            return

        filaAux = Fila()
        while self.dado is not None:
            if self.dado != value:
                filaAux.push(self.pop())
                continue
            self.pop()

        while filaAux.dado is not None:
            self.push(filaAux.pop())
    
    def removeAllByValueDiverso(self, value=None):
        if value is None:
            return

        filaAux = Fila()
        while self.dado is not None:
            if self.dado != value:
                filaAux.push(self.dado)
                self.dado = self.prox.dado
                self.prox = self.prox.prox
                continue
            self.dado = self.prox.dado
            self.prox = self.prox.prox

        while filaAux.dado is not None:
            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox

    #Q17
    def removeAllByIndexesElementar(self, indexes: list):
        if indexes is None or len(indexes) == 0:
            return
        
        filaAux = Fila()
        counter = 0
        length = self.lengthElementar()

        while self.dado is not None:
            filaAux.push(self.pop())
        
        while counter < length:
            if compareEqualsValueWithListOfValues(counter, indexes):
                filaAux.pop()
                counter += 1
                continue
            self.push(filaAux.pop())
            counter += 1

    def removeAllByIndexesDiverso(self, indexes: list):
        if indexes is None or len(indexes) == 0:
            return
        
        values= []

        for index in indexes:
            values.append(self.getValueByIndexElementar(index))
        
        for value in values:
            self.removeByValueElementar(value)

    #Q18
    def removeAllBySliceElementar(self, start: int, end: int):
        queueSize = self.lengthElementar()
        if queueSize < (end + 1) or queueSize < (start + 1):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.pop()
        
        while counter != start: # [1, 2, 3, 4, 5] e (1, 3)
            self.push(filaAux.pop())
            counter += 1
        
        while counter != (end + 1):
            filaAux.pop()
            counter += 1
        
        while filaAux.dado is not None:
            self.push(filaAux.pop())
    
    def removeAllBySliceDiverso(self, start: int, end: int):
        queueSize = self.lengthDiverso()
        if queueSize < (end + 1) or queueSize < (start + 1):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)
        counter = 0
        
        while self.dado is not None:
            self.pop()

        while counter != start: 
            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1
        
        while counter != (end + 1):
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1
        
        while filaAux.dado is not None:
            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox

    #Q19
    def setValueIndexElementar(self, index, value):
        queueSize = self.lengthElementar()
        if index > queueSize:
            print("Index out of bounds")
            return
        
        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.pop()
        
        while filaAux.dado is not None:
            if counter == index:
                filaAux.pop()
                self.push(value)
                counter += 1
                continue

            self.push(filaAux.pop())
            counter += 1
    
    def setValueIndexDiverso(self, index, value):
        queueSize = self.lengthDiverso()
        if index > queueSize:
            print("Index out of bounds")
            return
        
        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.pop()

        while filaAux.dado is not None:
            if counter == index:
                filaAux.dado = filaAux.prox.dado
                filaAux.prox = filaAux.prox.prox
                self.push(value)
                counter += 1
                continue

            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1

    #Q20
    def setValuesInIndexesElementar(self, indexes: list, elements: list):
        queueSize = self.lengthElementar()
        if compareValueWithLessThanListOfValues(queueSize, indexes):
            print("One of the indexes is out of bounds!")
            return

        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.pop()
        
        while filaAux.dado is not None:
            if compareEqualsValueWithListOfValues(counter, indexes):
                filaAux.pop()
                self.push(elements[indexes.index(counter)])
                counter += 1
            
            self.push(filaAux.pop())
            counter += 1

    def setValuesInIndexesDiverso(self, indexes: list, elements: list):
        queueSize = self.lengthDiverso()
        if compareValueWithLessThanListOfValues(queueSize, indexes):
            print("One of the indexes is out of bounds!")
            return

        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        while filaAux.dado is not None:
            if compareEqualsValueWithListOfValues(counter, indexes):
                filaAux.dado = filaAux.prox.dado
                filaAux.prox = filaAux.prox.prox
                self.push(elements[indexes.index(counter)])
                counter += 1
            
            self.push(filaAux.dado)
            filaAux.dado = filaAux.prox.dado
            filaAux.prox = filaAux.prox.prox
            counter += 1

# Auxiliary Functions
def compareEqualsValueWithListOfValues(value, listOfValues: list):
    for index in listOfValues:
        if value == index:
            return True
    
    return False

def compareValueWithLessThanListOfValues(value, listOfValues: list):
    for index in listOfValues:
        if value < index:
            return True
    
    return False



if __name__ == "__main__":
    test = Fila()
    test.pushWithArray([1, 2, 3, 4, 5])
    test.print()
    print(test.getIndexByValueDiverso(3))
