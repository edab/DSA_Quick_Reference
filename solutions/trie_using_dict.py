from collections import defaultdict

class TrieNode:

    def __init__(self):

        self.is_word = False
        self.children = defaultdict(TrieNode)

    def __str__(self, key="[root]", level=0):

        ret = "  " * (level-1) + "+-" * (level > 0) + key + "\n"
        for key in self.children:
            ret += self.children[key].__str__(key, level + 1)
        return ret

class Trie:

    def __init__(self, words = None):

        self.root = TrieNode()

        if words is not None:
            for word in words:
                self.insert(word)

    def insert(self, word):

        curr_node = self.root

        for char in word:
            curr_node = curr_node.children[char]

        curr_node.is_word = True

    def search(self, word):
      
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.is_word

    def __str__(self, level=0, node=None):
        ret = "Trie\n"
        ret += str(self.root)
        return ret


# Test cases
word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses']
word_trie = Trie(word_list)


# Test words
test_words = ['bear', 'goo', 'good', 'goos']
test_results = [True, True, True, False]

print(word_trie)
for word, res in zip(test_words, test_results):
  pass_str = f"Pass [{word} is in trie]"
  fail_str = f"Fail [{word} is in trie]"
  print (pass_str if (word_trie.search(word) == res) else fail_str)
