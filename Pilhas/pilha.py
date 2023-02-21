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

        if not self.prox:
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


my_pilha = Pilha('Pen', None)

my_pilha.push('carro')
my_pilha.push('tapete')
my_pilha.push('lampada')
my_pilha.push('computador')

my_pilha.pop()

my_pilha.list()