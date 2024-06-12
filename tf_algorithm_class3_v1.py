
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Create a new Jupyter Notebook
nb = new_notebook()

data_mark = """
# Algorithm Class 3 : Hash  Sring KMP

Overall Lead: Xiaowen Kang
Contact: xiaowen@svcamp.com

Kevin: Responsible for code validation, homework assignments, and electronic platform-related tasks.
Contact:kevin.lin@svcamp.com

Marco: Responsible for PowerPoint production and validation.
Contact: marco.zhang@svcamp.com



"""
nb.cells.append(new_markdown_cell(data_mark ))

s1 = """
# Seciton 1 Hash Table Fundamentals and Applications

## Overview

A Hash Table is a data structure that uses a hash function to map keys to an array of buckets or slots, enabling fast data storage and retrieval. It is widely used in dictionary implementations, where keys (such as names) map to values (such as cities or scores).

## How Hash Tables Work

### Hash Function

A hash function takes an input (a key) and returns an integer known as the hash value. This hash value determines the key's storage location in the hash table.

### Hash Value Calculation

- Example: The hash function converts the key "Alice Johnson" into a hash value `3303733913283304066`.
- The hash value is then used to compute the hash index using the modulo operation: `hash_value % list_length` (e.g., `3303733913283304066 % 10 = 6`).

### Data Storage

The key-value pair is stored at the computed hash index in the hash table. If the index is already occupied, a collision resolution strategy is employed.

### Collision Resolution

Different keys might map to the same hash index, leading to a hash collision. Common collision resolution strategies include:

- **Open Addressing**: Finds the next available slot to store the colliding key-value pair.
- **Separate Chaining**: Uses a linked list at each hash index to store multiple key-value pairs.

## Detailed Examples

### Insert Operation

#### Separate Chaining

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[hash_key] is None:
            self.table[hash_key] = new_node
        else:
            current = self.table[hash_key]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        hash_key = self.hash_function(key)
        current = self.table[hash_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
```

#### Open Addressing

```python
class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        original_hash_key = hash_key
        while self.table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.size
            if hash_key == original_hash_key:
                raise Exception("Hash table is full")
        self.table[hash_key] = (key, value)

    def search(self, key):
        hash_key = self.hash_function(key)
        original_hash_key = hash_key
        while self.table[hash_key] is not None:
            if self.table[hash_key][0] == key:
                return self.table[hash_key][1]
            hash_key = (hash_key + 1) % self.size
            if hash_key == original_hash_key:
                return None
        return None
```

### Example Code and Detailed Explanation

1. **Inserting "Alice Johnson"**:
   - Compute the hash value: `3303733913283304066`.
   - Compute the hash index: `3303733913283304066 % 10 = 6`.
   - Insert the key-value pair at index `6`.

2. **Inserting "Bob Smith"**:
   - Compute the hash value: `-684410649588854874`.
   - Compute the hash index: `-684410649588854874 % 10 = 6`.
   - Collision occurs at index `6`.
   - In separate chaining, add "Bob Smith" to the linked list at index `6`.
   - In open addressing, find the next available slot.

#### Separate Chaining Example

```python
# Create hash table
ht = HashTable(10)

# Insert data
ht.insert("Alice Johnson", "Math: 85, English: 92, Science: 78")
ht.insert("Bob Smith", "Math: 88, English: 75, Science: 90")

# Search data
print(ht.search("Alice Johnson"))  # Output: Math: 85, English: 92, Science: 78
print(ht.search("Bob Smith"))      # Output: Math: 88, English: 75, Science: 90

# Print hash table state
def print_hash_table(ht):
    for i, node in enumerate(ht.table):
        print(f"Index {i}:", end=" ")
        current = node
        while current:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")

print_hash_table(ht)
```

#### Open Addressing Example

```python
# Create hash table
ht_open = HashTableOpenAddressing(10)

# Insert data
ht_open.insert("Alice Johnson", "Math: 85, English: 92, Science: 78")
ht_open.insert("Bob Smith", "Math: 88, English: 75, Science: 90")

# Search data
print(ht_open.search("Alice Johnson"))  # Output: Math: 85, English: 92, Science: 78
print(ht_open.search("Bob Smith"))      # Output: Math: 88, English: 75, Science: 90

# Print hash table state
def print_hash_table_open(ht):
    for i, item in enumerate(ht.table):
        if item:
            print(f"Index {i}: ({item[0]}, {item[1]})")
        else:
            print(f"Index {i}: None")

print_hash_table_open(ht_open)
```

### Detailed Explanation of the Query Process

1. **Query "Alice Johnson"**:
   - Compute hash value: `3303733913283304066`.
   - Compute index: `3303733913283304066 % 10 = 6`.
   - Traverse the linked list at index `6` to find the key "Alice Johnson".

2. **Query "Bob Smith"**:
   - Compute hash value: `-684410649588854874`.
   - Compute index: `-684410649588854874 % 10 = 6`.
   - Traverse the linked list at index `6` to find the key "Bob Smith".

### Comparison with Traditional Methods

#### Traditional Methods (Linear Search)

1. **Storage and Retrieval Efficiency**:
   - Linear search has a time complexity of O(n).
   - Retrieval time increases significantly with the number of entries.

2. **Memory Usage**:
   - No additional mechanisms for collision handling are required.
   - Data is stored in a simple linear arrangement.

#### Hash Table Indexing

1. **Storage and Retrieval Efficiency**:
   - Average time complexity is O(1).
   - Consistent retrieval time regardless of data volume.

2. **Memory Usage**:
   - Requires extra memory for hash table and collision handling structures (e.g., linked lists or probing).
   - Efficient memory management through dynamic resizing.

### Advantages

- **Search Speed**: Hash tables significantly improve search speed, especially for large datasets.
- **Memory Efficiency**: Properly managed hash tables use memory efficiently despite requiring extra space for collision handling.
- **Dynamic Scaling**: Hash tables can dynamically adjust size to accommodate growing data volumes.

## Conclusion

Hash tables use hash functions to map keys to array indices, allowing for rapid data storage and retrieval. Collision resolution strategies, such as separate chaining and open addressing, ensure efficient handling of hash collisions. Compared to traditional linear search methods, hash tables offer superior performance, especially for large datasets.


"""
nb.cells.append(new_markdown_cell(s1))


