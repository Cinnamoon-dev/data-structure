import copy as cp

class Pilha :

    def __init__(self , dado = None, prox = None ):
        self.dado = dado
        self.prox = prox 

    def push(self, dado):

        new_pilha = Pilha(self.dado, self.prox)
        self.dado = dado
        self.prox = new_pilha

        return dado

    def pop(self):

        if not self :
            return None

        apagado = self.dado

        if self.prox:
            self.dado = None
            self.prox = None
        else:
            self.dado = self.prox.dado 
            self.prox = self.prox.prox


        return print("->>" + apagado);
    
    def list(self):
        aux = cp.deepcopy(self)

        while ( aux != None ):
            print( aux.dado )
            aux = aux.prox


nome_one = Pilha('Pen', None)
nome_two = Pilha('Apple', nome_one)
nome_three = Pilha('Apple', nome_two)
nome_four = Pilha('Pen', nome_three)

nome_four.list()


nome_four.pop()

