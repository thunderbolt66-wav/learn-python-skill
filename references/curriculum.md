# Complete Python Curriculum Reference

Source: [CodeWithHarry - Ultimate Python Course (10h 54m)](https://youtu.be/UrsmFxEIp5k)

---

## Chapter 1: Modules, Comments & pip
- **Modules**: Pre-written code that can be imported to leverage existing functionality.
  - Built-in (standard library): `math`, `os`, `random`, `sys`, `time`
  - External: installed via `pip install <module_name>` (e.g., `pyjokes`, `pyttsx3`, `requests`)
- **Comments**:
  - Single-line: `# This is a comment`
  - Multi-line: `'''` or `"""` docstrings or blocks
- **REPL**: Read-Eval-Print Loop in terminal (`python`) for quick calculations and experimentation.

---

## Chapter 2: Variables and Data Types
- **Variables**: Named memory locations holding data.
- **Identifiers**: Rules — letters, digits, underscores; cannot start with a digit; case-sensitive.
- **Primary Data Types**:
  - `int`: 1, -5, 1000
  - `float`: 3.14, -0.001
  - `str`: "hello", 'world'
  - `bool`: `True`, `False`
  - `NoneType`: `None` (absence of a value)
- **Operators**:
  - Arithmetic: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent)
  - Assignment: `=`, `+=`, `-=`, `*=`, etc.
  - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - Logical: `and`, `or`, `not`
- **Typecasting & `input()`**:
  - `input()` always returns a `str`. To accept an integer: `a = int(input("Enter number: "))`.

---

## Chapter 3: Strings
- **Immutability**: Strings cannot be modified in-place.
- **Slicing**:
  - Syntax: `string[start:stop:step]`
  - Negative indexing: `string[-1]` is the last character.
  - Reverse string: `string[::-1]`.
- **Key Methods**:
  - `len()`, `endswith()`, `startswith()`, `count()`, `capitalize()`, `find()`, `replace()`
- **Escape Sequences**:
  - `\n` (newline), `\t` (tab), `\'` (single quote), `\\` (backslash).
  - Raw strings: `r"C:\new_folder"`.
- **f-strings**: `f"Hello, {name}! You scored {score:.2f}"`.

---

## Chapter 4: Lists and Tuples
- **Lists** (Mutable, ordered, heterogeneous):
  - Syntax: `friends = ["Apple", 5, 3.14, True]`
  - Methods: `.append(x)`, `.sort()`, `.reverse()`, `.insert(i, x)`, `.pop(i)`, `.remove(x)`
- **Tuples** (Immutable, ordered, hashable):
  - Syntax: `tup = (1, 2, 3)`
  - Single element tuple requires a comma: `a = (1,)` (not `(1)` which is an integer).
  - Methods: `.count(x)`, `.index(x)`.
  - Packing and Unpacking: `x, y, z = (10, 20, 30)`.

---

## Chapter 5: Dictionary & Sets
- **Dictionaries** (Key-Value, ordered in Python 3.7+, mutable, keys must be hashable):
  - Syntax: `marks = {"Harry": 99, "Rohan": 85}`
  - Methods: `.keys()`, `.values()`, `.items()`, `.get(key, default)`, `.update(new_dict)`, `.pop(key)`.
  - Difference between `d["key"]` (raises `KeyError` if missing) and `d.get("key")` (returns `None`).
- **Sets** (Unordered collection of unique, hashable elements, mutable):
  - Empty set creation: `s = set()` (not `{}` which creates an empty dict).
  - Methods: `.add(x)`, `.remove(x)` (raises KeyError if missing), `.discard(x)` (silent if missing), `.pop()`, `.clear()`.
  - Operations: `.union()`, `.intersection()`, `.difference()`.

---

## Chapter 6: Conditional Expressions
- **Structure**:
  ```python
  if condition1:
      # statements
  elif condition2:
      # statements
  else:
      # default
  ```
- **Ternary Operator**: `result = "Adult" if age >= 18 else "Minor"`.
- **In-keyword**: `if "item" in my_list: ...`.

---

