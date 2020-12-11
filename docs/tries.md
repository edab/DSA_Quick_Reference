# Tries

A **Trie**, also known as a **Prefix Tree**, is an ordered tree where the keys are usually strings. Unlike a _Binary Search Tree (BST)_, no node store the key, but instead the position of the node in the tree defines the key with which it is associated.

- Time Complexity (m -> key length, n -> alphabet length)
  - Average
    - Access: $O(m)$
    - Search: $O(m)$
    - Insert: $O(m)$
    - Delete: $O(m)$
  - Worst
    - Access: $O(m*n)$
    - Search: $O(m*n)$
    - Insert: $O(m*n)$
    - Delete: $O(m*n)$

Tries were first described by René de la Briandais in 1959, and are an efficient solution to a common problem: build a function that provides a spell check.

The function we need to implement should only return `True` if the word exists, otherwise `False`. The simplest solution is to have a _hashmap_ of all know words, and in that case, it will take $O(1)$ to see if a word exists, but the memory size would be $O(m*n)$, where `m` is the length of the word, and `n` is the number of words.

The basic idea behind this data structure is that many different words share a common prefix, so why not save it once?

A _Trie_ can definitely help on space complexity, since he allows to save a prefix shared between many different words in the same place while sacrificing a little on performance.

## Common problems solved using Trie

- ***Longest prefix matching***: Given a dictionary of words and an input string, find the longest prefix of the string which is also a word in dictionary.
- ***Ukkonen’s Suffix Tree Construction***

## Implementations

### Basic Trie using dictionary

Let's think about three different words:

- analysis
- analyze
- anatomy

We need to find a way to save in memory the prefix ana and analy only one time, something like this:

```
- [ana]
  - [tomy] -> word
  - [ly]
    -[sis] -> word
    -[ze] -> word
```

We can create a node that has: a _boolean_ that help to understand if the letter encountered up that node form a valid word, and a _dictionary of nodes_.

A cleaner way to do that is using a `DefaultDict`, that in case the key is not available will return a default value.

```python
from collections import defaultdict

class TrieNode:

  def __init__(self):

    self.is_word = False
    self.children = defaultdict(TrieNode)
```

We can implement the data structure implementing a method for adding new words and one for checking if they exists:

```python
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
```

### Basic Trie using an array of characters

Another common implementation of a _Trie_ use an array of 26 elements, one for each letter, instead of the `dict()`.

```python
class TrieNode:

    def __init__(self):

        self.children = [None] * 26
        self.is_word = False

class Trie:

    def __init__(self):

        self.root = TrieNode()

    def _char_to_index(self, ch):
        """
        Converts current character into index from 'a' lower case
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
```

## References

- [File searching using variable length keys, Rene De La Briandais, 1959](https://www.semanticscholar.org/paper/File-searching-using-variable-length-keys-Briandais/3ce3f4cc1c91d03850ed84ef96a08498e018d18f)
- [Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology, Dan Gusfield, 1997](https://www.amazon.in/Algorithms-Strings-Trees-Sequences-Computational/dp/0521585198)
- [Algorithms, Sedgewick and Wayne, Addison Wesley, 2011, Chap. 5](https://www.amazon.com/Algorithms-4th-Robert-Sedgewick/dp/032157351X)
