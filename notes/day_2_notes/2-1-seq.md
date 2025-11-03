### Common Sequence Operations

Python provides several built-in operations that work across sequence types such as lists, tuples, and strings. These operations allow for flexible and efficient manipulation and querying of sequence data.

#### 1. Indexing
- Access individual elements using square brackets: `seq[index]`
- Supports negative indices for reverse access: `seq[-1]` (last element)

#### 2. Slicing
- Extract sub-sequences: `seq[start:stop]`
- Optional step: `seq[start:stop:step]`
- Works with lists, tuples, and strings

#### 3. Concatenation
- Combine sequences of the same type: `seq1 + seq2`
- Example: `[1, 2] + [3, 4]` results in `[1, 2, 3, 4]`

#### 4. Repetition
- Repeat sequences: `seq * n`
- Example: `[1, 2] * 3` results in `[1, 2, 1, 2, 1, 2]`

#### 5. Membership Testing
- Check if an element exists: `element in seq`, `element not in seq`
- Example: `3 in [1, 2, 3]` returns `True`

#### 6. Length, Min, Max
- `len(seq)` returns the number of elements
- `min(seq)` and `max(seq)` return the smallest and largest elements

#### 7. Iteration
- Loop through elements using `for` loops:
    ```python
    for item in seq:
            print(item)
    ```

#### 8. Sorting and Reversing
- `sorted(seq)` returns a new sorted list
- `reversed(seq)` returns an iterator for reversed sequence

#### 9. Counting and Indexing (Lists, Tuples, Strings)
- `seq.count(value)` returns the number of occurrences
- `seq.index(value)` returns the first index of value

#### 10. Conversion Between Sequence Types
- `list(seq)`, `tuple(seq)`, `set(seq)` convert between types

These operations form the foundation for working with sequences in Python, enabling efficient data access, transformation, and analysis.

```
```


### Manipulation of Lists

Lists are mutable sequences in Python, allowing dynamic modification of their contents. Here are common operations and methods for manipulating lists:

#### 1. Adding Elements
- **Append:** Adds a single element to the end: `list.append(item)`
- **Extend:** Adds all elements from another iterable: `list.extend([item1, item2])`
- **Insert:** Inserts an element at a specific index: `list.insert(index, item)`

#### 2. Removing Elements
- **Remove:** Removes the first occurrence of a value: `list.remove(item)`
- **Pop:** Removes and returns element at index (default last): `list.pop([index])`
- **Clear:** Removes all elements: `list.clear()`

#### 3. Updating Elements
- Assign new value to an index: `list[index] = new_value`
- Update multiple elements via slicing: `list[start:stop] = [new_values]`

#### 4. Sorting and Reversing
- **Sort in place:** `list.sort()` (optional `reverse=True`, `key=func`)
- **Reverse in place:** `list.reverse()`
- **Get sorted copy:** `sorted(list)`

#### 5. Searching
- **Index:** Find position of value: `list.index(value)`
- **Count:** Number of occurrences: `list.count(value)`

#### 6. Copying Lists
- **Shallow copy:** `list.copy()` or `list[:]`
- **Deep copy:** Use `copy.deepcopy(list)` for nested lists

#### 7. List Comprehensions
- Create new lists using expressions: `[expression for item in iterable if condition]`
    ```python
    squares = [x**2 for x in range(10)]
    ```

#### 8. Nested Lists
- Lists can contain other lists (multi-dimensional): `matrix = [[1,2], [3,4]]`
- Access nested elements: `matrix[0][1]`

#### 9. Deleting Elements
- **del statement:** Remove by index or slice: `del list[index]` or `del list[start:stop]`

#### 10. Other Useful Methods
- **Copy:** `list.copy()`
- **Reverse:** `list.reverse()`
- **Sort:** `list.sort()`

Lists are versatile and widely used for storing ordered, mutable collections of items. Their rich set of methods makes them suitable for a variety of data manipulation tasks.

```
```

### Manipulation of Tuples

Tuples are immutable sequences in Python, meaning their contents cannot be changed after creation. However, several operations and techniques allow for effective use and manipulation of tuples:

#### 1. Creating Tuples
- Use parentheses: `t = (1, 2, 3)`
- Single-element tuple: `t = (1,)` (note the comma)
- Tuple packing/unpacking: `a, b = (1, 2)`

#### 2. Accessing Elements
- Indexing: `t[index]`
- Slicing: `t[start:stop]`
- Negative indices supported

