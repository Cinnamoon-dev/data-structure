class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.hashTable = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_value(self, key, value): # 1, 2
        # Acha a chave
        # Acessa o indice da chave
        # Procurar no bucket se a chave ja existe
        # coloca nesse bucket a tupla (key, value)
        hashed_key = hash(key) % self.size
        bucket = self.hashTable[hashed_key]
        found_key = False

        for record in bucket:
            if record[0] == key:
                found_key = True
                break
        
        if found_key:
            bucket[hashed_key] = (key, value)

        else:
            bucket.append((key, value))

    def get_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashTable[hashed_key]

        for record in bucket:
            if record[0] == key:
                return record[1]
        
        return None

    def delete_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashTable[hashed_key]

        value = self.get_value(key)

        if not value:
            return

        bucket.remove((key, value))


asd = HashTable(50)

asd.set_value('cor', 'preta')
print(asd.get_value('cor'))
asd.delete_value('cor')
print(asd.get_value('cor'))