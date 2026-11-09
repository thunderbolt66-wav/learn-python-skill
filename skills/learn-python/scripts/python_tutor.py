#!/usr/bin/env python3
"""Interactive Python Tutor CLI companion for the learn-python skill."""

import argparse
import json
import sys

CHAPTERS = {
    0: ("Introduction & What is Programming?", "00:02:05"),
    1: ("Modules, Comments & pip", "00:09:41"),
    2: ("Variables and Data Types", "00:34:55"),
    3: ("Strings and Slicing", "01:15:57"),
    4: ("Lists and Tuples", "01:50:53"),
    5: ("Dictionary & Sets", "02:25:56"),
    6: ("Conditional Expressions", "03:09:41"),
    7: ("Loops in Python", "03:58:17"),
    8: ("Functions & Recursion", "04:50:53"),
    9: ("File Input/Output", "05:54:50"),
    10: ("Object Oriented Programming", "06:42:22"),
    11: ("Inheritance & Polymorphism", "07:23:17"),
    12: ("Advanced Python 1 (Walrus, Types, Exceptions)", "08:15:38"),
    13: ("Advanced Python 2 (Venvs, Lambdas, Functional)", "08:57:51"),
}

PROJECTS = {
    1: ("Snake, Water, Gun Game", "05:34:55", "CLI interactive choice game using random logic"),
    2: ("The Perfect Guess", "08:08:45", "Number guessing game with persistent high score"),
    3: ("Jarvis Voice Assistant", "09:30:22", "Voice-controlled virtual assistant (pyttsx3 + speech_recognition)"),
    4: ("AI AutoReply Bot", "10:17:56", "Screen OCR/automation chat responder (pyautogui + LLM)"),
}

def list_curriculum():
    print("=" * 65)
    print(" THE ULTIMATE PYTHON COURSE - CURRICULUM OVERVIEW")
    print(" Source: CodeWithHarry (10h 54m Masterclass)")
    print("=" * 65)
    for ch, (title, ts) in CHAPTERS.items():
        print(f"  [Ch {ch:02d}] {title:<42} ({ts})")
    print("-" * 65)
    print(" MILESTONE PROJECTS:")
    for pid, (title, ts, desc) in PROJECTS.items():
        print(f"  [Project {pid}] {title:<32} ({ts}) -> {desc}")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Python Tutor CLI Companion")
    parser.add_argument("--curriculum", action="store_true", help="Display full curriculum breakdown")
    parser.add_argument("--chapter", type=int, choices=range(0, 14), help="Show specific chapter details")
    parser.add_argument("--project", type=int, choices=range(1, 5), help="Show specific project details")
    
    args = parser.parse_args()
    if args.chapter is not None:
        title, ts = CHAPTERS[args.chapter]
        print(f"Chapter {args.chapter}: {title} (Video Timestamp: {ts})")
    elif args.project is not None:
        title, ts, desc = PROJECTS[args.project]
        print(f"Project {args.project}: {title} (Video Timestamp: {ts})\nDescription: {desc}")
    else:
        list_curriculum()

if __name__ == "__main__":
    main()