#### 3. Iteration
- Loop through elements:
    ```python
    for item in t:
        print(item)
    ```

#### 4. Concatenation and Repetition
- Concatenate tuples: `t1 + t2`
- Repeat tuples: `t * n`

#### 5. Membership Testing
- Check existence: `value in t`, `value not in t`

#### 6. Counting and Indexing
- `t.count(value)` returns number of occurrences
- `t.index(value)` returns first index of value

#### 7. Conversion
- Convert tuple to list for mutability: `list(t)`
- Convert list to tuple: `tuple(lst)`

#### 8. Nested Tuples
- Tuples can contain other tuples: `nested = ((1, 2), (3, 4))`
- Access nested elements: `nested[0][1]`

#### 9. Tuple Unpacking
- Assign elements to variables: `a, b, c = t`
- Extended unpacking: `a, *rest = t`

#### 10. Immutability
- Tuples cannot be changed directly; to "modify," convert to a list, change, then convert back.

Tuples are useful for fixed collections of items, such as representing records, and are often used for returning multiple values from functions.

```
```


### Manipulation of Sets

Sets are unordered collections of unique, immutable elements in Python. They are useful for membership testing, removing duplicates, and performing mathematical set operations.

#### 1. Creating Sets
- Use curly braces: `s = {1, 2, 3}`
- Use the `set()` constructor: `s = set([1, 2, 3])`
- Empty set: `s = set()` (not `{}`; `{}` creates a dict)

#### 2. Adding Elements
- **Add single element:** `s.add(element)`
- **Update with multiple elements:** `s.update([elem1, elem2])` or `s.update(other_set)`

#### 3. Removing Elements
- **Remove specific element:** `s.remove(element)` (raises error if not found)
- **Discard element:** `s.discard(element)` (no error if not found)
- **Pop element:** `s.pop()` (removes and returns an arbitrary element)
- **Clear all elements:** `s.clear()`

#### 4. Set Operations
- **Union:** `s1 | s2` or `s1.union(s2)` (all elements from both sets)
- **Intersection:** `s1 & s2` or `s1.intersection(s2)` (common elements)
- **Difference:** `s1 - s2` or `s1.difference(s2)` (elements in `s1` not in `s2`)
- **Symmetric Difference:** `s1 ^ s2` or `s1.symmetric_difference(s2)` (elements in either set, but not both)

#### 5. Membership Testing
- Check if element exists: `element in s`, `element not in s`

#### 6. Set Relations
- **Subset:** `s1 <= s2` or `s1.issubset(s2)`
- **Superset:** `s1 >= s2` or `s1.issuperset(s2)`
- **Disjoint:** `s1.isdisjoint(s2)`

#### 7. Iteration
- Loop through elements:
    ```python
    for item in s:
        print(item)
    ```

#### 8. Copying Sets
- **Shallow copy:** `s.copy()`
- **Deep copy:** Use `copy.deepcopy(s)` for sets containing mutable objects

#### 9. Immutable Sets
- **frozenset:** Immutable version of a set: `fs = frozenset([1, 2, 3])`
- Supports all set operations except modification

#### 10. Applications
- Removing duplicates from sequences: `set([1, 2, 2, 3])`
- Fast membership testing
- Mathematical set operations

Sets are ideal for storing unique items and performing efficient set algebra. Their methods and operations make them powerful tools for data analysis and manipulation.

```
```

### Manipulation of Dictionaries

Dictionaries are mutable, unordered collections of key-value pairs in Python. They allow efficient retrieval, insertion, and deletion of values based on unique keys.

#### 1. Creating Dictionaries
- **Literal syntax:** `d = {'a': 1, 'b': 2}`
- **Constructor:** `d = dict(a=1, b=2)`
- **From sequences:** `d = dict([('a', 1), ('b', 2)])`
- **Empty dictionary:** `d = {}`

#### 2. Accessing Values
- **By key:** `d[key]`
- **Get with default:** `d.get(key, default)`
- **Keys must be immutable (e.g., strings, numbers, tuples)**

#### 3. Adding and Updating Entries
- **Assign value:** `d[key] = value`
- **Update multiple:** `d.update({'c': 3, 'd': 4})`
- **Setdefault:** `d.setdefault(key, default)` (sets and returns value if key not present)

#### 4. Removing Entries
- **Delete by key:** `del d[key]`
- **Pop by key:** `d.pop(key)` (returns value, raises error if key not found)
- **Pop with default:** `d.pop(key, default)`
- **Pop arbitrary item:** `d.popitem()` (returns `(key, value)`, raises error if empty)
- **Clear all:** `d.clear()`

