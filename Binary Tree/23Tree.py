class Tree23:
    def __init__(self, data: "list[int]" = [], father: "Tree23" = None) -> None:
        self.data = data
        self.father = father
        self.children = []