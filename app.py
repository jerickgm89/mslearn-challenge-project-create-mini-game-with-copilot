import random

valid_moves = ['rock', 'paper', 'scissors']
score = 0

while True:
    user_move = input("Enter your move: ").lower()
    if user_move not in valid_moves:
        print("Invalid move. Please enter rock, paper, or scissors.")
        continue

    computer_move = random.choice(valid_moves)

    if (user_move == 'rock' and computer_move == 'scissors') or \
       (user_move == 'scissors' and computer_move == 'paper') or \
       (user_move == 'paper' and computer_move == 'rock'):
        score += 1
        print(f"You won! The computer chose {computer_move}. Your score is {score}.")
    elif user_move == computer_move:
        print(f"It's a tie! The computer also chose {computer_move}. Your score is {score}.")
    else:
        print(f"You lost! The computer chose {computer_move}. Your score is {score}.")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        break

print(f"Game over. Your final score is {score}.") 