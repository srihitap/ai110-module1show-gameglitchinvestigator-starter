# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
I noticed that the "New Game" button was broken, despite running out of attempts or guessing correctly, clicking the New Game button would not reset the progress.

Looking at the secret number, if I guessed too high, it would tell em to go higher and if I guessed to low it would tell me to go even lower. Sometimes it wouldn't give me any indication.

It also seems like the score isn't updated properly after each turn, fluctuating between negative numbers and positive numbers.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
  31|24  too low, go higher  "go lower"         none
  31|15  too low, go higher  "go lower"         none
|new game starts a new game  didn't start new   "must start new game"

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used ChatGPT, and Clause for my project. The AI was suggesting that I write my code in logic_utils ans it defined my checkguess function incorrectly for my test cases which were crashing. The underlying use was correct bu the suggestion was a wrong implementation. I verified this by running the test cases and checking the cause using ChatGPT until it worked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether the bug was fixed or not by running the program again and I saw whether the feature was fixed or not. For example, I opened the game and put guesses into the bar and checked whether it would tell me to go higher or lower properly and it told me to go correctly. The AI didn't help me understand the error/fix it but it designed some test cases using Claude. It added some code into my file.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I think I would explain Streamlit as like a picture, you take a picture and you can zoom in and out, and interact with that moment that was captured, but in real life, time might be moving and changes might be being made. In order to see what's happening newly, you'll have to run the code once again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I would like to continue using @ to add contect from now on because the AI seems to make better decisions that way. I would be more explicit with AI and not be lazy when I'm writing a prompt because the quality of the prompt changes the quality of the output. The project helped me understand how much simpler AI engineering can be compared to traditional code writing and makes a person much more efficient.