def add(a,b):
    print(f"Adding {a} + {b}")
    #Dieser (reuturn-) Befehl ist neu. Wird wohl das selbe machen, wie
    #Wenn ich schreiben würde print(a+b)
    return a+b

def subtract(a,b):
    print(f"Subtracting {a} and {b} ")
    #Man braucht wohl keine Klammern
    return a-b

def multiply(a,b):
    print(f"Multiplying {a} and {b}")
    return(a*b)

def divide(a,b):
    print(f"Dividing {a} and {b}")
    return(a/b)

#Die Variablen a und b sind lokale Variablen, die quasi als "Platzhalter"
#in der Funktion stehen, um ihr zu sagen, was mit ihnen passieren soll
#Ihr definierter Name ist dabei völlig gleichgültig. Am Ende ist eigentlich
#nur wichtig, wie viele Parameter es gibt (Um die Funktion mit entsprechender)
#Anzahl später aufrufen zu können) und was mit diesen Parametern innerhalb
#der Funktion passiert


print("Let's use the functions")

#Wir rufen die Funktionen auf und geben ihnen Werte, getrennt durch
#Kommas mit auf den Weg
age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")


#HIER EIN PUZZLE
print("Ein Puzzel für den Extra Credit")

what= add(age, subtract(height, multiply(weight, divide(iq,2))))
#Eine sehr verwschachtelte Rechnung. Was da genau vorgeht:
# Am besten von hinten nach Vorne:
#wir teilen den iq durch 2 und mulitplizieren das mit dem Gewicht
#wir ziehen von der Größe das vorherige Ergebnis ab
#und addieren das Alter dazu
#Von Hand:

#age=35
#weight=74
#height=180
#iq=100

#Zeile 40: (100)/2 = 50
#Fortsetzung Zeile 40: 50*74 = 3700
#Zeile42: 180-3700= -3250
#Zeile43: -3215

print("That becomes: ", what, "Can you do it by hand?")
