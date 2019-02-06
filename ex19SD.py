def printthis (x,y):
    gesamt=x+y
    print(f"Du hast insgesamt {gesamt} € auf dem Konto.")



printthis(20,39)

#Hier rufe ich die Funktion auf, lasse den Benutzer
#aber direkt per input Befehl die Attributwerte für die Funktion
# eingeben
printthis(input("Wie viele Euros hast du? \n > "), input("Wir viele Cents hast du? \n > "))

a = 300
b=22
printthis(a+23, b+222)
