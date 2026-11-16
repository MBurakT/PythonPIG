import random


def roll() -> int:
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


def play() -> None:
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2-4 players.")
                continue
        else:
            print("Invalid! Try again.")
            continue

    max_score = 50
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for i in range(players):
            print(f"Player {i + 1} turn has just stared!".center(50))
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? ").lower()
                if should_roll != "y":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a:", value)

                print(f"Your score is: {current_score}")

        player_scores[i] += current_score
        print("Your total score is:", player_scores[i])


play()