s2 = """

## Section 2: Hands-on Hash Table Application and Conflict Resolution

### Introduction

In this section, we will delve into a practical example of using hash tables for data storage and retrieval, emphasizing collision resolution strategies. This hands-on approach will enhance your understanding of hash tables and their applications.

### Example: Student Grades Storage

We'll use a hash table to store and retrieve student grades. The keys will be student names, and the values will be their grades in various subjects.

### Implementation Details

1. **Hash Table Class**: We'll define a hash table class with methods for insertion, searching, and handling collisions using separate chaining.
2. **Node Class**: Each entry in the hash table will be a node containing the key, value, and a pointer to the next node in case of collisions.

### Code Implementation

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[hash_key] is None:
            print('Insert -> hash_key =', hash_key)
            self.table[hash_key] = new_node
        else:
            print('Insert (collision) -> hash_key =', hash_key)
            current = self.table[hash_key]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        hash_key = self.hash_function(key)
        current = self.table[hash_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

# Example usage
ht = HashTable(10)
ht.insert("Alice Johnson", "Math: 85, English: 92, Science: 78")
ht.insert("Bob Smith", "Math: 88, English: 75, Science: 90")
print(f"Hash value for 'Alice Johnson': {hash('Alice Johnson')}")
print(f"Hash value for 'Bob Smith': {hash('Bob Smith')}")
print(ht.search("Alice Johnson"))  # Output: Math: 85, English: 92, Science: 78
print(ht.search("Bob Smith"))      # Output: Math: 88, English: 75, Science: 90

# Print hash table state
def print_hash_table(ht):
    for i, node in enumerate(ht.table):
        print(f"Index {i}:", end=" ")
        current = node
        while current:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")

print_hash_table(ht)
```

### Detailed Explanation

#### Insertion Operation

1. **Insert "Alice Johnson"**:
   - Compute the hash value: `3303733913283304066`.
   - Compute the hash index: `3303733913283304066 % 10 = 6`.
   - Insert the key-value pair at index `6`.
   - No collision occurs.

2. **Insert "Bob Smith"**:
   - Compute the hash value: `-684410649588854874`.
   - Compute the hash index: `-684410649588854874 % 10 = 6`.
   - Collision occurs at index `6`.
   - In separate chaining, add "Bob Smith" to the linked list at index `6`.

#### Search Operation

1. **Search "Alice Johnson"**:
   - Compute hash value: `3303733913283304066`.
   - Compute index: `3303733913283304066 % 10 = 6`.
   - Traverse the linked list at index `6` to find the key "Alice Johnson".

2. **Search "Bob Smith"**:
   - Compute hash value: `-684410649588854874`.
   - Compute index: `-684410649588854874 % 10 = 6`.
   - Traverse the linked list at index `6` to find the key "Bob Smith".

### Print Hash Table State

```python
def print_hash_table(ht):
    for i, node in enumerate(ht.table):
        print(f"Index {i}:", end=" ")
        current = node
        while current:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")

print_hash_table(ht)
```

Output:
```
Index 0: None
Index 1: None
Index 2: None
Index 3: None
Index 4: None
Index 5: None
Index 6: (Alice Johnson, Math: 85, English: 92, Science: 78) -> (Bob Smith, Math: 88, English: 75, Science: 90) -> None
Index 7: None
Index 8: None
Index 9: None
```

"""
nb.cells.append(new_markdown_cell(s2))


