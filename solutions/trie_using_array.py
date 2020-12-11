class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        """
        Private helper function, that converts current character into index
        use only 'a' through 'z' and lower case
        """
        return ord(ch) - ord('a')

    def insert(self, key):

        curr_node = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]

        curr_node.is_word = True

    def search(self, key):

        curr_node = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not curr_node.children[index]:
                return False
            curr_node = curr_node.children[index]

        return curr_node != None and curr_node.is_word

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