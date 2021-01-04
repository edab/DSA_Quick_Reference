# Hashing

Hashing is the operation of transforming data of arbitrary size, like a string of characters, into a usually shorter fixed-length value, like an integer, that represents the original string. Hashing is used to index and retrieve items in a database because it is faster to find the item using the shorter hashed key than to find it using the original value.

## Hash function

A basic hash function can use the `ord()` function for get the ordinal value of each character of a string, and compute its sum. The problem with this solution is that the same result can be obtained for am anagram, or another string that has two different letters:

```python
for item in ('earth thing', 'heart night', 'keapu light'):
   print(f"{item}: {sum(map(ord, item))}")

earth thing: 1102
heart night: 1102
keapu light: 1102
```

Hash function need to be very fast, and fast, so instead of creating a perfect and complex function capable of producing always unique key, we accept less perfect functions that produces collision.

One simple improvement can be the ability to consider the positions of each char adding a multiplier, that improve the results but doesn't prevent every collisions:

```python
def hash(input):
  mult = 1
  hv = 0
  for ch in input:
    hv += mult * ord(ch)
    mult += 1
  return hv

for item in ('earth thing', 'heart night', 'keapu light', 'ad', 'ga'):
  print(f"{item}: {hash(item)}")

earth thing: 6635
heart night: 6678
keapu light: 6664
ad: 297
ga: 297
```

A lot of research has been done trying to figuring out a good hash functions for strings, and one of the best ones is the one where we multiply each character $ch$ by a prime number $p$, usually 31 or 37, with increasing power, obtaining a good distribution:

$$ch_0 * p^0 + ch_1 * p^1 + ch_2 * p^2 + ch_3 * p^3 + ch_4 * p^4 ... $$

## Collision handling

The _hash function_ essentially reduces a large variable-length index to a fixed-length small one, and since this operation is prone to the collision, we have to be sure that the key remains unique.

Two different approach can be used to this problem:

- **Separate chaining**: were we use the same bucket to store multiple objects, and the bucket in this case will store a linked list of key-value pairs.
- **Open Addressing**: were, after knowing the bucket index, if is empty we store the value in it, otherwise we start an operation called _probing_ were we search another index using different techniques like: linear probing (we move to the next bucket), quadrating probing, double hashing (were we use an alternative hashing function). 



## Implementation

Python3 implementation: [hast_table.py](../solutions/hast_table.py)
