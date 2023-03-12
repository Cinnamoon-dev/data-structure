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

        while aux.dado is not None :
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


    # Q13 Elementar Remove All values of my stack # POSSIBLE ANSWER !!
    def removeAllFunny(self):
        self.dado = None
        self.prox = None

        return self
    
    # Q13 Elementar Remove All values of my stack 
    def removeAllElementar(self):
        aux = self

        while aux.pop() is not None:
            continue 
    
        return self

     # Q13 Generic Remove All values of my stack 
    def removeAllGeneric(self):
        aux = self
        new_pointer = None

        while aux.dado is not None:
            new_pointer = aux.prox
            del(aux)
            aux = new_pointer
    
        return self


my_pilha = Pilha('Pen', None)
my_pilha.pop()

my_pilha.pushWithClassLinkedList('Ola')
my_pilha.pushWithClassLinkedList('Mundo')
my_pilha.pushWithClassLinkedList('Cruel')
my_pilha.pushWithClassLinkedList('Pedro')
my_pilha.pushWithClassLinkedList('hey')
my_pilha.pushWithClassLinkedList('teste')
my_pilha.pushWithClassLinkedList('teste')
my_pilha.pushWithClassLinkedList('teste')

print("Esta Vazio ? >>" + str(my_pilha.isEmptyElementar()))
print(" Elementar First Element >>" + my_pilha.peakElementar())
print("Tamanho da minha estrutura Elementar>>" + str(my_pilha.tamanhoDaPilhaElementar()))
print("Tamanho da minha estrutura Generico>>" + str(my_pilha.tamanhoDaPilhaGeneric()))
print("Ultimo elemento da minha estrutura elementar >>" + str(my_pilha.lastElementElementar()))
print("Ultimo elemento da minha estrutura generico >>" + str(my_pilha.lastElementGeneric()))
print("Fazendo um get elementar no indice 2 >>" + str(my_pilha.getValueByIndexElementar(2)))
print("Fazendo um get generic no indice 2 >>" + str(my_pilha.getValueByIndexGeneric(2)))
print("Fazendo uma pesquisa elementar na pilha por Ola>>" + str(my_pilha.getIndexByValueElementar("Ola")))
print("Fazendo uma pesquisa generica na pilha por Ola>>" + str(my_pilha.getIndexByValueGeneric("Ola")))
print("Fazendo uma pesquisa dos indices de Pedro elementar na pilha>>" + str(my_pilha.getIndexByValueGeneric("Pedro")))
print("Fazendo uma pesquisa em todos os  indices por teste elementar>> " + str(my_pilha.getAllIndexByValueElementar("teste")))
print("Fazendo uma pesquisa em todos os  indices por teste generico>> " + str(my_pilha.getAllIndexByValueGenerico("teste")))
print("Fazendo uma pesquisa em todos os valores por um array de indexs  elementar[3,1]>> " + str(my_pilha.getValuesByIndexsElementar([3,1])))
print("Fazendo uma pesquisa em todos os valores por um array de indexs  generico [3,1]>> " + str(my_pilha.getValuesByIndexsGenerico([3,1])))
print("Pegando todos os valores dos indices [3:5] elementar" + str(my_pilha.getValuesBySliceElementar(3,5)))
print("Pegando todos os valores dos indices [3:5] generico" + str(my_pilha.getValuesBySliceGeneric(3,5)))


my_pilha.removeAllGeneric()
print("Minha pilha esta vazia ? >> " + str(my_pilha.isEmptyElementar()))
my_pilha.list()

