# 🐍 Learn Python — Agent Skill

> An interactive, comprehensive Python mentor and curriculum skill for AI coding assistants (Antigravity, Claude Code, Codex, Cursor, and Agent Skills hosts), modeled directly after **CodeWithHarry's** acclaimed 11-hour masterclass.

[![YouTube Video Banner](https://img.youtube.com/vi/UrsmFxEIp5k/maxresdefault.jpg)](https://youtu.be/UrsmFxEIp5k)

---

## 🌟 Credits & Acknowledgments

All curriculum content, practice sets, exercises, and milestone projects in this skill are adapted from the masterclass created by **Haris Ali Khan ([CodeWithHarry](https://www.codewithharry.com/))**:

- 📺 **Watch the Full Course on YouTube**: [Python Tutorial For Beginners in Hindi | Complete Python Course (10:53:54)](https://youtu.be/UrsmFxEIp5k)
- 💻 **Official Source Code Repository**: [CodeWithHarry/The-Ultimate-Python-Course](https://github.com/CodeWithHarry/The-Ultimate-Python-Course)
- 🌐 **Official Website & Handbooks**: [codewithharry.com/notes](https://www.codewithharry.com/notes/)
- 📄 **Ultimate Python Cheatsheet**: [codewithharry.com/blogpost/python-cheatsheet](https://www.codewithharry.com/blogpost/python-cheatsheet/)

Special thanks to **CodeWithHarry** for providing one of the most accessible, comprehensive, and practical programming curriculums available for beginners and experienced developers alike.

---

## 🚀 What is this Skill?

The `learn-python` skill equips your AI coding agent to become an active Python teacher, mentor, and curriculum navigator. Rather than just giving answers, the agent can:

1. **Teach Topics Step-by-Step**: Intuition first, followed by clean code snippets, common pitfalls, and quick practice drills.
2. **Assign & Evaluate Practice Sets**: Presents real problems from Chapters 1–13, evaluates user solutions, and provides hint ladders.
3. **Mentor Milestone Projects**: Guides the learner through 4 complete end-to-end Python applications with modular architectures.
4. **Code Review & Modernize**: Evaluates code against PEP 8, idiomatic patterns, and modern Python 3.10+ features (walrus operator `:=`, structural pattern matching, type hints).

---

## 📚 Curriculum & Timestamps

| Chapter | Topic | Timestamp | Highlights |
|---|---|---|---|
| **Ch 0** | What is Programming? | [`00:02:05`](https://youtu.be/UrsmFxEIp5k?t=125) | Interpreters, compilers, execution model |
| **Ch 1** | Modules, Comments & pip | [`00:09:41`](https://youtu.be/UrsmFxEIp5k?t=581) | Built-in vs external modules, pip, REPL, comments |
| **Ch 2** | Variables and Data Types | [`00:34:55`](https://youtu.be/UrsmFxEIp5k?t=2095) | Identifiers, data types, typecasting, `input()` |
| **Ch 3** | Strings & Slicing | [`01:15:57`](https://youtu.be/UrsmFxEIp5k?t=4557) | `[start:stop:step]`, string methods, escape sequences |
| **Ch 4** | Lists and Tuples | [`01:50:53`](https://youtu.be/UrsmFxEIp5k?t=6653) | Mutability vs Immutability, indexing, list/tuple methods |
| **Ch 5** | Dictionary & Sets | [`02:25:56`](https://youtu.be/UrsmFxEIp5k?t=8756) | Hashable keys, dict methods, set operations |
| **Ch 6** | Conditional Expressions | [`03:09:41`](https://youtu.be/UrsmFxEIp5k?t=11381) | `if`-`elif`-`else`, logical operators |
| **Ch 7** | Loops in Python | [`03:58:17`](https://youtu.be/UrsmFxEIp5k?t=14297) | `while`, `for`, `range()`, `for-else`, `break`/`continue`/`pass` |
| **Ch 8** | Functions & Recursion | [`04:50:53`](https://youtu.be/UrsmFxEIp5k?t=17453) | Arguments, default values, recursion base cases |
| **Project 1** | **Snake, Water, Gun Game** | [`05:34:55`](https://youtu.be/UrsmFxEIp5k?t=20095) | CLI choice game using random logic |
| **Ch 9** | File I/O | [`05:54:50`](https://youtu.be/UrsmFxEIp5k?t=21290) | `open()`, read/write/append modes, context manager `with` |
| **Ch 10** | OOP Fundamentals | [`06:42:22`](https://youtu.be/UrsmFxEIp5k?t=24142) | Classes, objects, `self`, `__init__`, static methods |
| **Ch 11** | Inheritance & OOPs | [`07:23:17`](https://youtu.be/UrsmFxEIp5k?t=26597) | Multilevel/multiple inheritance, `super()`, dunder methods |
| **Project 2** | **The Perfect Guess** | [`08:08:45`](https://youtu.be/UrsmFxEIp5k?t=29325) | Number guessing game with persistent high score (`hiscore.txt`) |
| **Ch 12** | Advanced Python 1 | [`08:15:38`](https://youtu.be/UrsmFxEIp5k?t=29738) | Walrus operator `:=`, type hints, match-case, `try-except-else-finally` |
| **Ch 13** | Advanced Python 2 | [`08:57:51`](https://youtu.be/UrsmFxEIp5k?t=32271) | Virtual environments, pip freeze, lambdas, map/filter/reduce |
| **Mega 1** | **Jarvis Virtual Assistant** | [`09:30:22`](https://youtu.be/UrsmFxEIp5k?t=34222) | Voice assistant (`speech_recognition`, `pyttsx3`, web automation, LLMs) |
| **Mega 2** | **AI AutoReply Bot** | [`10:17:56`](https://youtu.be/UrsmFxEIp5k?t=37076) | Desktop GUI automation (`pyautogui`, `pyperclip`, LLM chat responder) |

---

## 🛠️ Installation

### 1. Google Antigravity
Clone directly into your Antigravity skills directory:
```bash
git clone https://github.com/thunderbolt66-wav/learn-python-skill.git ~/.gemini/config/skills/learn-python
```

### 2. Claude Code
Install via git or copy into your project `.claude/skills` or `.agents/skills`:
```bash
git clone https://github.com/thunderbolt66-wav/learn-python-skill.git .agents/skills/learn-python
```

### 3. Codex / Agentskills.io
In your agent prompt:
```text
Use $skill-installer to install the learn-python skill from:
https://github.com/thunderbolt66-wav/learn-python-skill
```

---

## 💻 CLI Companion Helper

You can also run the bundled Python tutor script in your terminal to explore chapters and projects:

```bash
# Print the full course curriculum
python scripts/python_tutor.py --curriculum

# View a specific chapter's timestamp & details
python scripts/python_tutor.py --chapter 8

# View a project overview
python scripts/python_tutor.py --project 1
```

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).  
Original educational concepts and curriculum © [CodeWithHarry](https://www.codewithharry.com/).
