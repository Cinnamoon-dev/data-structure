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
            return counter
        
        counter += 1
        aux = pilha
        
        return self.lengthDiverso(aux.prox, counter)
    
    #Q7
    def lastElementar(self):
        filaAux = Fila(self.dado, self.prox)
        
        while filaAux.prox is not None:
            filaAux.pop()
        
        return filaAux.pop()
    
    def lastDiverso(self, fila=None):
        if fila.prox is None:
            return fila.dado
        
        aux = fila
        dado = self.lastDiverso(aux.prox)

        return dado

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
            if filaAux.pop() == value:
                indexes.append(counter)
            counter += 1
        
        return indexes
    
    def getAllIndexByValueDiverso(self, value):
        if value == None:
            return []

        filaAux = Fila(self.dado, self.prox)
        indexes = []

        for i in range(0, filaAux.lengthDiverso()):
            if filaAux.dado == value:
                indexes.append(i)
            filaAux = filaAux.prox
        
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
            if counter in indexes:
                values.append(dado)
            counter += 1
        
        return values

    def getValuesByIndexsDiverso(self, indexes=None):
        if indexes is None:
            return []

        filaAux = self
        values = []

        for i in range(0, filaAux.lengthDiverso()):
            if i in indexes:
                values.append(filaAux.dado)
            filaAux = filaAux.prox
        
        return values
    
    #Q12
    def getValuesBySliceElementar(self, begin: int, end: int) -> list: 
        if not (0 <= begin < self.lengthElementar() and 0 <= end < self.lengthElementar()):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)     
        counter = 0
        slice = []
        
        while counter != begin:
            filaAux.pop()
            counter += 1
        
        while counter != (end + 1):
            slice.append(filaAux.pop())
            counter += 1
        
        return slice

    def getValuesBySliceDiverso(self, begin: int, end: int) -> list:
        if not (0 <= begin < self.lengthDiverso() and 0 <= end < self.lengthDiverso()):
            print("Slice out of range")
            return None

        filaAux = self
        slice = []
        
        for i in range(0, filaAux.lengthDiverso()):
            if begin <= i <= end:
                slice.append(filaAux.dado)
            filaAux = filaAux.prox
        
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
        filaAux = Fila()
        counter = 0

        while self.dado is not None:
            if counter == index:
                self.pop()
                counter += 1
                continue
            
            self.insert(filaAux.pop())
            counter += 1
        
        while filaAux.dado is not None:
            self.insert(filaAux.pop())

    def removeByIndexDiverso(self, index):
        arrayAux = []
        
        while self.dado is not None:
            arrayAux.append(self.pop())
        
        arrayAux.pop(index)
        self.pushWithArray(arrayAux)

    #Q15
    def removeByValueElementar(self, value=None):
        if value is None or self.dado is None:
            return
        
        filaAux = Fila()

        while self.dado != value and self.dado is not None:
            filaAux.push(self.pop())
        
        self.pop()

        while filaAux.dado is not None:
            self.push(filaAux.pop())
    
    def removeByValueDiverso(self, value=None):
        if value is None or self.dado is None:
            return None
        
        aux = self
        counter = self.lengthDiverso - 1

        for i in range(counter, -1, -1):
            if aux.dado == value:
                aux.pop()
                return

            aux = aux.prox
    
    #Q16
    def removeAllByValueElementar(self, value=None):
        if value is None or self.dado is None:
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

        aux = self
        counter = self.lengthElementar() - 1

        for i in range(counter, -1, -1):
            if aux.dado == value:
                aux.pop()
                continue

            aux = aux.prox

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
            if counter in indexes:
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
        if not (0 <= start < self.lengthElementar() and 0 <= end < self.lengthElementar()):
            print("Slice out of range")
            return None

        filaAux = Fila(self.dado, self.prox)
        counter = 0

        while self.dado is not None:
            self.pop()
        
        while counter != start:
            self.push(filaAux.pop())
            counter += 1
        
        while counter != (end + 1):
            filaAux.pop()
            counter += 1
        
        while filaAux.dado is not None:
            self.push(filaAux.pop())
    
    def removeAllBySliceDiverso(self, start: int, end: int):
        if not (0 <= start < self.lengthElementar() and 0 <= end < self.lengthElementar()):
            print("Slice out of range")
            return None

        filaAux = Fila()
        listAux = []

        while self.dado is not None:
            filaAux.push(self.pop())
        
        while filaAux.dado is not None:
            dado = filaAux.pop()
            listAux.append(dado)
        
        for i, e in enumerate(listAux):
            if start <= i <= end:
                continue

            self.push(e)

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
    print(test.removeAllBySliceDiverso(2, 3))
    test.print()
