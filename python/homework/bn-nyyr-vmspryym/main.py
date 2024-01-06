
import random


def play():
    while True:
        user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit\n")

        if user == 'q':
            print("Thanks for playing!")
            break

        if user not in ['r', 'p', 's']:
            print("Invalid choice. Please choose 'r', 'p', 's', or 'q'.")
            continue

        computer = random.choice(['r', 'p', 's'])

        if user == computer:# If the choices are the same, it's a tie
            print("It's a tie")
        elif is_win(user, computer):
            print('You won!')
        else:
            print('You lose!')

# r > s, s > p, p > r (winning combinations)
def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
                player == 'p' and opponent == 'r')


play()