class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):
        
        self.size = 256  # Total number of slots in the table
        self.count = 0   # Number of slots filled
        self.slots = [None for i in range(self.size)]
        
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def __setitem__(self, key, value):
    
        item = HashItem(key, value)
        h = self._hash(key)

        # Found an empty slot
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size

        # Insert the element and update the count
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def __getitem__(self, key):

        h = self._hash(key)

        # We start looking for the key starting from that index
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size

        return None

# Test cases
ht = HashTable()
ht["watercolor"] = "William Henry Hunt"
ht["oil"] = "Pierre-Auguste Renoir"
ht["alcohol_markers"] = "Hayao Miyazaki"
ht["ad"] = "That values"
ht["ga"] = "doesn't collide"

for key in ("watercolor", "oil", "alcohol_markers", "worst", "ad", "ga"):
    v = ht[key]
    print(v)


