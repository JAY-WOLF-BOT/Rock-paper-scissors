import tkinter as tk
import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Set up the window
window = tk.Tk()
window.title("Rock Paper Scissors Game")

# Set up buttons
rock_button = tk.Button(window, text="Rock", width=20, command=lambda: play_game('Rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=20, command=lambda: play_game('Paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=20, command=lambda: play_game('Scissors'))
scissors_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors!", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the main loop
window.mainloop()
