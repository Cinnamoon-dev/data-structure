class Pilha :

    def __init__(self , dado = None, prox = None ):
        self.dado = dado
        self.prox = prox 

    # função criada para auxiliar nas questões elementares
    def create_aux_stack(self):

        stack_aux = Pilha()
        stack_two = Pilha()

        # ordem n
        while True:
            data_temp = self.pop()
            
            if data_temp is None:
                break

            stack_aux.pushWithClassLinkedList(data_temp)
        
        # ordem n 
        while True:
            data_temp = stack_aux.pop()

            if data_temp is None:
                break

            stack_two.pushWithClassLinkedList(data_temp)

        return stack_aux

    def create_aux_inverted_stack(self):
        # quando usar essa função self fica sem referencias para os nós
        pilha_aux = Pilha()
        
        # inserindo os dados invertidos ! 
        while self.peakElementar() is not None:
            pilha_aux.pushWithClassLinkedList(self.pop())

        return pilha_aux

    def popular_com_array(self, array_for_insert = None):

        if array_for_insert is None:
            return None

        for value in array_for_insert:
            self.pushWithClassLinkedList(value)

    def pushWithClassLinkedList( self, dado  ) :

        new_pilha = Pilha( self.dado, self.prox )
        self.dado = dado
        self.prox = new_pilha

        return dado

    def pop( self ) :

        apagado = self.dado

        if not self.prox:
            self.dado = None
            self.prox = None
        else:
            self.dado = self.prox.dado 
            self.prox = self.prox.prox

        return apagado
    
    def list( self ) -> None:

        aux = self

        while aux.prox is not None :
            print( aux.dado )
            aux = aux.prox

    # Q4 retorna o primeiro conforme a estrutura 
    def peakElementar( self ) :
        # primeiro elemento de uma pilha é o topo 
        aux_data = self.pop()
        self.pushWithClassLinkedList(aux_data)
        
        return aux_data

    # Q4 Generico primeiro conforme a estrutura
    def peakGenerico( self ) :
        return self.dado
    
    # Q5 Elementar averiguar se esta vazio 
    def isEmptyElementar( self ) -> bool:
        # meu pop só retorna none caso meu self n tenha referencia.
        data_temp = self.pop()
        
        if data_temp is None:
            return True
        
        self.pushWithClassLinkedList(data_temp)

        return False
        
    # Q5 Generico averiguar se esta vazio
    def isEmptyGeneric( self ) -> bool:
        return True if self.dado is None else False
    
    # Q6 Elementar Return length of my structure
    def tamanhoDaPilhaElementar( self ) :
        # usando uma pilha aux
        counter = 0
        aux_pilha = self.create_aux_stack()

        while aux_pilha.pop() is not None:
            counter += 1

        return counter
    
    # Q6 Generic Return length of my structure
    def tamanhoDaPilhaGeneric( self ) :
        
        counter   = 0
        aux_pointer = self
        
        while aux_pointer.prox is not None:
            counter += 1
            aux_pointer = aux_pointer.prox

        return counter
    
    # Q7 Elementar Return last element in my scruture
    def lastElementElementar( self ) :

        aux = self.create_aux_inverted_stack()
        return aux.peakElementar()

    # Q7 Generico Return last element in my scruture
    def lastElementGeneric( self ) :

        aux_pilha = Pilha( self.dado, self.prox)

        while aux_pilha.tamanhoDaPilhaGeneric() != 1:
            aux_pilha.pop()
    
        return aux_pilha.dado
    
    # Q8 Elementar Return a determined value in a spcific index
    def getValueByIndexElementar( self, index  ) :
        counter = 0
        data_temp = 1
        aux_pilha = self.create_aux_stack()
        
        while counter != index and data_temp is not None:
            counter += 1
            data_temp = aux_pilha.pop()

        if data_temp is None:
            return -1
        
        return aux_pilha.dado
    
    # Q8 Generic Return a determined value in a specific index
    def getValueByIndexGeneric( self, index  ) :

        aux = self
        my_values = []

        while aux is not None :
            my_values.append( aux.dado )
            aux = aux.prox

        try:
            return my_values[index]
        except IndexError:
            return None

    # Q9 Elementar Return the first index that storage a specific value
    def getIndexByValueElementar( self, dado ) :
        # esse counter é meu index
        counter = 0
        aux_pointer = self.create_aux_stack()

        while aux_pointer.peakElementar() is not None:    
            
            if aux_pointer.pop() == dado:
                return counter
            
            counter += 1

        if aux_pointer.peakElementar() is None:
            return -1

        return counter
    
    # Q9 Generic Return the first index that storage a specific value
    def getIndexByValueGeneric( self, dado  ):

        counter = 0
        aux_pilha = Pilha( self.dado, self.prox )

        while aux_pilha.dado != dado and aux_pilha.pop() is not None:
            counter += 1

        if aux_pilha.dado is None or aux_pilha.dado != dado:
            return -1

        return counter
    
    # Q10 Elementar Return a array of indexs that storage a specific value
    def getAllIndexByValueElementar( self, dado  ):
        
        counter = 0
        result = []
        aux_stack = self.create_aux_stack()

        while aux_stack.peakElementar() is not None:

            if aux_stack.pop() == dado:
                result.append(counter)
            
            counter += 1
        
        return result
    
    # Q10 Generic Return a array of indexs that storage a specific value
    def getAllIndexByValueGenerico( self, dado  ) :
        
        result = []
        my_node = Pilha(self.dado, self.prox)
        tam_stack = self.tamanhoDaPilhaGeneric()

        for i in range(0, tam_stack):
            if my_node.dado == dado:
                result.append(i)

            my_node = my_node.prox

        return result

    # Q11 Elementar return a array of values in an array of index
    def getValuesByIndexsElementar( self, indexs ) :
        
        result = []
        for index in indexs:
    
            counter = 0
            aux = self.create_aux_stack()

            while counter != index:
                aux.pop()
                counter += 1

            result.append(aux.pop())

        return result
    
    # Q11 Generic return a array of values in an array of index
    def getValuesByIndexsGenerico( self, indexs ) :

        result = []

        for index in indexs:
            data = self.getValueByIndexGeneric(index)
            result.append(data)
        
        return result
    
    # Q12 Elementar return a array sliced of my array
    def getValuesBySliceElementar(self, start  , end  ) :
        
        counter = 0
        result = []
        aux = self.create_aux_stack()

        while counter != end :

            if counter >= start:
                result.append(aux.dado)

            counter += 1
            aux = aux.prox

        return result
    
    # Q12 Generic return a array sliced of my array
    def getValuesBySliceGeneric(self, start , end  ) :
        result = []

        for index in range( start, end ):
            result.append( self.getValueByIndexElementar(index) )

        return result
    
    # Q13 Elementar Remove All values of my stack 
    def removeAllElementar(self) -> None:
        
        while self.pop() is not None:
            continue 
    
        return self.dado

    # Q13 Elementar Remove All values of my stack
    def removeAllGeneric(self) -> None:
        self.dado = None
        self.prox = None

        return self
    
    # Q14 Elementar Remove a specific value in a determinate index
    def removeByIndexElementar(self ,index ) :

        counter = 0
        pilha_aux = self.create_aux_inverted_stack()

        while pilha_aux.peakElementar() is not None:
            
            if index == counter:
                removed_element = pilha_aux.pop()
                continue

            counter += 1
            # inserindo na ordem correta ! 
            data_inserted = pilha_aux.pop()
            self.pushWithClassLinkedList(data_inserted)

        return removed_element
    
    # Q14 Generic Remove a specific value in a determinate index
    def removeByIndexGenerico(self ,index ) :

        aux = self
        
        dado_for_remove = self.getValueByIndexGeneric(index)
        
        if dado_for_remove == None:
            return -1

        while aux.dado != dado_for_remove:
            aux = aux.prox

        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox
        
        return dado_for_remove
    
    # Q15 Generic Remove the first data that has equal dado value 
    def removeFirstElementByValueElementar(self, dado ):
        
        isValid = 1
        pilha_aux = self.create_aux_inverted_stack()

        while pilha_aux.peakElementar() is not None:
            data_temp = pilha_aux.pop()
            
            if data_temp == dado and isValid != 0:
                isValid = 0
                continue

            self.pushWithClassLinkedList(data_temp)

        return dado
    
    # Q15 Generic Remove the first data that has equal dado value        
    def removeFirstElementByValueGenerico( self, dado ) :

        aux = self
        counter = 0 
        index_for_remove = aux.getIndexByValueElementar(dado)

        if index_for_remove == -1:
            return -1

        while counter != index_for_remove:
            aux = aux.prox
            counter += 1

        removed_element = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return removed_element

    # Q16 Elementar Remove all datas with a specific value
    def removeAllByValueElementar(self, value ) :
        
        pilha_aux = self.create_aux_inverted_stack()

        while pilha_aux.peakElementar() is not None:

            data_temp = pilha_aux.pop()
            
            if data_temp == value:
                data_temp = pilha_aux.pop()
            
            self.pushWithClassLinkedList( data_temp )

        return True
    
    # Q16 Generic Remove all datas with a specific value
    def removeAllByValueGeneric( self, value  ) -> bool:

        counter = 0
        qtd_itens = self.tamanhoDaPilhaElementar()

        # o qtd de loops é limitada a quantidade N de elementos 
        while counter != qtd_itens: 

            index_to_remove = self.getIndexByValueElementar(value) 

            if index_to_remove == -1:
                return True
            
            self.removeByIndexElementar(index_to_remove)
            counter += 1 

        return True
    
    # Q17 Elementar Remove all datas with a specific index
    def removeAllByIndexesElementar( self, indexs ) -> bool:

        pilha_aux = self.create_aux_inverted_stack()

        for index in indexs:
            
            while pilha_aux.peakElementar() is not None:
                
                if index == counter:
                    pilha_aux.pop()
                
                counter += 1   
                self.pushWithClassLinkedList( pilha_aux.pop() )
                
            counter = 0
            # crio minha stack invertida com os dados atualizados
            pilha_aux = self.create_aux_inverted_stack()

        return True
    
    # Q17 Generico Remove all datas with a specific index
    def removeAllByIndexesGeneric(self, indexs ) -> bool:

        for index in indexs:
            self.removeByIndexElementar(index)

        return True
    
    # Q18 Elementar Remove all datas starting in start and close in end
    def removeAllBySliceElementar( self, start , end  ) -> bool:

        counter = 0
        aux_stack = self.create_aux_stack()

        if start > end:
            return False

        while aux_stack.peakElementar() is not None:

            if counter >= start and counter < end:
                # não adiciono esse intervalo
                counter += 1 
                aux_stack.pop()
                continue

            counter += 1
            self.pushWithClassLinkedList(aux_stack.pop())

        return True

    # Q18 Generic Remove all datas starting in start and close in end
    def removeAllBySliceGeneric( self, start , end  ) -> bool:

        if start > end:
            return False
        
        aux = start
        
        for i in range(start, end):
            self.removeByIndexElementar(aux)
            aux += 1 - i

        return True
    
    # Q19 Elementar Assignment a value for a specific index
    def setValueInIndexElementar( self, index:int, value:str ) -> bool:

        counter = 0
        aux_stack = self.create_aux_inverted_stack()

        while aux_stack.peakElementar() is not None:
            
            if counter == index :
                counter += 1
                aux_stack.pop()
                self.pushWithClassLinkedList( value ) # valor atualizado
                continue

            counter += 1
            self.pushWithClassLinkedList( aux_stack.pop() )

        return True

    # Q19 Generic Assignment a value for a specific index
    def setValueInIndexGeneric(self, index  , value ) -> bool:
        aux = self
    
        for index in range(index):
            aux = aux.prox 

        aux.dado = value
        return True

    # Q20 Elementar Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesElementar( self, indexs, elements ) -> bool:
        
        counter = 0 
        counter_two = 0 # contador dos elements
        limite_loops = len( indexs )

        while counter_two < limite_loops:
            aux_stack = self.create_aux_inverted_stack()

            while aux_stack.peakElementar() is not None:

                if counter == indexs[ counter_two ]:
                    aux_stack.pop()
                    self.pushWithClassLinkedList( elements[counter_two] )

                counter += 1
                self.pushWithClassLinkedList( aux_stack.pop() )

            counter_two += 1

        return True
    
    # Q20 Generico Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesGenerico( self ,indexs , elements ):

        counter_one = 0

        for index in indexs:
            self.setValueInIndexGeneric( index, elements[counter_one] )
            counter_one += 1

        return True
