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
    def getValueByIndexElementar(self, index):
        if self.dado is None:
            return None

        pilhaAux = Pilha(self.dado, self.prox)
        pilhaAux2 = Pilha()
        counter = 0

        while pilhaAux.dado is not None:
            pilhaAux2.insert(pilhaAux.pop())

        while pilhaAux2.dado is not None:
            value = pilhaAux2.pop()
            if counter == index:
                return value
            counter += 1
        
        return None

    def getValueByIndexDiverso(self, index):
        if self.dado is None:
            return None

        pilhaAux = Pilha(self.dado, self.prox)
        pilhaAux2 = Pilha()
        counter = 0

        while pilhaAux.dado is not None:
            pilhaAux2.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux2.prox = pilhaAux2.prox.prox


        while pilhaAux.dado is not None:
            value = pilhaAux.dado
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox =pilhaAux.prox.prox

            if counter == index:
                return value
            counter += 1
        
        return None
    
    #Q9
    def getIndexByValueElementar(self, value=None):
        if value == None:
            return None
        
        pilhaAux = Pilha(self.dado, self.prox)
        found = False
        counter = 0

        while pilhaAux is not None:
            aux = pilhaAux.pop()
            if aux == value:
                found = True
                break
            counter += 1
        
        if found == True:
            return counter
        
        return None
    
    def getIndexByValueDiverso(self, value=None):
        if value == None:
            return None
        
        pilhaAux = Pilha(self.dado, self.prox)
        found = False
        counter = 0

        while pilhaAux.dado is not None:
            aux = pilhaAux.dado
            if aux == value:
                found = True
                break
            counter += 1

            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.dado = pilhaAux.prox.dado
        
        if found == True:
            return counter
        
        return None

    #Q10
    def getAllIndexByValueElementar(self, value):
        if value == None:
            return []

        pilhaAux = Pilha(self.dado, self.prox)
        indexes = []
        counter = 0

        while pilhaAux.dado is not None:
            aux = pilhaAux.pop()
            if aux == value:
                indexes.append(counter)
            counter += 1
        
        return indexes
    
    def getAllIndexByValueDiverso(self, value):
        if value == None:
            return []

        pilhaAux = Pilha(self.dado, self.prox)
        indexes = []
        counter = 0

        while pilhaAux.dado is not None:
            aux = pilhaAux.dado
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            if aux == value:
                indexes.append(counter)
            counter += 1
        
        return indexes
    
    #Q11
    def getValuesByIndexsElementar(self, indexes=None):
        if indexes is None:
            return []

        pilhaAux = Pilha(self.dado, self.prox)
        values = []
        counter = 0

        while pilhaAux.dado is not None:
            dado = pilhaAux.pop()
            if compareEqualsValueWithListOfValues(counter, indexes):
                values.append(dado)
            counter += 1
        
        return values

    def getValuesByIndexsDiverso(self, indexes=None):
        if indexes is None:
            return []

        pilhaAux = Pilha(self.dado, self.prox)
        values = []
        counter = 0

        while pilhaAux.dado is not None:
            dado = pilhaAux.dado
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            if compareEqualsValueWithListOfValues(counter, indexes):
                values.append(dado)
            counter += 1
        
        return values

    #Q12
    # Considerando o começo como o primeiro elemento que foi colocado na pilha
    def getValuesBySliceElementar(self, begin: int, end: int) -> list: 
        stackSize = self.lengthElementar()
        if stackSize < (end + 1) or stackSize < (begin + 1):
            print("Slice out of range")
            return None

        pilhaAux2 = Pilha(self.dado, self.prox)
        pilhaAux = Pilha()

        while pilhaAux2.dado is not None:
            value = pilhaAux2.pop()
            pilhaAux.insert(value)
        
        counter = 0
        slice = []
        
        while counter != begin:
            pilhaAux.pop()
            counter += 1
        
        while counter != (end + 1):
            value = pilhaAux.pop()
            slice.append(value)
            counter += 1
        
        return slice

    def getValuesBySliceDiverso(self, begin: int, end: int) -> list:
        stackSize = self.lengthElementar()
        if stackSize < (end + 1) or stackSize < (begin + 1):
            print("Slice out of range")
            return None

        pilhaAux2 = Pilha(self.dado, self.prox)
        pilhaAux = Pilha()

        while pilhaAux2.dado is not None:
            value = pilhaAux2.pop()
            pilhaAux.insert(value)

        counter = 0
        slice = []
        
        while counter != begin:
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox - pilhaAux.prox.prox
            counter += 1
        
        while counter != (end + 1):
            value = pilhaAux.dado
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
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
        pilhaAux = Pilha(self.dado, self.prox)
        counter = -1 # Para contar de 0 até n - 1, como indices

        while pilhaAux.dado is not None:
            pilhaAux.pop()
            counter += 1
        
        pilhaAux = Pilha(self.dado, self.prox)
        pilhaAux2 = Pilha()

        while counter != index:
            value = self.pop()
            pilhaAux2.insert(value) 
            counter -= 1
        
        self.pop()

        while pilhaAux2.dado is not None:
            value = pilhaAux2.pop()
            self.insert(value)

    def removeByIndexDiverso(self, index):
        pilhaAux = Pilha(self.dado, self.prox)
        counter = -1 # Para contar de 0 até n - 1, como indices

        while pilhaAux is not None:
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox
            counter += 1
        
        pilhaAux = Pilha(self.dado, self.prox)
        pilhaAux2 = Pilha()

        while counter != index:
            value = self.dado
            self.dado = self.prox.dado
            self.prox = self.prox.prox
            pilhaAux2.insert(value) 
            counter -= 1
        
        self.pop()

        while pilhaAux2.dado is not None:
            value = pilhaAux2.dado
            pilhaAux2.dado = pilhaAux2.prox.dado
            pilhaAux2.prox = pilhaAux2.prox.prox
            self.insert(value)
    #Q15
    def removeByValueElementar(self, value=None):
        if value is None:
            return
        
        pilhaAux = Pilha()

        while self.dado != value and self.dado is not None:
            pilhaAux.insert(self.pop())
        
        self.pop()

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.pop())
    
    def removeByValueDiverso(self, value=None):
        if value is None:
            return
        
        pilhaAux = Pilha()

        while self.dado != value and self.dado is not None:
            pilhaAux.insert(self.dado)
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        
        self.pop()

        while pilhaAux.dado is not None:
            self.insert(pilhaAux.dado)
            pilhaAux.dado = pilhaAux.prox.dado
            pilhaAux.prox = pilhaAux.prox.prox

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


test = Pilha()
test.initByArray([1, 2, 3, 4, 5])
test.print()
test.setValuesInIndexesElementar([0, 4], [10, 20])
test.print()