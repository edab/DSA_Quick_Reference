from collections import defaultdict

class TrieNode:

  def __init__(self):

    self.is_word = False
    self.children = defaultdict(TrieNode)
    
class Trie:

  def __init__(self):

    self.root = TrieNode()

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

# Test cases
word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.insert(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.search(word):
        print(f'"{word}" is a word.')
    else:
        print(f'"{word}" is not a word.')
