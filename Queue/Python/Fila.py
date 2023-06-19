class Fila:
    
    def __init__(self, dado = None, prox = None ):

        self.dado = dado
        self.prox = prox

    def insertWithArray( self , array ):
        
        for element in array:
            self.pushWithClassLinkedList( element )

        return True

    def pushWithClassLinkedList(self, dado):

        if dado is None:
            return None 
        
        # logica para a fila sem dados
        if self.dado is None:
            self.dado = dado
            self.prox = None
            return dado
        
        # lógica para a fila com dados  
        aux = self

        while aux.prox is not None:
            aux = aux.prox

        new_celula = Fila(dado)
        aux.prox = new_celula

        return dado

    def list( self ):

        if self.dado is None:
            return None 

        aux = self

        while aux.prox is None:
            print( aux.dado )
            aux = aux.prox

        return None
    
    def popWithClassLinkedList(self):
        # first In first Out 
        if self.dado is None:
            return None

        deleted = self.dado 

        if self.prox is not None:
            self.dado = self.prox.dado
            self.prox = self.prox.prox
        else:
            self.dado = None
            self.prox = None
        
        return deleted
    
    def create_aux_queue( self ):
        
        new_queue = Fila()
        aux_queue = Fila()
        # criando uma fila auxiliar para o retorno
        while True:
            data_temp =  self.pop()

            if data_temp is None:
                break

            new_queue.pushWithClassLinkedList(data_temp)
            aux_queue.pushWithClassLinkedList(data_temp)

        # recolocando todos os elementos na fila principal
        while True:
            data_temp = aux_queue.pop()

            if data_temp is None:
                break
            
            self.pushWithClassLinkedList(dado=data_temp)

        # ordem dos elementos é mantida.
        return new_queue

    # Q4 return the first element of my data structure
    def peekElementar(self):
        aux_queue = self.create_aux_queue()
        return aux_queue.popWithClassLinkedList()
    
    # Q4 return the first element of my data structure
    def peekGeneric( self ):
        return self.dado

    # Q5 return true if my queue is empty 
    def isEmptyElementar(self):
        new_queue = self.create_aux_queue()
        return True if new_queue.popWithClassLinkedList() is None else False
    
    # Q5 return true if my queue is empty 
    def isEmptyGeneric(self):
        return True if self.dado is None else False
    
    # Q6 returns the quantify of elements in my queue
    def lenElementar(self):
        
        quantidade = 0
        new_queue = self.create_aux_queue()
        
        while True:

            quantidade += 1
            if new_queue.prox is None:
                break
            
            new_queue = new_queue.prox

        return quantidade
    
    # Q6 returns the quantify of elements in my queue
    def lenGeneric(self):
        
        quantidade = 0
        aux_pointer = Fila(self.dado, self.prox)

        while aux_pointer.prox is not None:
            quantidade += 1
            aux_pointer = aux_pointer.prox

        return quantidade
    
    # Q7 returns the last item in my structure 
    def lastElementar(self):
        
        new_queue = self.create_aux_queue()
        
        while True:
            data_temp = new_queue.popWithClassLinkedList()
            
            if data_temp is None:
                break

            data = data_temp
        
        return data
        
    # Q7 return the last item in my structure 
    def lastGeneric(self):
        aux_pointer = Fila(self.dado, self.prox)
        tamanho_fila = self.lenGeneric()
        
        # por padrão ja retorna tamanho - 1, eu subtraio - 1 para sobrar apenas 1 node 
        for index in range( 0, tamanho_fila - 1 ):
            last_item = aux_pointer.popWithClassLinkedList()
    
        return last_item
    
    # Q8 return a value in a specific index 
    def getValueByIndexElementar( self, index ):

        counter = 0 
        data_temp = ''
        aux_queue = self.create_aux_queue()

        while data_temp is not None:
            
            if counter == index:
                return data_temp
            
            counter += 1 
            data_temp = aux_queue.pop()

        return -1 # dont find
    
    # Q8
    def getValueByIndexGeneric(self, index):
        
        aux_pointer = Fila(self.dado, self.prox)
        length_queue = aux_pointer.lenElementar()
        element = aux_pointer.popWithClassLinkedList()
        
        if index + 1 > length_queue:
            return -1 # don't find 

        for ind in range(0, index):
            aux_pointer = aux_pointer.prox

        return aux_pointer.dado

    # Q9 return the first index of a value in my struct
    def getIndexByValueElementar(self, value):

        counter = 0
        data_temp = ''
        new_queue = self.create_aux_queue()

        while data_temp is not None:

            if value == data_temp:
                return counter
            
            counter += 1
            data_temp = new_queue.pop()

        return -1 # don't find
    
    # Q9 return the first index of a value in my struct
    def getIndexByValueGeneric( self, value ):
        
        index = 0
        aux_pointer = Fila(self.dado, self.prox)
        item = aux_pointer.popWithClassLinkedList()

        while item != value and item is not None:
            index += 1
            item = aux_pointer.popWithClassLinkedList()

        return index if item == value else -1
    
    # Q10 return a array of index of a item value
    def getAllIndexByValueElementar(self,value):

        index = 0
        indexs = []
        aux_queue = self.create_aux_queue()

        while aux_queue is not None:

            if data_temp == value:
                indexs.append(index)
            
            index += 1
            data_temp = aux_queue.pop()

        return indexs
    
    # Q10 return a array of index of a item value
    def getAllIndexByValueGeneric(self,value):
        
        indexs = []
        aux_pointer = Fila(self.dado, self.prox)

        for index in range(0, aux_pointer.lenElementar()):

            if aux_pointer.dado == value:
                indexs.append(index)
            
            aux_pointer = aux_pointer.prox

        return indexs
    
    # Q11 return values in a specifics indexs
    def getValuesByIndexsElementar( self, indexs ):

        # vou ter que andar tanto em indexs quanto na minha fila de dados.

        index_j = 0
        values = []
        aux_one = self.create_aux_queue()

        for index_i in indexs:    
        
            index_j = 0
            aux_two = self.create_aux_queue()

            while aux_two is not None:
                
                if index_j == indexs[index_i]:
                    values.append(data_temp)
                    break

                index_j += 1
                data_temp = aux_two.popWithClassLinkedList()

            aux_one.popWithClassLinkedList()

        return values
    
    # Q11 return values in a specifics indexs
    def getValuesByIndexsGenerics(self, indexs):

        values = []
        index_j = 0
        length_indexs = len(indexs)
        length_datas = self.lenElementar()
        
        for index_i in range(0, length_indexs):
            aux = self

            for index_j in range(0,length_datas):
            
                if index_j == indexs[index_i]:
                    values.append(aux.dado)

                aux = aux.prox

        return values
    
    # Q12 get values in a slice of my array
    def getValuesBySliceElementar(self, start, end):

        if self.dado is None:
            return []

        aux = self
        counter = 0
        values = []

        while aux is not None:
            
            if counter >= start and counter < end:
                values.append(aux.dado)
            
            counter += 1
            aux = aux.prox

        return values
    
    # Q13 get values in a slice of my array
    def getValuesBySliceGeneric(self,start,end):

        aux = self
        values = []
        
        for index in range(start,end):
            values.append(aux.getValueByIndexGeneric(index))

        return values
            
    # Q14 remove all elements 
    def removeAllElementar(self):
        
        while self.dado is not None:
            self.popWithClassLinkedList()

        return self
    
    # Q14 
    def removeAllGeneric(self):
        self.dado = None
        self.prox = None
        return self
    
    # Q15 remove the first element that has value x 
    def removeByValueElementar(self, value):

        if self.dado is None:
            return None

        aux = self 

        while aux is not None:
            
            if aux.dado == value:
                aux.popWithClassLinkedList()
                return True
        
            aux = aux.prox 
        
        return False # dont find
    
    # Q15 
    def removeByValueGeneric(self, value):
        
        if self.dado is None:
            return None
        
        index_of_my_value = self.getIndexByValueElementar(value)

        if index_of_my_value < 0:
            return "index not valid"

        aux = self
        for index in range(self.getIndexByValueElementar(value)):
            aux = aux.prox

        aux.popWithClassLinkedList()

        return True
    
    # Q16 remove all elements by value
    def removeAllByValueElementar(self, value):
        
        if self.dado is None:
            return False

        aux = self

        while aux is not None:
            
            if aux.dado == value:
                aux.popWithClassLinkedList()
                continue

            aux = aux.prox
        
        return True
    
    # Q16 
    def removeAllByValueGeneric(self, value):
        
        if self.dado is None:
            return False
        
        aux = self
        counter = 0
        fila_legth = aux.lenElementar()

        for index in range(fila_legth):

            if value == aux.dado:
                aux.popWithClassLinkedList()
                counter += 1
                continue

            counter += 1
            aux = aux.prox

        return True
    
    # Q17 remove all by indexs 
    def removeAllByIndexesElementar(self , indexs):
        
        if self.dado is None:
            return False

        aux_one = self 
        aux_two = self
        index_i = 0
        index_j = 0 

        while aux_one is not None:    
        
            index_j = 0
            aux_two = self

            while aux_two is not None:
                
                try:
                    if index_j == indexs[index_i]:
                        aux_two.popWithClassLinkedList()
                        break
                except:

                    break

                index_j += 1
                aux_two = aux_two.prox

            index_i += 1
            aux_one = aux_one.prox
        
        return True
    
    # Q17 
    def removeAllByIndexesGeneric(self, indexs):
        
        # takes all values 
        values_in_indexs = self.getValuesByIndexsElementar(indexs)
        legth_queue = self.lenElementar()
        aux = self

        for value in values_in_indexs:
            for index in range(legth_queue):
                
                if aux.dado == value:
                    aux.popWithClassLinkedList()
                    continue
            
            aux = aux.prox


        return True

    # Q18 remove all by slice
    def removeAllBySliceElementar(self, start, end):
        
        if self.dado is None:
            return False
        
        aux = self 
        counter = 0

        while aux is not None:

            if counter >= start and counter < end:
                aux.popWithClassLinkedList()
                counter += 1
                continue

            counter += 1
            aux = aux.prox
        
        return True
    
    # Q19
    def removeAllBySliceGeneric(self, start, end):
        
        if self.dado is None and start > end:
            return False
        
        if end > self.lenGeneric():
            end = self.lenElementar()

        aux = self
        for index in range( end ):
            
            if index >= start:
                aux.popWithClassLinkedList()
                continue

            aux = aux.prox

        return True
    
    # Q19 set a value in a specific index
    def setValueInIndexElementar(self, index, value):

        if self.dado is None:
            return False
        
        aux = self
        counter = 0
        while aux is not None:
            
            if index == counter:
                aux.dado = value
                break

            counter += 1
            aux = aux.prox

        return True
    
    # Q19 
    def setValueInIndexGeneric(self, index, value):
        
        if self.dado is None and self.getIndexByValueElementar(value) == -1:
            return False

        aux = self
        counter = 0 
        
        while counter != index - 1:
            counter += 1
            aux = aux.prox

        aux.dado = value

        return True
    
    # Q20 set a value in a specific index of a indexs array 
    def setValuesInIndexesElementar(self, indexs, elements):

        # considerar array of indexs and array of elements has same legth

        if self.dado is None:
            return False
        
        aux_one = self 
        aux_two = self
        index_i = 0
        index_j = 0 

        while aux_one is not None:    
        
            index_j = 0
            aux_two = self

            while aux_two is not None:
                
                try:
                    if index_j == indexs[index_i]:
                        aux_two.dado = elements[index_i]
                        break
                except:
                    break

                index_j += 1
                aux_two = aux_two.prox

            index_i += 1
            aux_one = aux_one.prox
        
        return True
    
    # Q20 
    def setValuesInIndexesGeneric(self, indexs, elements):
        
        if self.dado is None:
            return False
        
        length_indexs = len(indexs) # is the length of elements too 
        length_datas = self.lenElementar()
        
        for index_i in range(length_indexs): # andando em indexs
            aux = self 
            
            for index_j in range(length_datas):

                if index_j == indexs[index_i]:
                    aux.dado = elements[index_i]
                    break
            
                aux = aux.prox

        return True 