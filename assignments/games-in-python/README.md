# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python that lets a player guess letters to reveal a hidden word before running out of attempts. Focus on clean game state, user-friendly prompts, and solid input validation.

## 🎓 Learning objectives

- Practice string and list manipulation in Python.
- Use loops and conditionals to control game flow.
- Work with sets for efficient membership checking (guessed letters).
- Read and validate user input.
- Apply randomness to pick game data.
- Design a simple, testable game state and display logic.

## ⏱ Estimated time

45–90 minutes depending on experience.

## ⚙️ Prerequisites

- Python 3.x installed
- Basic familiarity with Python syntax (variables, lists, functions, conditionals, loops)

## 📁 Files in this folder

- `starter-code.py` — starter script to complete or extend
- (optional) `data/words.txt` — a plain text word list (one word per line) if present

---

## 📝 Tasks

### 🛠️ Task 1 — Implement the Hangman game (required)

#### Description

Complete `starter-code.py` (or build your own script) so a player can play a full round of Hangman from the terminal.

#### Requirements

Completed program should:

- Randomly select a word from a predefined list (in-code list or `data/words.txt`).
- Prompt the player for single-letter guesses and validate the input.
- Display the current progress using underscores for unguessed letters (for example: `_ a _ _ m a n`).
- Track and display letters already guessed (both correct and incorrect).
- Limit incorrect guesses and show the number of remaining attempts.
- End with a clear message when the player wins (all letters revealed) or loses (no remaining attempts).


### 🛠️ Task 2 — (Optional) Add polish and improvements

#### Description

Add features that improve user experience or make the game more robust.

#### Suggestions

- Allow guessing the entire word as an alternative action.
- Add difficulty levels that adjust allowed attempts and/or filter the word list by length.
- Draw a simple ASCII-art hangman that progresses with each incorrect guess.
- Load a larger word list from `data/words.txt` and filter by difficulty.
- Add unit tests for helper functions (for example: display builder and input validator).

---

## ▶️ How to run

1. Open a terminal and navigate to this assignment folder:

```bash
cd assignments/games-in-python
```

2. Run the starter script with Python 3:

```bash
python3 starter-code.py
```

If your environment uses `python` for Python 3, run `python starter-code.py` instead.

---

## 💡 Starter tips and hints

- Keep a list of candidate words inside the script or load from `data/words.txt` if available.
- Use a set for guessed letters to allow fast membership checks and to avoid duplicates.
- Create a helper function to build the display string (replace unguessed letters with `_`).
- Validate input so only single alphabetical characters are accepted; ignore repeated guesses.
- Decrease remaining attempts only for incorrect *new* guesses.
- Print friendly, informative prompts and the game state after each guess.

---

## Example interaction

Player sees:

_ _ _ _ _

Player inputs: a

If 'a' is in the word, the display updates. If the guess is incorrect and new, remaining attempts decrease and the guessed letter list updates.

---

## ✅ Evaluation / success criteria

- Program runs without crashing and meets the required behavior in Task 1. (Pass)
- Repeated letters and repeated guesses are handled correctly. (Pass)
- Prompts and messages are clear and student-friendly. (Pass)

---

## ✨ Extensions (optional)

- Add difficulty levels and filter the word list by length.
- Implement ASCII-art hangman that draws progressively with wrong guesses.
- Allow full-word guesses and give appropriate feedback.
- Add unit tests for core helper functions: display builder and input validator.

---

## 📚 Help and resources

- Python `random.choice` for selecting a random word.
- Use `set` and string/list methods for efficient logic.
- Print intermediate state values while debugging (secret word, guessed letters, attempts left).

Good luck — have fun building the game! Keep the experience friendly and clear for other students who will use this assignment.