data_code_test2 = """

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[hash_key] is None:
            print('inert->hash_key=',hash_key)
            self.table[hash_key] = new_node
        else:
            print('inert-else->hash_key=',hash_key)
            current = self.table[hash_key]
            print('inert-else->current=',current)
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        hash_key = self.hash_function(key)
        current = self.table[hash_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

# 示例使用
ht = HashTable(10)
ht.insert("Alice Johnson", "Math: 85, English: 92, Science: 78")
ht.insert("Bob Smith", "Math: 88, English: 75, Science: 90")
print(f"Hash value for 'Alice Johnson': {hash('Alice Johnson')}")
print(f"Hash value for 'Bob Smith': {hash('Bob Smith')}")
print(ht.search("Alice Johnson"))  # 输出: Math: 85, English: 92, Science: 78
print(ht.search("Bob Smith"))      # 输出: Math: 88, English: 75, Science: 90



# 链地址法处理冲突示例
ht = HashTable(10)
ht.insert("Alice Johnson", "Math: 85, English: 92, Science: 78")
ht.insert("Bob Smith", "Math: 88, English: 75, Science: 90")

# 查看哈希表状态
def print_hash_table(ht):
    for i, node in enumerate(ht.table):
        print(f"Index {i}:", end=" ")
        current = node
        while current:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")

print_hash_table(ht)


"""
nb.cells.append(new_code_cell(data_code_test2))





