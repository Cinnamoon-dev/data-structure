class Pilha :

    def __init__(self , dado = None, prox = None ):
        self.dado = dado
        self.prox = prox 

    def popular_com_array(self, array_for_insert = None):

        if array_for_insert is None:
            return None

        for value in array_for_insert:
            self.pushWithClassLinkedList(value)

    def pushWithClassLinkedList( self, dado : int ) -> int:

        new_pilha = Pilha( self.dado, self.prox )
        self.dado = dado
        self.prox = new_pilha

        return dado

    def pop( self ):

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
    def peakElementar( self ) -> int:
        # primeiro elemento de uma pilha é o topo 
        aux_pilha = Pilha( self.dado, self.prox )
        aux_data = aux_pilha.pop()
        return aux_data

    # Q4 Generico primeiro conforme a estrutura
    def peakGenerico( self ) -> int:
        return self.dado
    
    # Q5 Elementar averiguar se esta vazio 
    def isEmptyElementar( self ) -> bool:
        # meu pop só retorna none caso meu self n tenha referencia.
        aux_pilha = Pilha( self.dado , self.prox )
        aux_data = aux_pilha.pop()
        return True if aux_data is None else False
        
    # Q5 Generico averiguar se esta vazio
    def isEmptyGeneric( self ) -> bool:
        return True if self.dado is None else False
    
    # Q6 Elementar Return length of my structure
    def tamanhoDaPilhaElementar( self ) -> int:
        # usando uma pilha aux
        aux_pilha = Pilha( self.dado, self.prox )
        counter = 0

        while aux_pilha.pop() is not None:
            counter += 1

        return counter
    
    # Q6 Generic Return length of my structure
    def tamanhoDaPilhaGeneric( self ) -> int :
        # usando um ponteiro aux 
        aux_pilha : Pilha = self
        counter : int = 0
        
        while aux_pilha.dado is not None:
            counter += 1
            aux_pilha = aux_pilha.prox

        return counter
    
    # Q7 Elementar Return last element in my scruture
    def lastElementElementar( self ) -> int:

        aux_pilha = Pilha( self.dado, self.prox )

        while not aux_pilha.prox is None:
            aux_pilha = aux_pilha.prox
    
        return aux_pilha.dado

    # Q7 Generico Return last element in my scruture
    def lastElementGeneric( self ) -> int:

        aux_pilha = Pilha(self.dado, self.prox)

        while aux_pilha.tamanhoDaPilhaGeneric() != 1:
            aux_pilha.pop()
    
        return aux_pilha.dado
    
    # Q8 Elementar Return a determined value in a spcific index
    def getValueByIndexElementar( self, index : int ) -> int:
        aux_pilha = Pilha( self.dado, self.prox )
        counter = 0
        
        while counter != index and aux_pilha is not None:
            counter += 1
            aux_pilha = aux_pilha.prox

        if aux_pilha is None:
            return -1
        
        return aux_pilha.dado
    
    # Q8 Generic Return a determined value in a spcific index
    def getValueByIndexGeneric( self, index : int ) -> int:

        aux = self
        my_values = []

        while aux.prox is not None :
            my_values.append( aux.dado )
            aux = aux.prox

        return my_values[index]
    
    # Q9 Elementar Return the first index that storage a specific value
    def getIndexByValueElementar( self, dado : int ) -> int:

        counter = 0
        aux_pointer = self

        while aux_pointer.dado != dado and aux_pointer.prox is not None:    
            aux_pointer = aux_pointer.prox
            counter += 1

        if aux_pointer.prox is None and aux_pointer.dado != dado:
            return -1

        return counter
    
    # Q9 Generic Return the first index that storage a specific value
    def getIndexByValueGeneric( self, dado : int ) -> int:

        counter = 0
        aux_pilha = Pilha( self.dado, self.prox )

        while aux_pilha.dado != dado and aux_pilha.pop() is not None:
            counter += 1

        if aux_pilha.prox is None and aux_pilha.dado != dado:
            return -1

        return counter
    
    # Q10 Elementar Return a array of indexs that storage a specific value
    def getAllIndexByValueElementar( self, dado : int ):
        
        result = []
        
        if self is None:
            return result

        aux = self
        counter = 0

        while aux is not None:

            if aux.dado == dado:
                result.append(counter)
            
            aux = aux.prox
            counter += 1
        
        return result
    
    # Q10 Generic Return a array of indexs that storage a specific value
    def getAllIndexByValueGenerico( self, dado : int ) -> int:
        
        result = []

        if self is None:
            return result
        
        counter = 0
        my_newpilha = Pilha(self.dado, self.prox)

        my_dado = my_newpilha.pop()

        while my_dado is not None:
            
            if my_dado == dado:
                result.append(counter)
            
            my_dado = my_newpilha.pop()
            counter += 1

        return result

    # Q11 Elementar return a array of values in an array of index
    def getValuesByIndexsElementar( self, indexs ) :
        
        result = []

        if self is None:
            return result

        for index in indexs:
    
            aux = self
            counter = 0

            while counter != index:
                aux = aux.prox
                counter += 1

            result.append(aux.dado)

        return result
    
    # Q11 Generic return a array of values in an array of index
    def getValuesByIndexsGenerico( self, indexs ) :

        result = []

        if self is None:
            return result

        aux = self

        for index in indexs:
            data = aux.getValueByIndexGeneric(index)
            result.append(data)
        
        return result
    
    # Q12 Elementar return a array sliced of my array
    def getValuesBySliceElementar(self, start : int , end : int ) :
        
        result = []

        if self is None:
            return result

        aux = self
        counter = 0

        while counter != end :

            if counter >= start:
                result.append(aux.dado)

            counter += 1
            aux = aux.prox

        return result
    
    # Q12 Generic return a array sliced of my array
    def getValuesBySliceGeneric(self, start : int, end : int ) :
        result = []

        if self is None:
            return result

        for index in range(start, end):
            result.append(self.getValueByIndexElementar(index))

        return result
    
    # Q13 Elementar Remove All values of my stack 
    def removeAllElementar(self) -> None:
        
        aux = self

        while aux.pop() is not None:
            continue 
    
        return self

    # Q13 Elementar Remove All values of my stack
    def removeAllGeneric(self) -> None:
        self.dado = None
        self.prox = None

        return self
    
    # Q14 Elementar Remove a specific value in a determinate index
    def removeByIndexElementar(self ,index : int) -> int:

        aux = self
        counter = 0

        while counter != index and aux is not None:
            aux = aux.prox
            counter += 1

        if aux is None:
            return -1

        deleted = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return deleted
    
    # Q14 Generic Remove a specific value in a determinate index
    def removeByIndexGenerico(self ,index : int) -> int:

        aux = self
        dado_for_remove = self.getValueByIndexGeneric(index)

        while aux.dado != dado_for_remove:
            aux = aux.prox

        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox
        
        return dado_for_remove
    
    # Q15 Generic Remove the first data that has equal dado value 
    def removeFirstElementByValueElementar(self, dado : int) -> int:
        
        aux = self

        while aux.dado != dado:
            aux = aux.prox
        
        # remove o primeiro elemento que ele encontrar
        removed_element = aux.dado
        aux.dado = aux.prox.dado
        aux.prox = aux.prox.prox

        return removed_element
    
    # Q15 Generic Remove the first data that has equal dado value        
    def removeFirstElementByValueGenerico( self, dado : int) -> int:

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
    def removeAllByValueElementar(self, value : int) -> int:
        
        aux = self 

        while aux.dado is not None:
            
            if aux.dado == value:
                aux.pop()
                continue

            aux = aux.prox

        return True
    
    # Q16 Generic Remove all datas with a specific value
    def removeAllByValueGeneric( self, value : int ) -> bool:

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
    def removeAllByIndexesElementar( self, indexs ) -> bool:

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
    def removeAllByIndexesGeneric(self, indexs ) -> bool:

        for index in indexs:
            self.removeByIndexElementar(index)

        return True
    
    # Q18 Elementar Remove all datas starting in start and close in end
    def removeAllBySliceElementar( self, start : int, end : int ) -> bool:

        aux = self
        counter = 0

        if start > end:
            return False

        while aux is not None:

            if counter >= start and counter < end:
                aux.pop()
                counter += 1 
                continue

            counter += 1
            aux = aux.prox

        return True

    # Q18 Generic Remove all datas starting in start and close in end
    def removeAllBySliceGeneric( self, start : int, end : int ) -> bool:

        if start > end:
            return False
        
        aux = start
        
        for i in range(start, end):
            self.removeByIndexElementar(aux)
            aux += 1 - i

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
    def setValueInIndexGeneric(self, index : int , value : int) -> bool:
        aux = self
    
        for index in range(index):
            aux = aux.prox 

        aux.dado = value
        return True

    # Q20 Elementar Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesElementar( self, indexs, elements ) -> bool:

        if len(indexs) != len(elements):
            return -1

        counter_two = 0 # vai ser no maximo do tamanho da minha pilha
        limite_loops = len(indexs)
        counter_one = 0 # vai ser no maximo do tamanho dos vetores de entrada

        while counter_two < limite_loops:
            aux = self

            while aux is not None:

                if counter_one == indexs[ counter_two ]:
                    aux.dado = elements[ counter_two  ]

                counter_one += 1
                aux = aux.prox

            counter_one = 0
            counter_two += 1

        return True
    
    # Q20 Generico Change my stack values with a list of values and a list of indexs 
    def setValuesInIndexesGenerico( self ,indexs , elements ):

        counter_one = 0

        for index in indexs:
            self.setValueInIndexGeneric( index, elements[counter_one] )
            counter_one += 1

        return True


