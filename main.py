#GC32

import random
again = "yes"
while again == "yes":
    a = random.randrange(0, 1)
    print(a)
    b = input("Confess or Stay Silent").lower()
    if b == "confess" and a == 0:
        print("You are staying in prison for five years")
    elif b == "confess" and a == 1:
        print("You are free to go")
    elif b == "stay silent" and a == 0:
        print("You are in prison for twenty years")
    elif b == "stay silent" and a == 1:
        print("You are in prison for one year")
    again = input("\nDo you want to play again?\n").lower()


