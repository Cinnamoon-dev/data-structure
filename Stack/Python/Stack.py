import copy

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
    
    def lengthDiverso(self, pilha=None, counter=0):
        if pilha is None or pilha.dado is None:
            return 0
        
        counter += 1
        aux = pilha
        
        return self.lengthDiverso(aux.prox, counter)

    #Q7
    def lastElementar(self):
        pilhaAux = Pilha(self.dado, self.prox)
        
        while pilhaAux.prox is not None:
            pilhaAux.pop()

        return pilhaAux.pop()
    
    def lastDiverso(self):
        pilhaAux = self

        while pilhaAux.prox is not None:
            pilhaAux = pilhaAux.prox

        return pilhaAux.dado
    
    #Q8
    def getValueByIndexElementar(self, index):
        if self.dado is None:
            return None

        pilhaAux = Pilha()
        
        while self.dado is not None:
            pilhaAux.insert(self.pop())

        valueIndex = None
        counter = 0

        while pilhaAux.dado is not None:
            value = pilhaAux.pop()
            
            if counter == index:
                valueIndex = value

            self.insert(value)
            counter += 1
        
        return valueIndex

    def getValueByIndexDiverso(self, index):
        if self.dado is None:
            return None

        pilhaAux = self
        listAux = []

        while pilhaAux is not None:
            listAux.append(pilhaAux.dado)
            pilhaAux = pilhaAux.prox

        listAux.reverse()

        for i, e in enumerate(listAux):
            if i == index:
                return e

        return None
    
    #Q9
    def getIndexByValueElementar(self, value=None):
        if value == None:
            return None
        
        pilhaAux = Pilha()
        
        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        index = None
        counter = 0

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop()) 
            if self.peakElementar() == value:
                index = counter
            counter += 1
        
        return index
    
    def getIndexByValueDiverso(self, value=None):
        if value == None:
            return None
        
        pilhaAux = self
        listAux = []

        while pilhaAux is not None:
            listAux.append(pilhaAux.dado)
            pilhaAux = pilhaAux.prox

        listAux.reverse()

        for i, e in enumerate(listAux):
            if e == value:
                return i
       
        return None

    #Q10
    def getAllIndexByValueElementar(self, value):
        if value == None:
            return []

        pilhaAux = Pilha()
        indexes = []
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
            if self.peakElementar() == value:
                indexes.append(counter)
            counter += 1

        return indexes
    
    def getAllIndexByValueDiverso(self, value):
        if value == None:
            return []

        pilhaAux = self
        indexes = []

        for i in range(self.lengthDiverso() - 1, -1, -1):
            if pilhaAux.dado == value:
                indexes.append(i)
            
            pilhaAux = pilhaAux.prox
        
        return indexes
    
    #Q11
    def getValuesByIndexsElementar(self, indexes=None):
        if indexes is None:
            return []

        pilhaAux = Pilha()
        values = []
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
            if counter in indexes:
                values.append(self.peakElementar())
            counter += 1
        
        return values

    def getValuesByIndexsDiverso(self, indexes=None):
        if indexes is None:
            return []

        pilhaAux = self
        values = []

        for i in range(self.lengthDiverso() - 1, -1, -1):
            if i in indexes:
                values.append(pilhaAux.dado)
            pilhaAux = pilhaAux.prox

        return values

    #Q12
    def getValuesBySliceElementar(self, begin: int, end: int) -> list:
        if not (0 <= begin < self.lengthElementar() and 0 <= end < self.lengthElementar()):
            print("Slice out of range")
            return None

        pilhaAux = Pilha()

        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        counter = 0
        slice = []
        
        while counter != begin:
            self.insert(pilhaAux.pop())
            counter += 1
        
        while counter != (end + 1):
            value = pilhaAux.pop()
            slice.append(value)

            self.insert(value)
            counter += 1
        
        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())

        return slice

    def getValuesBySliceDiverso(self, begin: int, end: int) -> list:
        if not (0 <= begin < self.lengthDiverso() and 0 <= end < self.lengthDiverso()):
            print("Slice out of range")
            return None

        pilhaAux = Pilha()

        while self.dado is not None:
            pilhaAux.insert(self.pop())

        slice = []

        for i in range(0, pilhaAux.lengthDiverso()):
            if begin <= i <= end:
                slice.append(pilhaAux.dado)
            self.insert(pilhaAux.pop())
             
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
        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())

        while pilhaAux.dado is not None:
            if counter == index:
                pilhaAux.pop()
                counter += 1
                continue

            self.insert(pilhaAux.pop())
            counter += 1

    def removeByIndexDiverso(self, index):
        counter = self.lengthDiverso() - 1
        pilhaAux = Pilha()
        
        while self.dado is not None:
            pilhaAux.insert(self.pop())

        for i in range(counter, -1, -1):
            if i == index:
                self.pop()
                break

            pilhaAux.insert(self.pop())
        
        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())

    #Q15
    def removeByValueElementar(self, value=None):
        if value is None or self.dado is None:
            return
        
        pilhaAux = Pilha()

        while self.dado != value and self.dado is not None:
            pilhaAux.insert(self.pop())
        
        self.pop()

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
    
    def removeByValueDiverso(self, value=None):
        if value is None or self.dado is None:
            return None
        
        aux = self

        while aux is not None:
            if aux.dado == value:
                aux.pop()
            aux = aux.prox

    #Q16
    def removeAllByValueElementar(self, value=None):
        if value is None:
            return

        pilhaAux = Pilha()
        while self.dado is not None:
            if self.dado != value:
                pilhaAux.insert(self.pop())
                continue
            self.pop()

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
    
    def removeAllByValueDiverso(self, value=None):
        if value is None:
            return

        pilhaAux = Pilha()
        while self.dado is not None:
            if self.dado != value:
                pilhaAux.insert(self.dado)
                self.dado = self.prox.dado
                self.prox = self.prox.prox
                continue
            self.dado = self.prox.dado
            self.prox = self.prox.prox

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox

    #Q17
    def removeAllByIndexesElementar(self, indexes: list):
        if indexes is None or len(indexes) == 0:
            return
        
        pilhaAux = Pilha()
        counter = 0
        length = self.lengthElementar()

        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        while counter < length:
            if compareEqualsValueWithListOfValues(counter, indexes):
                pilhaAux.pop()
                counter += 1
                continue
            self.insert(pilhaAux.pop())
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
        stackSize = self.lengthElementar()
        if stackSize < (end + 1) or stackSize < (start + 1):
            print("Slice out of range")
            return None

        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        while counter != start: # [1, 2, 3, 4, 5] e (1, 3)
            self.insert(pilhaAux.pop())
            counter += 1
        
        while counter != (end + 1):
            pilhaAux.pop()
            counter += 1
        
        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
    
    def removeAllBySliceDiverso(self, start: int, end: int):
        stackSize = self.lengthDiverso()
        if stackSize < (end + 1) or stackSize < (start + 1):
            print("Slice out of range")
            return None

        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.dado)
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        while counter != start:
            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            counter += 1
        
        while counter != (end + 1):
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            counter += 1
        
        while pilhaAux.dado is not None:
            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox

    #Q19
    def setValueIndexElementar(self, index, value):
        stackSize = self.lengthElementar()
        if index > stackSize:
            print("Index out of bounds")
            return
        
        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        while pilhaAux.dado is not None:
            if counter == index:
                pilhaAux.pop()
                self.insert(value)
                counter += 1
                continue

            self.insert(pilhaAux.pop())
            counter += 1
    
    def setValueIndexDiverso(self, index, value):
        stackSize = self.lengthDiverso()
        if index > stackSize:
            print("Index out of bounds")
            return
        
        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.dado)
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        while pilhaAux.dado is not None:
            if counter == index:
                pilhaAux.dado = pilhaAux.prox.dado
                pilhaAux.prox = pilhaAux.prox.prox
                self.insert(value)
                counter += 1
                continue

            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            counter += 1

    #Q20
    def setValuesInIndexesElementar(self, indexes: list, elements: list):
        stackSize = self.lengthElementar()
        if compareValueWithLessThanListOfValues(stackSize, indexes):
            print("One of the indexes is out of bounds!")
            return

        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.pop())
        
        while pilhaAux.dado is not None:
            if compareEqualsValueWithListOfValues(counter, indexes):
                pilhaAux.pop()
                self.insert(elements[indexes.index(counter)])
                counter += 1
            
            self.insert(pilhaAux.pop())
            counter += 1

    def setValuesInIndexesDiverso(self, indexes: list, elements: list):
        stackSize = self.lengthDiverso()
        if compareValueWithLessThanListOfValues(stackSize, indexes):
            print("One of the indexes is out of bounds!")
            return

        pilhaAux = Pilha()
        counter = 0

        while self.dado is not None:
            pilhaAux.insert(self.dado)
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        while pilhaAux.dado is not None:
            if compareEqualsValueWithListOfValues(counter, indexes):
                pilhaAux.dado = pilhaAux.prox.dado
                pilhaAux.prox = pilhaAux.prox.prox
                self.insert(elements[indexes.index(counter)])
                counter += 1
            
            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
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
    test = Pilha()
    test.initByArray([1, 2, 3, 4, 5])
    test.print()
    print(test.removeByValueDiverso(5))
    test.print()
