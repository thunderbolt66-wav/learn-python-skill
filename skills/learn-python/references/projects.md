# Milestone Projects Guide

The course includes 2 mini projects and 2 mega projects designed to reinforce programming fundamentals, data structures, OOP, OS interactions, and AI integration.

---

## Project 1: Snake, Water, Gun Game
**Video Timestamp**: `05:34:55`  
**Concept**: Conditional logic, mapping, random module, and game theory.

### Rules
- **Snake vs Water**: Snake drinks water -> Snake wins.
- **Water vs Gun**: Gun drowns in water -> Water wins.
- **Gun vs Snake**: Gun shoots snake -> Gun wins.

### Implementation
```python
import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
you_str = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

if you_str not in you_dict:
    print("Invalid choice!")
else:
    you = you_dict[you_str]
    print(f"You chose {reverse_dict[you]}\nComputer chose {reverse_dict[computer]}")

    if computer == you:
        print("It's a Draw!")
    else:
        # Mathematical shortcut: (computer - you) % 3
        # Or explicit logic:
        if (computer - you) == -1 or (computer - you) == 2:
            print("You Win!")
        else:
            print("You Lose!")
```

---

## Project 2: The Perfect Guess (Number Guessing Game)
**Video Timestamp**: `08:08:45`  
**Concept**: While loops, conditional evaluation, state management, File I/O for persistent high score.

### Rules
- The computer picks a random integer between 1 and 100.
- The player repeatedly guesses the number.
- The game tells the player "Higher number please" or "Lower number please" until the guess is correct.
- High score (lowest number of guesses) is recorded in `hiscore.txt`.

### Implementation
```python
import random

n = random.randint(1, 100)
guesses = 0
user_guess = -1

print("Welcome to The Perfect Guess Game!")

while user_guess != n:
    guesses += 1
    user_guess = int(input("Guess the number (1-100): "))
    if user_guess > n:
        print("Lower number please!")
    elif user_guess < n:
        print("Higher number please!")

print(f"You have guessed the number {n} correctly in {guesses} attempts!")

# High score persistence
try:
    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read().strip() or "999999")
except FileNotFoundError:
    hiscore = 999999

if guesses < hiscore:
    print(f"New High Score! Previous best: {hiscore}, Your score: {guesses}")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
```

---

## Mega Project 1: Jarvis Virtual Voice Assistant
**Video Timestamp**: `09:30:22`  
**Concept**: Audio I/O (`speech_recognition`, `pyttsx3`), web browser automation, API requests, AI responses.

### Dependencies
```bash
pip install speechrecognition pyttsx3 pyaudio requests
```

### Core Architecture
1. **TTS Engine (`speak`)**: Text-to-speech using SAPI5 (Windows) or espeak (Linux).
2. **STT Engine (`listen`)**: Microphone listener using Google Speech Recognition API.
3. **Command Parser**:
   - Web links: "open youtube", "open google", "open linkedin".
   - Music Player: Plays pre-mapped songs or YouTube streams.
   - News reader: Fetches live headlines via NewsAPI.
   - AI Brain: Queries OpenAI or Gemini API for general conversation.

### Implementation Skeleton
```python
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

engine = pyttsx3.init()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def process_command(c: str):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        speak(f"Playing {song}")
    elif "news" in c:
        # Example NewsAPI fetch
        speak("Fetching today's top headlines...")
    else:
        speak("I heard your request. Integrating with AI model for reply.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
                word = recognizer.recognize_google(audio)

                if "jarvis" in word.lower():
                    speak("Yes, sir?")
                    with sr.Microphone() as src:
                        audio = recognizer.listen(src, timeout=5, phrase_time_limit=6)
                        command = recognizer.recognize_google(audio)
                        print(f"User: {command}")
                        process_command(command)
        except Exception:
            continue
```

---

## Mega Project 2: AI AutoReply Bot
**Video Timestamp**: `10:17:56`  
**Concept**: Desktop GUI automation (`pyautogui`), clipboard access (`pyperclip`), LLM chat automation.

### Dependencies
```bash
pip install pyautogui pyperclip requests
```

### Core Workflow
1. Locate target application coordinates on screen (e.g. WhatsApp Web or Chat client).
2. Select text region, copy to clipboard (`pyperclip.paste()`).
3. Send extracted chat history to LLM (OpenAI, Gemini, or local Ollama).
4. Simulate keyboard input and click to send automated response.

### Implementation Pattern
```python
import pyautogui
import pyperclip
import time

def auto_reply(prompt: str) -> str:
    # Query Gemini or OpenAI
    return "This is an automated response from AI."

def run_bot():
    print("Auto-reply bot starting in 3 seconds. Focus your chat window...")
    time.sleep(3)
    
    # 1. Drag and copy chat
    pyautogui.moveTo(600, 250)
    pyautogui.dragTo(1200, 800, duration=1.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(600, 250)  # Deselect
    
    chat_text = pyperclip.paste()
    print("Captured message:", chat_text)
    
    # 2. Generate response
    reply = auto_reply(chat_text)
    
    # 3. Paste and send
    pyautogui.click(900, 950)  # Input box
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

if __name__ == "__main__":
    # run_bot()
    pass
```