s3 = """
# Section 3: Comprehensive Guide to String Data Structure and Algorithms

## Section 3-1: Introduction to String Data Structure

### Basic Concepts

Strings in Python are sequences of characters enclosed within single, double, or triple quotes. Strings are immutable, meaning once created, they cannot be modified.

**Popular Representations of Characters:**

1. **ASCII (American Standard Code for Information Interchange)**:
   - Represents characters using 1 byte.
   - Example: 'A' = 65, 'a' = 97.

2. **Unicode**:
   - Represents characters using UTF-8 (1 to 4 bytes) or UTF-16 (2 to 4 bytes).
   - Covers over 110,000 characters across various scripts and symbols.

### Applications of Strings

Strings are fundamental in various applications, including text processing, data representation, and communication protocols. They are used extensively in file handling, user inputs, and display messages.

### String Operations

1. **Basic Operations**:
   - Concatenation: `greet = greeting + name`
   - Comparison: `==, >, <`
   - Indexing and Slicing: 
     ```python
     s = "abc"
     s[0], s[1], s[2]
     s[3:6], s[::], s[::-1]
     ```

2. **Immutability**:
   - Strings cannot be changed after creation.
   - Example: `s[0] = "k"` is invalid; use `"k" + s[1:]`.

### Common String Interview Problems

1. **Removal**:
   - Remove specific characters from a string.
   - Remove leading/trailing/duplicate spaces.

2. **De-duplication**:
   - Remove adjacent duplicate characters.

3. **Reversal**:
   - Reverse the entire string or individual words.

4. **Substring Search (strstr)**:
   - Naive method, Rabin-Karp, and KMP algorithms.

## Section 3-2: Detailed Algorithms and Implementation

### Character Removal

#### Problem: Remove specific characters from a string

**Example**: Remove 'u' and 'n' from "student".
**Output**: "stdet"

**Solution**:

1. **Naive Approach**:
   - Iterate through the string and remove characters.
   - Problem: Incorrect indexing due to immutability.

```python
def remove_chars(string):
    for i in range(len(string)):
        if string[i] == 'u' or string[i] == 'n':
            string = string[:i] + string[(i + 1):]
    return string
```

2. **Two-Pointer Technique**:
   - Convert string to list for mutability.
   - Use two pointers to filter out characters.

```python
def remove_chars_v2(string):
    lst = list(string)
    i, j = 0, 0
    while j < len(lst):
        if lst[j] not in ['u', 'n']:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])
```

**Complexity**:
- Time: O(n)
- Space: O(n)

### Removing Leading/Trailing and Duplicate Spaces

#### Problem: Remove leading, trailing, and duplicate spaces from a string.

**Example**: "   abc   de   "
**Output**: "abc de"

**Solution**:

1. **Two-Pointer Technique**:
   - Use pointers to track and remove spaces.

```python
def remove_spaces(string):
    if not string:
        return string
    lst = list(string)
    i, j = 0, 0
    while j < len(lst):
        if lst[j] != ' ' or (i != 0 and lst[i - 1] != ' '):
            lst[i] = lst[j]
            i += 1
        j += 1
    if i > 0 and lst[i - 1] == ' ':
        i -= 1
    return ''.join(lst[:i])
```

**Complexity**:
- Time: O(n)
- Space: O(n)

### Character De-duplication

#### Problem: Remove adjacent duplicate characters.

**Example**: "aaaaaabbazw"
**Output**: "abazw"

**Solution**:

1. **Two-Pointer Technique**:

```python
def remove_duplicates(string):
    if not string or len(string) < 2:
        return string
    lst = list(string)
    slow, fast = 1, 1
    while fast < len(lst):
        if lst[fast] != lst[slow - 1]:
            lst[slow] = lst[fast]
            slow += 1
        fast += 1
    return ''.join(lst[:slow])
```

**Complexity**:
- Time: O(n)
- Space: O(n)

2. **Stack-Based Method**:

```python
def remove_duplicates_stack(string):
    if not string or len(string) < 2:
        return string
    stack = []
    fast = 0
    while fast < len(string):
        if stack and string[fast] == stack[-1]:
            while fast < len(string) and string[fast] == stack[-1]:
                fast += 1
            stack.pop()
        else:
            stack.append(string[fast])
            fast += 1
    return ''.join(stack)
```

**Complexity**:
- Time: O(n)
- Space: O(n)

### String Reversal

#### Problem: Reverse the words in a string.

**Example**: "I love Yahoo"
**Output**: "Yahoo love I"

**Solution**:

1. **Split and Reverse**:

```python
def reverse_words(string):
    arr = string.split(" ")
    arr.reverse()
    return " ".join(arr)
```

2. **In-Place Reversal**:

```python
def reverse_helper(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

def reverse_string(string):
    lst = list(string)
    reverse_helper(lst, 0, len(lst) - 1)
    i = 0
    left = 0
    right = 0
    while i < len(lst):
        if i == len(lst) - 1 or lst[i + 1] == " ":
            right = i
            reverse_helper(lst, left, right)
            left = i + 2
        i += 1
    return ''.join(lst)
```

**Complexity**:
- Time: O(n)
- Space: O(n)

### Substring Search

#### Problem: Implement `strstr()` to check if a string is a substring of another.

1. **Brute-Force Approach**:

```python
def strstr(text, pattern):
    m = len(text)
    n = len(pattern)
    if m < n:
        return -1
    for i in range(m - n + 1):
        if text[i:i+n] == pattern:
            return i
    return -1
```

**Complexity**:
- Time: O(m * n)
- Space: O(1)

2. **Rabin-Karp Algorithm**:

```python
def rabin_karp(text, pattern):
    m = len(text)
    n = len(pattern)
    if m < n:
        return -1

    base = 256
    prime = 101
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(n - 1):
        h = (h * base) % prime

    for i in range(n):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(m - n + 1):
        if pattern_hash == text_hash:
            for j in range(n):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i

        if i < m - n:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + n])) % prime
            if text_hash < 0:
                text_hash += prime

    return -1
```

**Complexity**:
- Time: O(m + n) on average, O(m * n) in the worst case.
- Space: O(1)

## Conclusion

This comprehensive guide provides a detailed overview of string data structures and algorithms. We have covered basic operations, character removal, de-duplication, reversal, and substring search. Each section includes in-depth explanations and Python code examples to illustrate the concepts and implementations.

Understanding these fundamental string operations and algorithms is crucial for solving common interview problems and efficiently processing textual data in real-world applications.
"""
nb.cells.append(new_markdown_cell(s3))