if __name__ == '__main__':

    # populando com array 
    pilha = Pilha()
    print("\n popular com array", "#"*10)
    pilha.popular_com_array(['pedro','henrique', 'barreto','freires'])
    pilha.list()
    print('\npop',"#"*10)
    pilha.pop()
    pilha.list()
    print('\npeak',"#"*10)
    print(pilha.peakElementar(), "Elementar")
    print(pilha.peakGenerico(), "Generico")
    print('\nisEmpty',"#"*10)
    print(pilha.isEmptyGeneric(), "Generico")
    print(pilha.isEmptyElementar(), "Elementar")
    print('\nTam. Pilha',"#"*10)
    print(pilha.tamanhoDaPilhaElementar(), "Elementar")
    print(pilha.tamanhoDaPilhaGeneric(), "Generico")
    print('\nLast Element',"#"*10)
    print(pilha.lastElementElementar(), "Elementar")
    print(pilha.lastElementGeneric(), "Generico")
    print('\nGet Value by Index',"#"*10)
    print(pilha.getValueByIndexElementar(1), "Elementar")
    print(pilha.getValueByIndexGeneric(1), "Generico")
    print('\nGet Index By Value',"#"*10)
    print(pilha.getIndexByValueElementar('pedro'), "Elementar")
    print(pilha.getIndexByValueGeneric('pedro'), "Generico")
    print('\nGet All Index by Value',"#"*10)
    print(pilha.getAllIndexByValueElementar(1), "Elementar")
    print(pilha.getAllIndexByValueGenerico(1), "Generico")
    print('\nGet All Values by Indexs',"#"*10)
    print(pilha.getValuesByIndexsElementar( [1,2]), "Elementar")
    print(pilha.getValuesByIndexsGenerico([1,2]), "Generico")
    print('\nGet Values by Slice',"#"*10)
    print(pilha.getValuesBySliceElementar(1,2), "Elementar")
    print(pilha.getValuesBySliceGeneric(1,2), "Generico")
    
    print('\nRemove All',"#"*10, "Elementar")
    pilha.removeAllElementar()
    pilha.list()
    pilha.popular_com_array(['pedro', 'barreto','freires', 'souza','andrade','bernado','campos'])
    
    print('\nRemove All',"#"*10, "Generico")
    pilha.removeAllGeneric()
    pilha.list()
    pilha.popular_com_array(["pedro",'henrique', 'barreto','freires'])
    
    print("\n### removing index 2  ####", "Elementar")
    pilha.removeByIndexElementar(2)
    pilha.list()

    print("\n### removing index 2  ####", "Generico")
    pilha.removeByIndexGenerico(2)
    pilha.list()
    
    print('\nRemove by Value ',"#"*10)
    pilha.removeAllGeneric()
    pilha.popular_com_array( ["pedro",'henrique','barreto', 'freires'])
    pilha.removeFirstElementByValueGenerico('pedro')
    pilha.list()
    print('-'*5)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    pilha.removeFirstElementByValueElementar('pedro')
    pilha.list()

    print('\nRemove All by a Value ',"#"*10)
    
    pilha.removeAllGeneric()
    pilha.popular_com_array( ["pedro",'henrique','barreto', 'freires'])
    pilha.removeAllByValueElementar('pedro')
    pilha.list()
    print('-'*5)
    
    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    pilha.removeAllByValueGeneric('pedro')
    pilha.list()
    
    print('\nRemove All by indexs  ',"#"*10)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    pilha.removeAllByIndexesElementar([1,2])
    pilha.list()
    print('-'*5)
    
    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    pilha.removeAllByIndexesElementar([1,2])
    pilha.list()

    print('\nRemove All by slice  ',"#"*10)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("removing... , slice : (0,4), Elementar")
    pilha.removeAllBySliceElementar(0,4)
    pilha.list()
    print('-'*5)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("removing... , slice : (0,4), Elementar")
    pilha.removeAllBySliceGeneric(0,4)
    pilha.list()

    print('\nSet Value in Index Elementar',"#"*10)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("(3,'catatau'), Elementar")
    pilha.setValueInIndexElementar(3,'catatau')
    pilha.list()
    print('-'*5)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("(3,'catatau'), Generic")
    pilha.setValueInIndexGeneric(3,'catatau')
    pilha.list()

    print('\n Set Values in Indexs',"#"*10)

    pilha.removeAllGeneric()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("index : [0,2], array : ['catatau', 'iceberg']", "Generic")
    pilha.setValuesInIndexesGenerico([0,2],['catatau','iceberg'])
    pilha.list()
    print('-'*5)

    pilha.removeAllElementar()
    pilha.popular_com_array(["pedro",'henrique','barreto', 'freires'])
    print("index : [0,2], array : ['catatau', 'iceberg']", "Elementar")
    pilha.setValuesInIndexesElementar([0,2],['catatau','iceberg'])
    pilha.list()


    