#### 5. Iteration
- **Keys:** `for key in d:`
- **Values:** `for value in d.values():`
- **Items:** `for key, value in d.items():`

#### 6. Dictionary Views
- **Keys view:** `d.keys()`
- **Values view:** `d.values()`
- **Items view:** `d.items()`
- Views reflect changes to the dictionary

#### 7. Membership Testing
- **Key existence:** `key in d`, `key not in d`
- **Value existence:** `value in d.values()`

#### 8. Copying Dictionaries
- **Shallow copy:** `d.copy()`
- **Deep copy:** `copy.deepcopy(d)` (for nested dictionaries)

#### 9. Dictionary Comprehensions
- Create new dictionaries using expressions:
    ```python
    squares = {x: x**2 for x in range(5)}
    ```

#### 10. Nested Dictionaries
- Dictionaries can contain other dictionaries:
    ```python
    data = {'user': {'name': 'Alice', 'age': 30}}
    ```
- Access nested values: `data['user']['name']`

#### 11. Useful Methods
- **get:** `d.get(key, default)`
- **setdefault:** `d.setdefault(key, default)`
- **update:** `d.update(other_dict)`
- **fromkeys:** `dict.fromkeys(seq, value)` (creates new dict from keys)

#### 12. Dictionary Ordering
- As of Python 3.7+, dictionaries preserve insertion order

#### 13. Applications
- Fast key-based lookup
- Storing structured data
- Counting occurrences (with `collections.Counter`)
- Grouping data

Dictionaries are essential for mapping relationships and organizing data efficiently. Their flexible structure and rich set of methods make them a core data type in Python.

```
```
### Python Sequence & Collection Types Cheat Sheet

#### Common Sequence Operations
- **Indexing:** `seq[index]`, negative indices supported
- **Slicing:** `seq[start:stop:step]`
- **Concatenation:** `seq1 + seq2`
- **Repetition:** `seq * n`
- **Membership:** `element in seq`
- **Length/Min/Max:** `len(seq)`, `min(seq)`, `max(seq)`
- **Iteration:** `for item in seq:`
- **Sorting/Reversing:** `sorted(seq)`, `reversed(seq)`
- **Counting/Indexing:** `seq.count(value)`, `seq.index(value)`
- **Type Conversion:** `list(seq)`, `tuple(seq)`, `set(seq)`

#### Lists
- **Mutable, ordered**
- Add: `append`, `extend`, `insert`
- Remove: `remove`, `pop`, `clear`, `del`
- Update: `list[index] = value`, slicing
- Sort/Reverse: `sort`, `reverse`
- Copy: `copy`, slicing, `copy.deepcopy`
- Comprehensions: `[expr for item in iterable if cond]`
- Nested: `matrix = [[...], [...]]`

#### Tuples
- **Immutable, ordered**
- Create: `(1, 2, 3)`, `(1,)`
- Access: indexing, slicing
- Concatenate/Repeat: `t1 + t2`, `t * n`
- Count/Index: `count`, `index`
- Unpack: `a, b = t`, `a, *rest = t`
- Convert: `list(t)`, `tuple(list)`
- Nested: `((1,2), (3,4))`

#### Sets
- **Mutable, unordered, unique elements**
- Create: `{1,2,3}`, `set([1,2,3])`
- Add: `add`, `update`
- Remove: `remove`, `discard`, `pop`, `clear`
- Operations: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric diff)
- Relations: `<=`, `>=`, `isdisjoint`
- Membership: `in`, `not in`
- Copy: `copy`, `copy.deepcopy`
- Immutable: `frozenset([...])`

#### Dictionaries
- **Mutable, unordered, key-value pairs**
- Create: `{'a': 1}`, `dict(a=1)`, `dict([('a',1)])`
- Access: `d[key]`, `d.get(key, default)`
- Add/Update: `d[key]=value`, `update`, `setdefault`
- Remove: `del`, `pop`, `popitem`, `clear`
- Iteration: `for key in d`, `for value in d.values()`, `for k,v in d.items()`
- Views: `keys()`, `values()`, `items()`
- Copy: `copy`, `copy.deepcopy`
- Comprehensions: `{k: v for ...}`
- Nested: `d = {'user': {'name': ...}}`
- Ordering: Preserves insertion order (Python 3.7+)

---