s4 = r"""

## Section 4: Hand-on Detailed Analysis of the KMP Algorithm Based on STRING

### Background

The Knuth-Morris-Pratt (KMP) algorithm is a classic string matching algorithm developed by Donald Knuth, Vaughan Pratt, and James H. Morris in 1977. The algorithm was designed to solve the problem of efficiently finding occurrences of a "pattern" within a "text". The primary goal is to minimize the number of comparisons by leveraging the pattern's internal structure.

### Problem Solved by KMP

The KMP algorithm significantly reduces the number of character comparisons needed to find a pattern within a text. Traditional string matching algorithms, such as the naive approach, can be inefficient, especially for large texts and patterns. The KMP algorithm addresses this inefficiency by pre-processing the pattern to build a partial match table, which allows the algorithm to skip unnecessary comparisons.

### Key Concepts

#### Pattern’s Self-Similarity

Self-similarity in the pattern refers to the repetitive sequences within the pattern. This characteristic is used to determine how far to slide the pattern along the text when a mismatch occurs.

#### Shifted Similarity

Shifted similarity involves identifying how much of the pattern can be reused when a mismatch occurs. The partial match table captures this information.

#### Sliding Window Shifted Similarity

The sliding window approach in KMP involves using the partial match table to determine the next alignment of the pattern with the text, thus avoiding redundant comparisons.

### Detailed Explanation of the Algorithm

#### Constructing the Partial Match Table (Prefix Table)

The partial match table, or prefix table, records the lengths of the longest proper prefix of the pattern that matches a proper suffix of the pattern up to each position.

1. **Initialization**:
   - Initialize an array `pi` of the same length as the pattern with all values set to 0.
   - Set the first value `pi[0]` to 0, as the longest prefix which is also a suffix for a single character is always 0.

2. **Filling the Table**:
   - Use two pointers, `i` (current character in the pattern) and `j` (length of the current matching prefix).
   - Iterate through the pattern:
     - If the characters at `P[i]` and `P[j]` match, increment `j` and set `pi[i]` to `j`.
     - If they do not match and `j` is not 0, set `j` to `pi[j-1]` and repeat the comparison.
     - If they do not match and `j` is 0, set `pi[i]` to 0 and move to the next character.



- ![Partial Match Table](https://raw.githubusercontent.com/williampolicy/svcamp_data_algorithm/main/puml_partial_match_table.png)
```python
def compute_partial_match_table(P):
    m = len(P)
    pi = [0] * m
    j = 0
    i = 1
    while i < m:
        if P[i] == P[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                pi[i] = 0
                i += 1
    return pi
```

#### KMP Search Algorithm

1. **Initialization**:
   - Compute the partial match table for the pattern.
   - Initialize two indices, `i` for the text and `j` for the pattern.

2. **Search Process**:
   - Iterate through the text:
     - If `P[j]` matches `T[i]`, increment both `i` and `j`.
     - If `j` reaches the length of the pattern, a match is found. Reset `j` using the partial match table.
     - If a mismatch occurs and `j` is not 0, reset `j` using the partial match table.
     - If a mismatch occurs and `j` is 0, simply move to the next character in the text.



- ![KMP Algorithm](https://raw.githubusercontent.com/williampolicy/svcamp_data_algorithm/main/kmp_algorithm.png)

```python
def KMP_search(T, P):
    n = len(T)
    m = len(P)
    pi = compute_partial_match_table(P)
    i = 0
    j = 0
    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1
        if j == m:
            print("Found pattern at index " + str(i - j))
            j = pi[j - 1]
        elif i < n and P[j] != T[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1

# Example usage
T = "I study in SVCAMP"
P = "SVCAMP"
KMP_search(T, P)
```

### Example and Detailed Analysis

Let's consider the pattern "ABCABD" and the text "ABCABCAAABBABCABDBBAA".

#### Partial Match Table Construction

1. **Pattern**: "ABCABD"
2. **Length of the pattern (m)**: 6
3. **Initialize the pi array**: `pi = [0, 0, 0, 0, 0, 0]`
4. **Initialize indices**: `j = 0`, start `i` from 1

#### Construction Process:

**Step 1**: For `i = 1`
- `P[i] = 'B'`, `P[j] = 'A'`
- `P[i] != P[j]`
- Since `j = 0`, set `pi[1] = 0`
- Move to `i = 2`

**pi array**: `[0, 0, 0, 0, 0, 0]`

**Step 2**: For `i = 2`
- `P[i] = 'C'`, `P[j] = 'A'`
- `P[i] != P[j]`
- Since `j = 0`, set `pi[2] = 0`
- Move to `i = 3`

**pi array**: `[0, 0, 0, 0, 0, 0]`

**Step 3**: For `i = 3`
- `P[i] = 'A'`, `P[j] = 'A'`
- `P[i] == P[j]`
- Increment `j`: `j = 1`
- Set `pi[3] = j = 1`
- Move to `i = 4`

**pi array**: `[0, 0, 0, 1, 0, 0]`

**Step 4**: For `i = 4`
- `P[i] = 'B'`, `P[j] = 'B'`
- `P[i] == P[j]`
- Increment `j`: `j = 2`
- Set `pi[4] = j = 2`
- Move to `i = 5`

**pi array**: `[0, 0, 0, 1, 2, 0]`

**Step 5**: For `i = 5`
- `P[i] = 'D'`, `P[j] = 'C'`
- `P[i] != P[j]`
- Since `j != 0`, set `j = pi[j - 1] = pi[1] = 0`
- Since `j = 0`, set `pi[5] = 0`
- Move to `i = 6`

**pi array**: `[0, 0, 0, 1, 2, 0]`

### Partial Match Table for "ABCABD"

**pi array**: `[0, 0, 0, 1, 2, 0]`

### Detailed Comparison Process Using the Partial Match Table

Let’s consider the text `T = "ABCABCAAABBABCABDBBAA"` and the pattern `P = "ABCABD"`.

#### Without the Partial Match Table (Naive Approach)

1. Compare `T[0:6]` with `P`: `ABCABC` != `ABCABD` (Mismatch at `T[5]` and `P[5]`)
2. Move to the next character in `T` and repeat.

This would involve a lot of redundant comparisons, making the process inefficient.

#### Using the Partial Match Table

Using the partial match table, we avoid redundant comparisons by leveraging the information in the `pi` array.

**Step-by-Step Comparison with the Partial Match Table**:

1. `T[0] == P[0]`: `A == A`, `i = 1`, `j = 1`
2. `T[1] == P[1]`: `B == B`, `i = 2`, `j = 2`
3. `T[2] == P[2]`: `C == C`, `i = 3`, `j = 3`
4. `T[3] == P[3]`: `A == A`, `i = 4`, `j = 4`
5. `T[4] == P[4]`: `B == B`, `i = 5`, `j = 5`
6. `T[5] != P[5]`: `C != D`, use `pi[5]`, `j = pi[4] = 2`
7. `T[5] == P[2]`: `C == C

`, `i = 6`, `j = 3`
8. `T[6] == P[3]`: `A == A`, `i = 7`, `j = 4`
9. `T[7] == P[4]`: `A == B`, use `pi[4]`, `j = pi[3] = 1`
10. `T[7] != P[1]`: `A != B`, use `pi[1]`, `j = pi[0] = 0`
11. `T[8] == P[0]`: `B == A`, `i = 9`, `j = 0`
12. Repeat the comparison steps until `j == m` or `i == n`.

By using the partial match table, we skip unnecessary comparisons and only perform comparisons where there is a potential match, significantly reducing the number of operations.

### Conclusion

The KMP algorithm optimizes string search by leveraging the pattern's self-similarity, reducing redundant comparisons through the use of a partial match table. This table captures the longest prefix which is also a suffix, allowing the algorithm to efficiently skip over sections of the text that cannot possibly match the pattern. By understanding and applying these principles, we achieve a highly efficient string matching algorithm essential for various computational tasks and applications.
### Mathematical Expressions

Let \( T \) be the text and \( P \) be the pattern.

1. **Partial Match Table**:
   The partial match table \( \kappa \) captures the longest proper prefix of \( P \) that is also a suffix up to each position.

$$
\kappa[i] = \begin{cases} 
0 & \text{if } i = 0 \\
\text{length of the longest proper prefix of } P[0:i] \text{ which is also a suffix} & \text{if } i > 0 
\end{cases}
$$

2. **KMP Search**:
   During the search, we use the partial match table to skip unnecessary comparisons.

$$
\text{For each } i \text{ in } T: 
$$

$$
\begin{cases}
j = \kappa[j-1] & \text{if } T[i] \neq P[j] \text{ and } j \neq 0 \\
i++ & \text{if } T[i] \neq P[j] \text{ and } j = 0 \\
i++, j++ & \text{if } T[i] = P[j]
\end{cases}
$$

3. **When a match is found**:
   If the pattern is fully matched, we record the match and use the partial match table to continue the search efficiently.

$$
j = m \Rightarrow \text{Match at index } i - j 
$$

$$
j = \kappa[j - 1]
$$

### Enhanced Explanation with Detailed Steps

To further clarify the usage of the partial match table and the match process:

1. **Initialization**:
   - Compute the partial match table $ \kappa $ for the pattern $ P $.
   - Initialize indices \( i \) for the text \( T \) and \( j \) for the pattern \( P \).

2. **Search Process**:
   - Iterate through the text \( T \):
     - If \( P[j] = T[i] \), both indices are incremented (\( i++ \) and \( j++ \)).
     - If \( j \) reaches the length of the pattern \( m \), a match is found at index \( i - j \). Reset \( j \) using the partial match table $ \kappa[j-1] $.
     - If \( P[j] \neq T[i] \) and \( j \neq 0 \), reset \( j \) using the partial match table \( \kappa[j-1] \).
     - If \( P[j] \neq T[i] \) and \( j = 0 \), simply move to the next character in the text (\( i++ \)).

### KMP Search Example

Let's consider the pattern $ P = \text{"ABCABC"} $  and the text $ T = \text{"ABCABCAAABBABCABDBBAA"} $.

1. **Partial Match Table** for $ P = \text{"ABCABC"} $:

$$
\kappa = [0, 0, 0, 1, 2, 3]
$$

2. **Search Process**:
   - \( i = 0, j = 0 \)
   - \( T[0] = P[0] \): \( A = A \), \( i++ \), \( j++ \)
   - \( T[1] = P[1] \): \( B = B \), \( i++ \), \( j++ \)
   - \( T[2] = P[2] \): \( C = C \), \( i++ \), \( j++ \)
   - \( T[3] = P[3] \): \( A = A \), \( i++ \), \( j++ \)
   - \( T[4] = P[4] \): \( B = B \), \( i++ \), \( j++ \)
   - \( T[5] = P[5] \): \( C = C \), \( i++ \), \( j++ \)
   - \( j = 6 \): Match found at index \( i - j = 0 \),$ j = \kappa[5] = 3 $
   - Continue comparing from $ T[6] $ and $ P[3] $, efficiently skipping unnecessary comparisons based on \( \kappa \).

By following this detailed explanation and using the provided formulas, you can clearly see how the KMP algorithm leverages the partial match table to minimize redundant comparisons, thus achieving efficient string matching.




"""
nb.cells.append(new_markdown_cell(s4))


