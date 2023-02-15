class Pilha :

    def __init__(self , dado ):
        self.dado = dado
        self.next = None 


    def push(self, dado):
        self.next = Pilha(dado)

    def pop(self):
        this = self 
        this.dado = this.next 
        

