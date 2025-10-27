# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## Learning objectives

- Practice working with strings, lists, and basic data structures.
- Use loops and conditionals to control game flow.
- Read user input and validate it.
- Apply random selection to choose game data.
- Design simple game state and display updates to users.

## Prerequisites

- Basic familiarity with Python (variables, lists, strings, functions).
- Python 3.x installed on your machine.

## Estimated time

About 45–90 minutes depending on experience.

## What you'll build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts. The game should display the current progress (e.g., _ a _ _ m a n), show letters already guessed, and track remaining attempts.

**Skills practiced:** string manipulation, loops, conditionals, list/set operations, user input handling, random selection.

## Requirements (must-haves)

Your game must:

- Randomly select a word from a predefined list.
- Prompt the player for single-letter guesses.
- Show current progress with unguessed letters as underscores (e.g., _ _ a _ _ ).
- Track and display letters the player has already guessed.
- Limit the number of incorrect guesses and show remaining attempts.
- End the game with a clear win or lose message.

## How to run

1. Open a terminal and navigate to this assignment folder:

   cd assignments/games-in-python

2. Run the starter script with Python 3:

   python3 starter-code.py

If your environment uses `python` for Python 3, use `python starter-code.py` instead.

## Starter tips and hints

- Keep a list of words in your program (or load from `data/words.txt` if provided).
- Use a set to track guessed letters and to check membership quickly.
- Build a helper function that returns the display string (with underscores) given the secret word and guessed letters.
- Validate input: accept only single alphabetical characters and ignore repeated guesses.
- Update the number of remaining attempts only for incorrect, new guesses.

## Example interaction

Player sees:

_ _ _ _ _

Player inputs: a

A correct guess updates the display if 'a' is in the word. Incorrect guesses reduce remaining attempts and add the letter to "guessed".

## Evaluation / success criteria

- Program runs without crashing and follows the requirements above. (Pass)
- Correct handling of repeated letters and repeated guesses. (Pass)
- Clear, user-friendly prompts and messages. (Pass)

## Extensions (optional)

Try one or more of these to deepen the challenge:

- Add difficulty levels that change the number of attempts or the word list.
- Implement a simple ASCII-art hangman that draws more of the figure on each incorrect guess.
- Allow players to guess the whole word.
- Load a larger word list from a text file and filter by word length for difficulty.
- Add unit tests for the helper functions (display builder, guess validation).

## Help and resources

If you get stuck, try:

- Printing intermediate values (secret word, guessed letters, attempts left) to debug game state.
- Writing small helper functions and testing them individually.
- Reviewing Python docs for `random.choice` and basic string/list methods.

Good luck — have fun building the game! Keep the user experience friendly and clear for other students trying this assignment.
