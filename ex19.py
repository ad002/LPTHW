def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket\n")

print("We can just give the function numbers directly: ")

#Wir rufen die Funktion cheese_and_crackers auf und geben ihr
# Zahlwerte für Cheese count und boxes of crackers mit
cheese_and_crackers(20, 30)



print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

#Wir rufen die Funktion cheese_and_crackers auf, allerdings mit den Werten
# der vorher definierten Variablen
cheese_and_crackers(amount_of_cheese, amount_of_crackers)




print("We can even do Math inside, too: ")
#Wir rufen die Funktion cheese_and_crackers auf, aber errechnen die Werte
#für die Argumente erst beim Aufrufen
cheese_and_crackers(10+20, 5+6)



print("And we can combine the two: Variables and Math: ")
#Wir rufen die Funktion cheese_and_crackers auf und Berechnen die
# Werte für die Argumente aus einer Addition von Variablenwerten
# und eifnachen Zahlwerten
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