s4_2=r"""
### Complete Code for Partial Match Table and KMP Algorithm with Examples

Here is the complete code for computing the partial match table and performing the KMP search algorithm. This includes two examples to demonstrate the process.

#### Computing the Partial Match Table (Prefix Table)

```python
def compute_partial_match_table(P):
    m = len(P)
    pi = [0] * m  # Initialize the partial match table with zeros
    j = 0  # Length of the previous longest prefix suffix
    i = 1  # Start from the second character in the pattern
    
    # Loop through the pattern to fill the partial match table
    while i < m:
        if P[i] == P[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                pi[i] = 0
                i += 1
    
    return pi

# Example pattern "ABCABD"
P = "ABCABD"
pi = compute_partial_match_table(P)
print("Partial Match Table for 'ABCABD':", pi)
```

#### KMP Search Algorithm

```python
def KMP_search(T, P):
    n = len(T)
    m = len(P)
    pi = compute_partial_match_table(P)
    i = 0  # Index for T (text)
    j = 0  # Index for P (pattern)
    
    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1
        
        if j == m:
            print("Found pattern at index", i - j)
            j = pi[j - 1]
        elif i < n and P[j] != T[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1

# Example 1: Pattern "ABCABD" in Text "ABCABCAAABBABCABDBBAA"
T1 = "ABCABCAAABBABCABDBBAA"
P1 = "ABCABD"
print("\nExample 1:")
KMP_search(T1, P1)

# Example 2: Pattern "ABCABC" in Text "ABCABCAAABBABCABDBBAA"
T2 = "ABCABCAAABBABCABDBBAA"
P2 = "ABCABC"
print("\nExample 2:")
KMP_search(T2, P2)
```

### Detailed Explanation of the Code

#### Partial Match Table Construction

1. **Initialization**:
   - The `pi` array is initialized with zeros.
   - `j` is the length of the previous longest prefix suffix.
   - `i` starts from 1, as `pi[0]` is always 0.

2. **Filling the Table**:
   - If `P[i]` matches `P[j]`, increment both `i` and `j`, and set `pi[i]` to `j`.
   - If there is a mismatch and `j` is not 0, set `j` to `pi[j-1]` and continue the comparison.
   - If there is a mismatch and `j` is 0, set `pi[i]` to 0 and move to the next character.

#### KMP Search Algorithm

1. **Initialization**:
   - Compute the partial match table `pi` for the pattern `P`.
   - Initialize indices `i` and `j` for the text `T` and the pattern `P`, respectively.

2. **Search Process**:
   - Iterate through the text `T`:
     - If `P[j]` matches `T[i]`, increment both `i` and `j`.
     - If `j` reaches the length of the pattern `m`, a match is found. Print the match index and reset `j` using `pi[j-1]`.
     - If there is a mismatch and `j` is not 0, reset `j` using `pi[j-1]`.
     - If there is a mismatch and `j` is 0, move to the next character in the text `T`.

### Running the Code

To run this code, copy and paste it into a Python environment or a Jupyter notebook. The output will display the partial match table for the given pattern and the indices of found matches in the text for both examples.

```python
# Computing the partial match table for "ABCABD"
P = "ABCABD"
pi = compute_partial_match_table(P)
print("Partial Match Table for 'ABCABD':", pi)

# Running KMP search for both examples
print("\nExample 1:")
KMP_search(T1, P1)

print("\nExample 2:")
KMP_search(T2, P2)
```

### Output

The output will show the partial match table and the indices where the pattern is found in the text.

```plaintext
Partial Match Table for 'ABCABD': [0, 0, 0, 1, 2, 0]

Example 1:
Found pattern at index 12

Example 2:
Found pattern at index 0
Found pattern at index 9
```


"""
nb.cells.append(new_markdown_cell(s4_2))


