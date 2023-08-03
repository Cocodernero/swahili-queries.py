# sweahili-queries.py
how well do you know Kenya?

This Python script is a simple quiz game that tests your knowledge. It presents a series of questions to the user and allows them to answer. After each answer, it provides feedback and keeps track of the score. Once all the questions are answered, it displays the final score and the percentage of correct answers.
Quiz Questions and Answers

The script contains a dictionary named quiz that stores questions and their corresponding answers. Each question is represented as a key, and the value associated with each key is another dictionary with two keys:

    "swali": The question itself.
    "jibu": The correct answer to the question.

How to Play

    Run the script in your Python environment.

    The script will display the first question from the quiz dictionary along with the prompt "jibu?" (meaning "answer" in Swahili).

    Input your answer and press Enter.

    The script will provide feedback:
        If your answer is correct, it will display "nare" (meaning "correct" in Swahili), and your score will be incremented by one.
        If your answer is incorrect, it will display "buda hizi ndyo gani!" (meaning "come on, what's this!" in Swahili), show the correct answer, and keep your score unchanged.

    The script will proceed to the next question, and the process will repeat until all questions are answered.

    Once all the questions are answered, the script will display the final score and the percentage of correct answers.
