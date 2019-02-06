i=1
numbers = []

#while i<6:
#    print(f"At the top i is {}")
    #Wir fügen die Zahl i der Liste hinzu
    #Um exakt zu sein: Wir hängen sie hinten an. Da sie bislang leer ist,
    #geht es mit 1 an Stelle [0] los
#    numbers.append(i)
#    i=i+1
#    print("Numbers now: ", numbers )
#    print(f"At the bottom i is {i}")


#AUFGABE 1: CONVERT THE WHILE LOOP TO A FUNCTION THAT YOU CAN CALL AND
#           REPLACE 6 IN THE TEST (i<6) WITH A VARIABLE

def putNumberIn(times):
    #Weil wir innerhalb einer Funktion sind, aber auf die Lokale Variable i
    #zugreifen, müssen wir das hier mit i global kurz angeben
    global i
    while i<times:
        print(f"At the top i is {i}")
        numbers.append(i)
        i+=1
        print("numbers is now:", numbers)
        print(f"at the bottom i is {i}")

#LET'S CALL THE FUNCTION:
putNumberIn(10)
#Oder: Mit input (den wir aber erst wieder von String zurück in Int verwandeln
#müssen, um damit die Funktion putNumberIn aufrufen zu können)
putNumberIn(int(input("Wie lang soll die Liste werden?> ")))


print("The numbers: ")
#aka: Solange in Numbers etwas drin ist, gebe alles der Reihe nach aus,
#was drin ist.
for num in numbers:
    print(num)
