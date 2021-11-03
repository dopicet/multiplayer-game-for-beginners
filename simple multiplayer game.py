import random

# list of score
lst_counter = []
# variable for score
counter = []
print("Guess the number")

def multiplayerGame(player):
    global counter
    counter = 0  # reintilize the counter variable to zero beacuse of previous score. 
    n = random.randint(1,10)
    print(f"\n{player} your turn")
    while True:
        usr = int(input("Enter you number: "))
        counter += 1
        if n == usr:
            print(f"congratulation {player} you guess the right number")
            print(f"{player} score: {counter}")
            break
        elif n > usr:
            print("guess greater")
        elif n < usr:
            print("guess lower")
        else:
            print("something went wrong")
    lst_counter.append(counter)

if __name__ == '__main__':
    player1 = input("Player1 Enter Your Name: ")
    player2 = input("Player2 Enter Your Name: ")

    multiplayerGame(player1)
    multiplayerGame(player2)

    if lst_counter[0] == lst_counter[1]:
        print("Draw")
    elif lst_counter[0]>lst_counter[1]:
        print(f"{player2} won")
    else:
        print(f"{player1} won")
