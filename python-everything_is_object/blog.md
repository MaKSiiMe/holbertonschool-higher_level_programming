# Python3: Mutable, Immutable and the Trap of Shared References

## Introduction

In Python, understanding the difference between **mutable** and **immutable** data types is essential, especially when dealing with function arguments. The behavior of Python variables can lead to unexpected results if we ignore how references are managed in memory.

Let’s break down the concepts of mutability, function argument passing, and common pitfalls encountered by Python developers.

## Immutable vs Mutable Types

### Immutable types
Immutable objects **cannot** be changed after they are created. Examples include:

- `int`
- `float`
- `str`
- `tuple`
- `bool`

```python
a = 5
b = a
b = 10
print(a)  # Output: 5
```

In this example, `a` remains `5` because integers are immutable. The assignment `b = 10` does **not** modify `a`.

### Mutable types
Mutable objects **can** be modified in place. Examples include:

- `list`
- `dict`
- `set`

```python
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # Output: [1, 2, 3, 4]
```

Both `list1` and `list2` refer to the **same** object in memory. Mutating `list2` also affects `list1`.

## Function Parameters and References

Python uses **pass-by-object-reference** (also known as **pass-by-assignment**). When an object is passed to a function, the **reference** is passed, not a copy.

### Example with mutable type:

```python
def add_item(my_list):
    my_list.append(4)

items = [1, 2, 3]
add_item(items)
print(items)  # Output: [1, 2, 3, 4]
```

Since `my_list` refers to the same object as `items`, the modification inside the function is **reflected outside**.

### Example with immutable type:

```python
def increment(x):
    x += 1

num = 5
increment(num)
print(num)  # Output: 5
```

Although `x` is incremented inside the function, it doesn’t affect `num` outside, because integers are immutable and a **new object** is created when `x += 1`.

## Pitfall: Unexpected Mutation

### Problematic function:

```python
def append_to_list(val, my_list=[]):
    my_list.append(val)
    return my_list
```

```python
print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] ❌ Unexpected!
```

Why? Because default arguments are evaluated only **once**, the list is shared between function calls.

### Corrected version:

```python
def append_to_list(val, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(val)
    return my_list
```

```python
print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2]
```

This ensures a **new list** is created for each call when no list is provided.

## Conclusion

Understanding **mutability** and **object references** is key to mastering Python’s behavior with variables and function arguments. Remember:

- Immutable objects behave like value types.
- Mutable objects behave like reference types.
- Be cautious with default arguments, especially mutable ones.

This knowledge will help you write safer, more predictable Python code, and avoid common traps related to shared references.