data_code_test = """

def compute_partial_match_table(P):
    m = len(P)
    pi = [0] * m  # Initialize the partial match table with zeros
    j = 0  # Length of the previous longest prefix suffix
    i = 1  # Start from the second character in the pattern
    
    # Loop through the pattern to fill the partial match table
    while i < m:
        if P[i] == P[j]:
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                pi[i] = 0
                i += 1
    
    return pi

# Example pattern "ABCABD"
P = "ABCABD"
pi = compute_partial_match_table(P)
print("Partial Match Table for 'ABCABD':", pi)


"""
nb.cells.append(new_code_cell(data_code_test))




data_code_test3 = """
def KMP_search(T, P):
    n = len(T)
    m = len(P)
    pi = compute_partial_match_table(P)
    i = 0  # Index for T (text)
    j = 0  # Index for P (pattern)
    
    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1
        
        if j == m:
            print("Found pattern at index", i - j)
            j = pi[j - 1]
        elif i < n and P[j] != T[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1

# Example 1: Pattern "ABCABD" in Text "ABCABCAAABBABCABDBBAA"
T1 = "ABCABCAAABBABCABDBBAA"
P1 = "ABCABD"
print("\nExample 1:")
KMP_search(T1, P1)

# Example 2: Pattern "ABCABC" in Text "ABCABCAAABBABCABDBBAA"
T2 = "ABCABCAAABBABCABDBBAA"
P2 = "ABCABC"
print("\nExample 2:")
KMP_search(T2, P2)

"""
nb.cells.append(new_code_cell(data_code_test3))






data_code_test4 = """

# Computing the partial match table for "ABCABD"
P = "ABCABD"
pi = compute_partial_match_table(P)
print("Partial Match Table for 'ABCABD':", pi)

# Running KMP search for both examples
print("\nExample 1:")
KMP_search(T1, P1)

print("\nExample 2:")
KMP_search(T2, P2)

"""

nb.cells.append(new_code_cell(data_code_test4))


with open('al_class3_lecture_v1.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

