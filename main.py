import random

def check_win(comp, player):
    if comp == player:
        return "Draw"

    # Snake = 1, Water = 2, Gun = 3
    if (comp == 1 and player == 2) or \
       (comp == 2 and player == 3) or \
       (comp == 3 and player == 1):
        return "Computer wins"
    else:
        return "Player wins"


print("Snake = 1 , Water = 2 , Gun = 3")

player = int(input("Enter your choice (1-3): "))

if player < 1 or player > 3:
    print("Wrong input ")
else:
    comp = random.randint(1, 3)
    result = check_win(comp, player)

    print("Computer chose:", comp)
    print(result)
