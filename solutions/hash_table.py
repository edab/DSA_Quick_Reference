class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, initial_size = 10):

        self.num_entries = 0  # Number of slots filled
        self.p = 31           # The encoding prime number [usually 31 or 37]
        self.bucket_array = [None for i in range(initial_size)]

    def size(self):
        return self.num_entries

    def _hash_poly(self, key):

        # represents (self.p^0) which is 1
        current_coefficient = 1
        hash_code = 0
        num_buckets = len(self.bucket_array)

        for character in str(key):
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p

        return hash_code % num_buckets

    def _hash_mul(self, key):

        mult = 1
        hv = 0
        num_buckets = len(self.bucket_array)

        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % num_buckets

    def __setitem__(self, key, value):

        item = HashItem(key, value)
        h = self._hash_poly(key)
        num_buckets = len(self.bucket_array)

        # Found an empty slot
        while self.bucket_array[h] is not None:
            if self.bucket_array[h].key is key:
                break
            h = (h + 1) % num_buckets

        # Insert the element and update the count
        if self.bucket_array[h] is None:
            self.num_entries += 1
        self.bucket_array[h] = item

    def __getitem__(self, key):

        h = self._hash_poly(key)
        num_buckets = len(self.bucket_array)

        # We start looking for the key starting from that index
        while self.bucket_array[h] is not None:
            if self.bucket_array[h].key is key:
                return self.bucket_array[h].value
            h = (h + 1) % num_buckets

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
