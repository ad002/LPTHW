print("""You enter a dark room with two doors.
Do you go trough door #1 or door#2?""")

door=input("Enter # of which door are you choosing: ")

if door=="1":
    print("There's a giant bear here eating a cheese cake")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("Enter number: 1 or 2? ")

    if bear =="1":
        print("The bear eats your face off. Good job!")

    elif bear=="2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away")
#Wichtig hier: Die Einrückung zeigt, dass das elif zum obersten if gehört
#Elif fügt immer noch eine zweite Abfragemöglichkeit hinzu
#kurz für Else/If
elif door=="2":
    print("You srare into the endless absyss at Cthulus retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothpins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    #Der erste OR boolean check ever!
    if insanity =="1" or insanity=="2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good job!")
#Auch hier wieder: Das else gehört zum allerersten if
else:
    print("You stumble around and fall on a knife and die. Good job!")
