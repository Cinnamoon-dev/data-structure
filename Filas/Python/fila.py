class No:
    def __init__(self, data = None ):
        self.data = data
        self.next = None

class Fila:
    
    def __init__(self=None) -> None:
        self.first_no  = None # representa o primeiro No
        self.last_no = None # representa o ultimo No

    def push(self, dado):

        celula = No(dado)

        if self.last_no is not None:
            self.last_no.next = celula # salvando a referencia para acessar 
        
        self.last_no = celula # toda vez que eu adicionar um dado ele deverá estar em ultimo 
        
        if self.first_no is None:
            self.first_no = celula

        return dado

    def list(self):

        if self.first_no is None:
            return None 

        aux = self.first_no

        while( aux ):
            print( aux.data )
            aux = aux.next

        return None
        

        

my_fila = Fila()
my_fila.push('pedro')
my_fila.push('john')
my_fila.push('gabriel')
my_fila.push('barreto')
my_fila.push('folha')
my_fila.list()