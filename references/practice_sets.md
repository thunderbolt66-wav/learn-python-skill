# Practice Sets & Problem Solving Reference

From [The Ultimate Python Course](https://github.com/CodeWithHarry/The-Ultimate-Python-Course)

---

## Chapter 1: Modules, Comments & pip
1. **Twinkle Twinkle**: Write a program to print "Twinkle Twinkle Little Star" poem formatted with line breaks.
2. **REPL Calculator**: Use Python REPL to calculate the 5 table (`5 * 1`, `5 * 2`, etc.).
3. **Module Install & Use**: Install an external module (e.g., `pyttsx3` or `pyjokes`) and execute it to speak text or tell a joke.
4. **Directory Listing**: Write a Python program to print the contents of a directory using the built-in `os` module (`os.listdir()`).
5. **Comment Labeling**: Add comments to explain each line of the directory listing program.

---

## Chapter 2: Variables & Data Types
1. **Sum of Two Numbers**: Write a program to add two numbers input by the user.
2. **Remainder Calculation**: Find remainder when a number is divided by `z` (`num % z`).
3. **Check Input Type**: Check the type of variable assigned using `input()`.
4. **Comparison**: Use comparison operator to find out whether a given variable `a` is greater than `b`.
5. **Average**: Find the average of two numbers entered by the user.
6. **Square of a Number**: Calculate the square of a number entered by the user (`a ** 2` or `a * a`).

---

## Chapter 3: Strings
1. **User Greeting**: Display user-entered name followed by `"Good Afternoon"` using `f-string`.
2. **Template Letter Filler**:
   ```python
   letter = '''Dear <|Name|>,
   You are selected!
   <|Date|>'''
   ```
   Replace placeholders `<|Name|>` and `<|Date|>` with real values using `.replace()`.
3. **Double Space Detection**: Detect double space `"  "` in a string using `.find()`.
4. **Double Space Replacement**: Replace double spaces with single space.
5. **Escape Sequence Formatting**: Format string with appropriate `\n` and `\t` escape characters.

---

## Chapter 4: Lists & Tuples
1. **Store Fruits**: Store seven fruits in a list entered by the user.
2. **Student Marks Sorting**: Accept marks of 6 students and display them in sorted order (`marks.sort()`).
3. **Tuple Immutability Check**: Verify that a tuple cannot be modified (attempt `t[0] = x` and observe `TypeError`).
4. **List Sum**: Sum a list of 4 numbers without using `sum()` (or with `sum()`).
5. **Count Zeros**: Count number of zeros in a tuple `a = (7, 0, 8, 0, 0, 9)` using `a.count(0)`.

---

## Chapter 5: Dictionary & Sets
1. **Hindi-to-English Translation Dictionary**: Create a dictionary of Hindi words with values as their English translation. Provide user an option to look it up.
2. **Unique Numbers Input**: Input eight numbers from the user and display all unique numbers using a `set`.
3. **Type Mixing in Sets**: Can we have a set with `18` (int) and `'18'` (str) as values in it? (Yes, types differ).
4. **Length of Set**: What will be the length of `s = set()`; `s.add(20)`; `s.add(20.0)`; `s.add('20')`? (`20 == 20.0` evaluates to `True`, so length is 2!).
5. **Empty Set Type**: What is the type of `s = {}`? (Dictionary, not set!).
6. **Favorite Languages Dict**: Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use their names as keys.

---

## Chapter 6: Conditional Expressions
1. **Greatest of Four**: Find the greatest of four numbers entered by the user.
2. **Pass or Fail**: Check whether a student has passed (requires minimum 40% overall and at least 33% in each of 3 subjects).
3. **Spam Detection**: Detect spam comments containing phrases: `"make a lot of money"`, `"buy now"`, `"subscribe this"`, `"click this"`.
4. **Username Length**: Check whether a given username contains less than 10 characters.
5. **Name in List**: Find out whether a given name is present in a list of registered users.
6. **Grade Calculator**: Calculate student grade (90-100: Ex, 80-90: A, 70-80: B, 60-70: C, 50-60: D, <50: F).

---

## Chapter 7: Loops in Python
1. **Multiplication Table**: Print multiplication table of a given number using `for` loop.
2. **Greet Names**: Greet all person names stored in a list `l = ["Harry", "Soham", "Sachin", "Rahul"]` that start with `'S'`.
3. **Multiplication Table via `while`**: Print multiplication table using `while` loop.
4. **Prime Number Checker**: Check if a given number is prime.
5. **Sum of First N Natural Numbers**: Calculate sum using `while` loop.
6. **Factorial**: Calculate factorial of a given number using `for` loop.
7. **Star Pattern 1 (Pyramid)**:
   ```text
     *
    ***
   *****
   ```
8. **Star Pattern 2 (Right Triangle)**:
   ```text
   *
   **
   ***
   ```
9. **Star Pattern 3 (Hollow Square)**:
   ```text
   ***
   * *
   ***
   ```
10. **Reversed Multiplication Table**: Print table in reverse order (`10` down to `1`).

---

## Chapter 8: Functions & Recursion
1. **Greatest of Three**: Function to find greatest of three numbers.
2. **Celsius to Fahrenheit**: Function to convert Celsius to Fahrenheit: `(c * 9/5) + 32`.
3. **Prevent Print Newline**: How do you prevent Python `print()` function to print a new line at the end? (`print("text", end="")`).
4. **Recursive Sum**: Recursive function to calculate the sum of first `n` natural numbers.
5. **Recursive Pattern**: Recursive function to print first `n` lines of inverted pyramid:
   ```text
   ***
   **
   *
   ```
6. **Inches to Centimeters**: Function to convert inches to cm (`inches * 2.54`).
7. **Strip & Remove Word**: Function to remove a given word from a list and strip it at the same time.
8. **Table Function**: Function to print multiplication table of a number.

---

## Chapter 9: File I/O
1. **Poem Word Search**: Read `poem.txt` and check if it contains the word `"twinkle"`.
2. **High Score Tracker**: `game()` function generates random score. Check `hiscore.txt`; if current score > hiscore, update file.
3. **Generate Tables (2-20)**: Generate multiplication tables from 2 to 20 and write them to individual files (`tables/table_2.txt` ...).
4. **Word Censor**: Replace offensive word `"Donkey"` with `"#####"` in a file.
5. **List of Words Censor**: Replace a list of offensive words with `"#####"`.
6. **Log File Search**: Check if `log.txt` contains `"python"`.
7. **Line Number in Log**: Find out the exact line number where `"python"` is present.
8. **File Copy**: Make a copy of a text file (`this.txt` to `this_copy.txt`).
9. **File Identical Check**: Check whether two files have identical contents.
10. **Wipe File Contents**: Wipe out the content of a file using Python.
11. **Rename File**: Rename `old.txt` to `renamed_by_python.txt`.

---

## Chapter 10: Object Oriented Programming
1. **Programmer Class**: Store information of programmers working at Microsoft (name, salary, pin).
2. **Calculator Class**: Capable of finding square, cube, and square root of a number.
3. **Class vs Instance Attribute Conflict**: Create class attribute `a = 0`; change `obj.a = 1`; verify class attribute unchanged.
4. **Static Greet Method**: Add `@staticmethod` `greet()` to calculator class.
5. **Train Booking System**: Class `Train` with methods to `book_ticket()`, `get_status()`, and `get_fare_info()`.
6. **Can `self` be renamed?**: What happens if `self` is named `harry` or `slf`? (It works, but violates PEP 8 convention).

---

## Chapter 11: Inheritance & More on OOPs
1. **2D and 3D Vectors**: Create class `C2dVec` and use inheritance to create `C3dVec`.
2. **Pets and Dogs**: Class `Animals`, class `Pets` derived from Animals, and class `Dog` derived from Pets. Add `bark()` method.
3. **Employee Salary & Increment**: Class `Employee` with attributes `salary` and `increment`. Use `@property` decorator for `salaryAfterIncrement` and `@salaryAfterIncrement.setter`.
4. **Complex Numbers**: Class `Complex` to represent complex numbers, with overloaded `+` (`__add__`) and `*` (`__mul__`).
5. **Vector Dimensions & Operations**: Class `Vector` with `__add__` and `__mul__` for dot product.
6. **Vector `__str__`**: Vector string representation `7i + 8j + 10k`.
7. **Vector Dimension Check**: Override `__len__` to display vector dimensions.

---

## Chapter 12: Advanced Python 1
1. **File Opening Graceful Exit**: Open three files (`1.txt`, `2.txt`, `3.txt`). If any file is missing, handle with `try-except` without crashing.
2. **Third, Fifth, Seventh Element**: Print 3rd, 5th, and 7th elements from a list using `enumerate()`.
3. **List Comprehension Multiplication Table**: Create multiplication table using list comprehension: `[num * i for i in range(1, 11)]`.
4. **Division Zero Handling**: Program to divide `a` by `b`. Catch `ZeroDivisionError` and print friendly message.
5. **Table File Output via Comprehension**: Store multiplication tables in `tables.txt`.

---

## Chapter 13: Advanced Python 2
1. **Virtual Environment Setup**: Create `myenv1` and `myenv2`, install different library versions, export `pip freeze > requirements.txt`.
2. **String Formatting**: Format string using `.format()` or f-strings: `"The name of the student is {}, his marks are {} and phone number is {}"`.
3. **Filter Divisible by 5**: Filter list of integers to retain only numbers divisible by 5 using `filter()` and lambda.
4. **Reduce Max Number**: Find maximum element in a list using `functools.reduce()`.
5. **Flask/Web Server**: Run a minimal web server using Flask/FastAPI to serve Python content.
