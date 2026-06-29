# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game is a high/low concept. It will randomly generate a secret number and issues some number of guesses. The goal is to correctly guess the secret number within those guesses but also before running out of attempts. THe game will help by telling you whether your guess was too high or too low.
- [ ] Detail which bugs you found.
The hints were opposite, when guessing too high it would say go higher, and tell you to go lower when guessing too low. The new game button wasn't working.
- [ ] Explain what fixes you applied.
I changed the high/low logic for the function and it seems to properly indicate now. The new game button should also work.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select New Game if starting again.
2. Put a number in the bar and click on "Submit Guess"
3. Following the on screen hint, continue selecting numbers until you've run out of attempts/guessed correctly.
4. Once done, check the secret number by clicking on the dropdown bar.
5. Select New Game once again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
(.venv) (base) srihitapanati@Srihitas-Air ai110-module1show-gameglitchinvestigator-starter % PYTHONPATH=. pytest
====================================================== test session starts =======================================================
platform darwin -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/srihitapanati/Desktop/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                                                                                                                

tests/test_game_logic.py .....                                                                                             [100%]

======================================================= 5 passed in 0.02s ========================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
