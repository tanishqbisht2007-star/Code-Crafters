import tkinter as tk
from tkinter import messagebox

# ----------------------------------------------------
#  QUESTION BANK (EASY TO EXPAND)
# ----------------------------------------------------
question_bank = {
    "Science": [
        ("What planet is known as the Red Planet?",
         ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
        ("What gas do plants absorb?",
         ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "Carbon Dioxide"),
        ("Chemical symbol for water?",
         ["H2O", "HO2", "O2H", "HHO"], "H2O"),
        ("Which part of the cell contains DNA?",
         ["Nucleus", "Cytoplasm", "Ribosome", "Mitochondria"], "Nucleus"),
        ("What force keeps us grounded?",
         ["Friction", "Magnetism", "Gravity", "Pressure"], "Gravity")
    ],

    "History": [
        ("Who was the first US President?",
         ["Lincoln", "John Adams", "George Washington", "Thomas Jefferson"], "George Washington"),
        ("When did WW2 end?",
         ["1943", "1945", "1950", "1939"], "1945"),
        ("Who discovered America?",
         ["Columbus", "Magellan", "Da Gama", "Cook"], "Columbus"),
        ("Pyramids were built by?",
         ["Romans", "Greeks", "Egyptians", "Chinese"], "Egyptians"),
        ("The Great Wall protected China from?",
         ["Japanese", "Huns", "Mongols", "Koreans"], "Mongols")
    ]
}

# ----------------------------------------------------
#  GLOBAL VARIABLES
# ----------------------------------------------------
root = tk.Tk()
root.geometry("650x420")
root.title("Quiz Game")

current_category = ""
questions = []
index = 0
score = 0
selected_answer = tk.StringVar()


# ----------------------------------------------------
# 1. SHOW RULES
# ----------------------------------------------------
def show_rules():
    clear_window()

    rules = (
        "QUIZ RULES:\n"
        "1. Choose a category.\n"
        "2. Answer 5 questions.\n"
        "3. Each correct answer = 1 point.\n"
        "4. Correct answer will be shown each time.\n"
    )

    tk.Label(root, text=rules, font=("Arial", 16), justify="left").pack(pady=40)
    tk.Button(root, text="Start", font=("Arial", 16), command=select_category).pack()


# ----------------------------------------------------
# 2. SELECT CATEGORY
# ----------------------------------------------------
def select_category():
    clear_window()

    tk.Label(root, text="Select a Category", font=("Arial", 20)).pack(pady=20)

    for cat in question_bank:
        tk.Button(root, text=cat, font=("Arial", 16),
                  command=lambda c=cat: start_quiz(c)).pack(pady=8)


def start_quiz(category):
    global current_category, questions, index, score
    current_category = category
    questions = question_bank[category]
    index = 0
    score = 0
    ask_questions()


# ----------------------------------------------------
# 3. ASK QUESTIONS
# ----------------------------------------------------
def ask_questions():
    clear_window()
    global index

    if index >= len(questions):
        calculate_score()
        return

    q, opts, _ = questions[index]

    tk.Label(root, text=f"{current_category} Quiz", font=("Arial", 18)).pack()
    tk.Label(root, text=f"Question {index + 1}/5", font=("Arial", 14)).pack(pady=5)
    tk.Label(root, text=q, font=("Arial", 18), wraplength=600).pack(pady=25)

    selected_answer.set("")  # reset selection

    for opt in opts:
        tk.Radiobutton(root, text=opt, variable=selected_answer, value=opt,
                       font=("Arial", 16)).pack(anchor="w", padx=50)

    tk.Button(root, text="Submit", font=("Arial", 16),
              command=check_answer).pack(pady=20)


def check_answer():
    global index, score

    user_ans = selected_answer.get()

    if user_ans == "":
        messagebox.showwarning("Error", "Please select an answer!")
        return

    correct = questions[index][2]

    if user_ans == correct:
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong!\nCorrect Answer: {correct}")

    index += 1
    ask_questions()


# ----------------------------------------------------
# 4. SHOW FINAL SCORE
# ----------------------------------------------------
def calculate_score():
    clear_window()

    tk.Label(root, text="QUIZ COMPLETED!", font=("Arial", 22)).pack(pady=20)
    tk.Label(root, text=f"Your Score: {score} / 5", font=("Arial", 18)).pack(pady=10)

    tk.Button(root, text="Play Again", font=("Arial", 16),
              command=show_rules).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 16),
              command=root.quit).pack()


# ----------------------------------------------------
# UTIL: CLEAR SCREEN
# ----------------------------------------------------
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# ----------------------------------------------------
# 5. MAIN FUNCTION
# ----------------------------------------------------
def main():
    show_rules()
    root.mainloop()


# Run Program
main()