## Chapter 7: Loops in Python
- **`while` loop**: Repeats while a boolean condition remains `True`.
- **`for` loop**: Iterates over sequences (lists, strings, tuples, dictionaries, `range`).
- **`range(start, stop, step)`**: Generates integer sequences up to `stop - 1`.
- **`for ... else`**: The `else` block executes ONLY if the loop finishes without hitting a `break`.
- **Control statements**:
  - `break`: Terminate loop immediately.
  - `continue`: Skip to the next iteration.
  - `pass`: Null statement, placeholder.

---

## Chapter 8: Functions & Recursion
- **Functions**:
  - Definition: `def greet(name="User"): ...`
  - Positional vs Keyword arguments.
  - Return statements: default return is `None`.
- **Recursion**:
  - Function calling itself.
  - Essential components: **Base Case** (termination condition) and **Recursive Step**.
  - Example: Factorial `fact(n) = 1 if n <= 1 else n * fact(n - 1)`.

---

## Chapter 9: File I/O
- **Modes**:
  - `'r'`: Read (default, throws error if file doesn't exist).
  - `'w'`: Write (overwrites or creates file).
  - `'a'`: Append (appends at end of file).
  - `'+'`: Update (read and write, e.g. `'r+'`, `'w+'`).
  - `'b'`: Binary mode (e.g. `'rb'`, `'wb'`).
- **Context Manager (`with`)**:
  - Automatically handles file closing even if exceptions occur:
    ```python
    with open("file.txt", "r") as f:
        content = f.read()
    ```
- **File methods**: `.read()`, `.readline()`, `.readlines()`, `.write()`, `.writelines()`.

---

## Chapter 10: Object Oriented Programming (OOP)
- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.
- **Attributes**:
  - Class Attribute: Shared across all instances.
  - Instance Attribute: Unique to each instance (overrides class attribute on lookup).
- **`self`**: Reference to the current instance of the class.
- **`__init__` constructor**: Dunder method executed automatically upon object instantiation.
- **`@staticmethod`**: Method that does not take `self` or `cls` parameter.

---

## Chapter 11: Inheritance & More on OOPs
- **Inheritance Types**:
  - Single: Child inherits from Parent.
  - Multiple: Child inherits from Parent1, Parent2.
  - Multilevel: Child inherits from Parent, GrandChild inherits from Child.
- **`super()`**: Calls parent class methods and constructors.
- **Class Methods & Static Methods**:
  - `@classmethod` with `cls` parameter to modify class-level state.
- **Property Decorators**:
  - `@property` (getter)
  - `@attr.setter` (setter)
- **Operator Overloading (Dunder Methods)**:
  - `__add__` (`+`), `__sub__` (`-`), `__mul__` (`*`), `__str__` (string representation), `__len__` (`len()`).

---

## Chapter 12: Advanced Python 1
- **Walrus Operator (`:=`)**: Assigns values to variables as part of a larger expression.
  ```python
  if (n := len(items)) > 3:
      print(f"List is too long: {n} items")
  ```
- **Type Hints**:
  ```python
  def greet(name: str) -> str:
      return f"Hello, {name}"
  ```
- **Match-Case (Python 3.10+)**: Structural pattern matching.
- **Dictionary Merge (`|`) & Update (`|=`)**: `merged = dict1 | dict2`.
- **Exception Handling**:
  - `try`, `except Exception as e`, `else` (runs if NO exception occurred), `finally` (ALWAYS runs).
  - Custom exceptions via `raise ValueError("Invalid value")`.
- **`enumerate()`**: Loops with index: `for idx, item in enumerate(my_list): ...`.
- **List Comprehensions**: `[x**2 for x in nums if x % 2 == 0]`.

---

## Chapter 13: Advanced Python 2
- **Virtual Environments**: Isolated environments (`python -m venv myenv`, `pip freeze > requirements.txt`).
- **Lambda Functions**: Anonymous inline functions: `square = lambda x: x * x`.
- **`str.join()`**: `", ".join(["a", "b", "c"]) -> "a, b, c"`.
- **Functional Programming**:
  - `map(func, iterable)`: Applies function to every element.
  - `filter(func, iterable)`: Filters elements where predicate returns `True`.
  - `reduce(func, iterable)` from `functools`: Cumulatively aggregates values.
