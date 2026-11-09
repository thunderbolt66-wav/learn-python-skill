---
name: learn-python
description: >-
  Comprehensive Python tutor and reference skill based on CodeWithHarry's Ultimate Python Course
  (10h 54m complete masterclass). Guides learners and developers from absolute zero to advanced
  modern Python, covering variables, strings, data structures, conditional logic, loops, functions,
  File I/O, OOP, inheritance, advanced Python 3.10+ (walrus, match-case, type hints), and 4 complete
  projects: Snake Water Gun, The Perfect Guess, Jarvis Voice Assistant, and AI AutoReply Bot.
license: MIT
metadata:
  source_video: "https://youtu.be/UrsmFxEIp5k"
  source_repo: "https://github.com/CodeWithHarry/The-Ultimate-Python-Course"
  author_credit: "CodeWithHarry (The Ultimate Python Course)"
---

# Learn Python Skill

An interactive, pedagogical programming guide and reference curriculum modeled after CodeWithHarry's comprehensive 11-hour Ultimate Python masterclass.

Use this skill when:
- The user wants to learn Python from scratch or master specific topics.
- The user asks for explanation, code examples, best practices, or exercises on any Python topic.
- The user wants to build one of the 4 milestone projects (Snake-Water-Gun, The Perfect Guess, Jarvis Voice Assistant, AI AutoReply Bot).
- The user wants practice problems, quizzes, or code review on their Python solutions.

---

## Curriculum Overview (13 Chapters + 4 Projects)

| Chapter | Topic | Key Concepts | Timestamp in Video |
|---|---|---|---|
| **Ch 0** | What is Programming? | Interpreters, compilers, why Python, execution model | `00:02:05` |
| **Ch 1** | Modules, Comments & pip | Built-in vs external modules, `pip install`, REPL, comments (`#`, `"""`) | `00:09:41` |
| **Ch 2** | Variables & Data Types | Identifiers, `int`, `float`, `str`, `bool`, `None`, operators, `type()`, `input()` | `00:34:55` |
| **Ch 3** | Strings | Slicing `[start:stop:step]`, negative indexing, string methods, escape sequences | `01:15:57` |
| **Ch 4** | Lists & Tuples | Mutability vs Immutability, indexing, list methods, tuple methods, packing/unpacking | `01:50:53` |
| **Ch 5** | Dictionary & Sets | Key-value pairs, hashability, dictionary methods, set theory, set operations | `02:25:56` |
| **Ch 6** | Conditional Expressions | `if`-`elif`-`else`, logical operators (`and`, `or`, `not`), nested conditions | `03:09:41` |
| **Ch 7** | Loops in Python | `while`, `for`, `range()`, `for-else`, `break`, `continue`, `pass` | `03:58:17` |
| **Ch 8** | Functions & Recursion | Arguments, return values, default parameters, base cases, recursion depth | `04:50:53` |
| **Project 1** | **Snake, Water, Gun Game** | Random choice, score matrix, CLI interactive game loop | `05:34:55` |
| **Ch 9** | File I/O | Reading, writing, appending, context manager (`with`), file pointer seek/tell | `05:54:50` |
| **Ch 10** | Object Oriented Programming | Class vs Instance attributes, `self`, `__init__`, static methods | `06:42:22` |
| **Ch 11** | Inheritance & Polymorphism | Single/Multiple/Multilevel inheritance, `super()`, `@classmethod`, `@property`, operator overloading | `07:23:17` |
| **Project 2** | **The Perfect Guess** | Number guessing game, high-score tracking via file persistence | `08:08:45` |
| **Ch 12** | Advanced Python 1 | Walrus operator `:=`, type hints, match-case, exception handling (`try-except-else-finally`), `enumerate` | `08:15:38` |
| **Ch 13** | Advanced Python 2 | Virtual environments, `pip freeze`, Lambda functions, `join`, `format`, `map`, `filter`, `reduce` | `08:57:51` |
| **Mega 1** | **Jarvis Voice Assistant** | `pyttsx3`, `speech_recognition`, web automation, news API, OpenAI/Gemini integration | `09:30:22` |
| **Mega 2** | **AI AutoReply Bot** | `pyautogui`, `pyperclip`, screen reading, automated LLM chat replies | `10:17:56` |

---

## Modes of Interaction

When interacting with the user, determine which mode best suits their need:

### 1. `Lesson Mode` (`explain`, `teach`, `learn`)
Explain concepts using the **CodeWithHarry pedagogical style**:
1. **Analogy / Intuition First**: Explain why the concept exists before showing the syntax.
2. **Minimal Working Example**: Short, clear script demonstrating the syntax.
3. **Common Pitfalls & Gotchas**: Highlight edge cases (e.g., mutable default arguments, tuple single element comma `(1,)`, dictionary key mutability).
4. **Interactive Practice Prompt**: Give the user a 2-minute coding challenge to reinforce learning.

### 2. `Practice Mode` (`practice`, `exercise`, `problems`)
Provide hands-on exercises from the course's Practice Sets:
- Consult [references/practice_sets.md](file:///C:/Users/ojasp/.gemini/config/skills/learn-python/references/practice_sets.md).
- Give problem statements without spoiling the answer.
- Provide progressive hints if the user struggles.
- Evaluate the user's code for correctness, time/space complexity, and idiomatic Python style.

### 3. `Project Mode` (`build`, `project`)
Guide the user through building one of the 4 milestone projects:
- Consult [references/projects.md](file:///C:/Users/ojasp/.gemini/config/skills/learn-python/references/projects.md).
- Break the project down into manageable steps:
  1. High-level architecture & rules
  2. Input / Output specification
  3. Core game / automation logic
  4. Edge cases & error handling
  5. Modern extensions (GUI with Tkinter/PyQt, Web with Streamlit/FastAPI, or AI enhancements)

### 4. `Code Review Mode` (`review`, `debug`, `optimize`)
When the user submits Python code:
- Check for syntax errors, logical bugs, and anti-patterns.
- Refactor using modern Python features (list comprehensions, f-strings, walrus operator, pattern matching).
- Ensure PEP 8 naming and formatting compliance.

---

## Detailed References

- Full Curriculum & Theory: [references/curriculum.md](file:///C:/Users/ojasp/.gemini/config/skills/learn-python/references/curriculum.md)
- Practice Problems & Solutions: [references/practice_sets.md](file:///C:/Users/ojasp/.gemini/config/skills/learn-python/references/practice_sets.md)
- Complete Project Guides: [references/projects.md](file:///C:/Users/ojasp/.gemini/config/skills/learn-python/references/projects.md)
