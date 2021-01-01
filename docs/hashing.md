# Hashing

Hashing is the operation of transforming data of arbitrary size, like a string of characters, into a usually shorter fixed-length value, like an integer, that represents the original string. Hashing is used to index and retrieve items in a database because it is faster to find the item using the shorter hashed key than to find it using the original value.

## Hash function

A basic hash function can use the `ord()` function for get the ordinal value of each character of a string, and compute its sum:

```python
>>> sum(map(ord, 'earth thing'))
1102
```

The problem with this solution is that the same result can be obtained for am anagram, or another string that has two different letters:

```python
>>> sum(map(ord, 'heart night'))
1102
>>> sum(map(ord, 'keapu light'))
1102
```
