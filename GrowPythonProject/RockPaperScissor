import tkinter as tk
import random

def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return f"Computer chose {computer_choice}. {result}"

def on_button_click(choice):
    result_text.set(determine_winner(choice))

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Labels
label = tk.Label(root, text="Choose your move:")
label.pack()

# Buttons
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click('rock'))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click('paper'))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click('scissors'))
scissors_button.pack(side=tk.LEFT, padx=10)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12, 'bold'))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
