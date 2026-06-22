# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                  | Expected Behavior       | Actual Behavior              | Console Output / Error |
| ---------------------- | ----------------------- | ---------------------------- | ---------------------- |
| secret = 50, guess = 1 | GO HIGHER (hint)        | GO LOWER (hint)              | N/A                    |
| Hard                   | Guess 1 to 50           | Guess 1 to 100               | N/A                    |
| Normal                 | 8 attempts              | 7 attempts                   | N/A                    |
| Submit                 | history registers guess | previous guess is registered | N/A                    |

---

## 2. How did you use AI as a teammate?

- Claude code was used to assist with debugging and testing the application.

- Claude correctly pinpointed the reason why the game launched with 1 less attempt than suggested. It identified the issue as being the session state's attempts being initialized to 1 instead of 0.
  Reloading the game after refactoring the buggy line of code correctly displayed the number of attempts left for each difficulty.

- When trying to solve the inaccurate history iupdate, claude suggested to move the debug info block after the submit logic. While this was correct, the instructions were a bit misleading. It specified to move a line (st.write("History:", st.session_state.history) of the 'dev debug' expander) to another instead of moving the block of code. Although the update was functional, the history array was no longer part of the developer debug info expander/dropdown.

---

## 3. Debugging and testing your fixes

- Deciding if a bug was fixed involved refactoring the necessary codes reloading the application and observing it's behavior based on the inputs including edge cases. The bug was considered fixed if the application produced the expected output.

- I tested the right display of attempts and attempts' history by reloading and playing the playing the game to visualize if the number of attempts and history's array updated accordingly.

To throughly test the displayed hint based on users' guesses Claude code was used to generate a pytest which tested win cases, too high cases, too low, parametized and string comparison tests. After inspection of the code generated, running the pytest command in the terminal returned successful results on all tests.

- Claude was helpful in implementing a pytest in a few seconds, but only detailed each function upon asking a follow up request to elaborate. It provided details on the different tests' categories/cases, explained their coverages and the reasons. For example, implementing a parameterized test function allowed to testing various scenarios at once instead of implementing different tests for each scenario.

---

## 4. What did you learn about Streamlit and state?

From my understanding, streamlit reruns re-execute the script after users' interactions with components such as buttons, text boxes' inputs, sliders etc. This behavior causes any changes made to reset after reruns. To remember these changes throught a session streamlit uses session states to store values accross reruns. In the case of this guesser game, the number of attempts, history, score, and secret number live in session states to not be erased after the user clicks submit.

---

## 5. Looking ahead: your developer habits

- One habit that i would reuse in future projects or labs is to use AI to help with implementing tests. Not only implement them was really fast, but AI has also been really valuable in identifying some cases i hadn't taught of.

- One thing to do different on coding task would be to have the file to be updated opened/selected in the editor when prompting the AI. I noticed that doing so gives context to the AI and eliminates the need to constantly attach the file to the chat. Although this only works if the file is the one being actively worked on.

- I've come to realize that AI can be misleading and somtimes wrong with its suggestions. This could be a result of bad prompting practices and lack of context.
