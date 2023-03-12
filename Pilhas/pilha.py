class Pilha :

    def __init__(self , dado = None, prox = None ):
        self.dado = dado
        self.prox = prox 


    def popular_com_array(self, array_for_insert = None):

        if array_for_insert is None:
            return None

        for value in array_for_insert:
            self.pushWithClassLinkedList(value)


    def pushWithClassLinkedList(self, dado):

        new_pilha = Pilha(self.dado, self.prox)
        self.dado = dado
        self.prox = new_pilha

        return dado

    def pop(self):

        if not self :
            return None

        apagado = self.dado

        if not self.prox:
            self.dado = None
            self.prox = None
        else:
            self.dado = self.prox.dado 
            self.prox = self.prox.prox

        return apagado
    
    def list(self):
        aux = self

        while aux is not None :
            print( aux.dado )
            aux = aux.prox

    # Q4 retorna o primeiro conforme a estrutura 
    def peakElementar(self):
        aux = self.pop()
        self.pushWithClassLinkedList(aux)
        return aux

    # Q4 Generico primeiro conforme a estrutura
    def peakGenerico(self):
        return self.dado
    
    # Q5 Elementar averiguar se esta vazio 
    def isEmptyElementar(self):
        # meu pop só retorna none caso meu self n tenha referencia.
        data_temp = self.pop()
        
        if data_temp is None:
            return True
        
        self.pushWithClassLinkedList(data_temp)
        return False
        
    # Q5 Generico averiguar se esta vazio
    def isEmptyGeneric(self):
        if self.dado is None:
            return True
        
        return False
    
    # Q6 Elementar Return length of my structure
    def tamanhoDaPilhaElementar(self):
        aux = Pilha(self.dado, self.prox)
        counter = 0

        while aux.pop() is not None:
            counter += 1

        return counter
    
    # Q6 Generic Return length of my structure
    def tamanhoDaPilhaGeneric(self):
        aux = self
        counter = 0
        
        while aux.dado is not None:
            counter += 1
            aux = aux.prox

        return counter
    
    # Q7 Elementar Return last element in my scruture
    def lastElementElementar(self):
        aux = self 

        while aux.prox.dado is not None:
            aux = aux.prox
    
        return aux.dado

    # Q7 Generico Return last element in my scruture
    def lastElementGeneric(self):
        aux = Pilha(self.dado, self.prox)

        while aux.tamanhoDaPilhaGeneric() != 1:
            aux.pop()
    
        return aux.dado
    
    # Q8 Elementar Return a determined value in a spcific index
    def getValueByIndexElementar(self, index):
        aux = Pilha(self.dado, self.prox)
        counter = 0
        
        while counter != index:
            counter += 1
            aux = aux.prox
        
        return aux.dado
    
    # Q8 Generic Return a determined value in a spcific index
    def getValueByIndexGeneric(self, index):
        my_values = []
        aux = self

        while aux.prox is not None :
            my_values.append(aux.dado)
            aux = aux.prox

        return my_values[index]
    
    # Q9 Elementar Return the first index that storage a specific value
    def getIndexByValueElementar(self, dado):
        aux = self
        counter = 0

        while aux.dado != dado:

            if aux.prox is None:
                return -1
            
            aux = aux.prox
            counter += 1

        return counter
    
    # Q9 Generic Return the first index that storage a specific value
    def getIndexByValueGeneric(self, dado):
        counter = 0
        aux = self

        while aux.dado != dado:
            counter += 1
            aux = aux.prox

        return counter
    
    # Q10 Elementar Return a array of indexs that storage a specific value
    def getAllIndexByValueElementar(self, dado):
        result = [] # isso n quebra a ideia de ser uma instrução elementar ? 
        aux = self
        counter = 0

        while aux.prox != None:

            if aux.dado == dado:
                result.append(counter)
            
            aux = aux.prox
            counter += 1
        
        return result
    
    # Q10 Generic Return a array of indexs that storage a specific value
    def getAllIndexByValueGenerico(self, dado):
        result = []
        my_newpilha = Pilha(self.dado, self.prox)
        counter = 0

        if self is None:
            return result

        my_dado = my_newpilha.pop()

        while my_dado is not None:
            
            if my_dado == dado:
                result.append(counter)
            
            my_dado = my_newpilha.pop()
            counter += 1

        return result

    # Q11 Elementar return a array of values in per a array of index
    def getValuesByIndexsElementar(self, indexs):
        result = []
        # posso usar outras funções ? 

        for index in indexs:
            # complexity is n² 
            aux = self
            counter = 0

            while counter != index:
                aux = aux.prox
                counter += 1

            result.append(aux.dado)

        return result
    
    # Q11 Generic return a array of values in per a array of index
    def getValuesByIndexsGenerico(self, indexs):
        aux = self
        result = []

        for index in indexs:
            data = aux.getValueByIndexGeneric(index)
            result.append(data)
        
        return result
    
    # Q12 Elementar return a array sliced of my array
    def getValuesBySliceElementar(self, start, end):
        counter = 0
        aux = self
        result = []

        while counter != end :

            if counter >= start:
                result.append(aux.dado)

            counter += 1
            aux = aux.prox

        return result
    
    # Q12 Generic return a array sliced of my array
    def getValuesBySliceGeneric(self, start, end):
        result = []

        for index in range(start, end):
            result.append(self.getValueByIndexElementar(index))

        return result
    
    # Q13 Elementar Remove All values of my stack 
    def removeAllElementar(self):
        aux = self

        while aux.pop() is not None:
            continue 
    
        return self

    # Q13 Elementar Remove All values of my stack # POSSIBLE ANSWER !!
    def removeAllGeneric(self):
        self.dado = None
        self.prox = None

        return self
    
    # Q14 Elementar Remove a specific value in a determinate index
    def removeByIndexElementar(self ,index):
        aux = self
        counter = 0

        while counter != index:
            aux = aux.prox
            counter += 1

        last_data_storaged = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return last_data_storaged
    
    # Q14 Generic Remove a specific value in a determinate index
    def removeByIndexGenerico(self ,index):
        
        aux = self
        dado_for_remove = self.getValueByIndexGeneric(index)

        while aux.dado != dado_for_remove:
            aux = aux.prox

        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox
        
        return dado_for_remove
    
    # Q15 Generic Remove the first data that has equal dado value 
    def removeFirstElementByValueElementar(self, dado):
        aux = self

        while aux.dado != dado:
            aux = aux.prox
        
        # remove o primeiro elemento que ele encontrar
        removed_element = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return removed_element
    
    # Q15 Generic Remove the first data that has equal dado value        
    def removeFirstElementByValueGenerico(self,dado):

        aux = self
        index_for_remove = aux.getAllIndexByValueElementar(dado)[0] # take the first element for remove 
        counter = 0 

        while counter != index_for_remove:
            aux = aux.prox
            counter += 1

        removed_element = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return removed_element

    # Q16 Elementar Remove all datas with a specific value
    def removeAllByValueElementar(self, value):
        aux = self 

        while aux.dado is not None:
            
            if aux.dado == value:
                aux.pop()
                continue

            aux = aux.prox

        return True
    
    # Q16 Generic Remove all datas with a specific value
    def removeAllByValueGeneric(self, value):
        qtd_itens = self.tamanhoDaPilhaElementar()
        counter = 0

        while counter != qtd_itens: 

            index_to_remove = self.getIndexByValueElementar(value) 

            if index_to_remove == -1:
                return True
            
            self.removeByIndexElementar(index_to_remove)
            counter += 1 

        return True
    
    # Q17 Elementar Remove all datas with a specific index
    def removeAllByIndexesElementar(self, indexs):
        
        aux = self 
        counter  = 0

        for index in indexs:
            
            while index != counter:
                aux = aux.prox 
                counter += 1   

            aux.pop()
            counter = 0
            aux = self 

        return True
    
    # Q17 Generico Remove all datas with a specific index
    def removeAllByIndexesGeneric(self, indexs):

        for index in indexs:
            self.removeByIndexElementar(index)

        return True
    
    # Q18 Elementar Remove all datas starting in start and close in end
    def removeAllBySlice(self, start, end):
        counter = 0
        aux = self

        while counter != end :

            if counter >= start:
                aux.pop()

            counter += 1
            aux = aux.prox

        return True

    # Q18 Generic Remove all datas starting in start and close in end
    def removeAllBySlice(self, start, end):

        for index in range(start, end):
            self.removeByIndexElementar(self.getValueByIndexElementar(index))

        return True
    
    # Q19 Elementar Assignment a value for a specific index
    def setValueInIndexElementar(self, index:int, value:str) -> bool:

        aux = self
        counter = 0

        while counter != index:
            counter += 1
            aux = aux.prox

        
        aux.dado = value
        
        return True

    # Q19 Generic Assignment a value for a specific index
    def setValueInIndexGeneric(self, index, value):
        aux = self
    
        for index in range(index):
            aux = aux.prox 

        aux.dado = value
        return True

    # Q20 Elementar Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesElementar(self ,indexs, elements):
        aux = self
        counter_one = 0
        counter_two = 0

        limite_loops = len(indexs)

        while counter_two < limite_loops:
            counter_two += 1

            while counter_one != indexs[counter_two - 1]:
                aux = aux.prox 
                counter_one += 1 

            aux.dado = elements[counter_one]
            counter_one = 0

        return True
    
    # Q20 Generico Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesGenerico(self ,indexs, elements):
        counter_one = 0

        for index in indexs:
            self.setValueInIndexGeneric(index,elements[counter_one])
            counter_one += 1

        return True
