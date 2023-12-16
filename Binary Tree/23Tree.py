class Tree23:
    def __init__(self, data: "list[int]" = [], father: "Tree23" = None) -> None:
        self.data = data
        self.father = father
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0

    def search(self, data):
        current = self

        while True:
            if not data in current.data and current.isLeaf():
                return None

            if data in current.data:
                return current

            if len(current.data) == 1:
                if data < current.data[0]:
                    current = current.children[0]
                    continue

                current = current.children[1]
                continue
            
            if len(current.data) == 2:
                if data < current.data[0]:
                    current = current.children[0]
                    continue

                if current.data[0] < data < current.data[1]:
                    current = current.children[1]
                    continue

                if current.data[1] < data:
                    current = current.children[2]
                    continue
        
    # Insert
    # Se tiver 3 dados num nó subir um valor com a função split
    # Criar um while para fazer essa verificação até infinitos pais
    # Se o pai for None que tem criar um novo pai com os dois valores de baixo
    # Separar em dois while um para subir o 3 até precisar criar um novo pai
    # Outro para ir quebrando os filhos em novos nós, começar olhando para o primeiro caso quando se insere os tres primeiros valores
    # Lembrar que o pior caso em que todos os nos são 3-nodes é o pior e que podem existir nós com um espaço vago no caminho de subida
    def split(self):
        current = self

        while len(current.data) == 3 and current.father is not None:
            value = current.data.pop(1)
            current.father.data.append(value)
            current.father.data.sort()

            current = current.father