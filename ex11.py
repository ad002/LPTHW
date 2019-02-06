# Der Befehl input() sorgt dafür, dass die Eingabekonsole eine Eingabe von mir verlangt.
print("How old are you?", end='')
#Die Eingage, der sog. "input" wird in der Variable age gespeichert
age = input()

# Der end='' Befehl sorgt dafür, dass die Zeile nicht aufhört, sondern mit dem
#folgenden Befehl weitergeführt wird. Die Ausgabe ist in diesem Fall in einer Zeile:
#"Ich liebe meine Leben Ich liebne meine Leben"
print("Ich liebe meine Lebenen ", end='')
print ("Ich liebne meine Leben")





print("How tall are you? ", end='')
height= input()

print("How much is your weight? ", end='')
weight = input()

# Hier gibt es wieder zwei Möglichkeiten, die Variablen in einen String-Ausgabetext
#einzubetten. Die Variante mit Kommas:
print("So you are ", age,"years old ", height, "Centimeters tall and ", weight, " heavy.")

#Und die Variante mit (f "String {Variable}").
#In diesem Fall mit 3 Variablen hat sich diese Variante als praktischer erwiesen, da nicht andauernd "" gesetzt werden müssen und man nicht so sehr auf die Leerzeichen achten muss
print(f"So you are {age} years old, {height} tall and {weight} heavy.")

#Wenn man nur den input() Befehl schreibt, beendet Python das Programm nicht,
#sondern wartet, dass man irgendetwas (Egal ob Zahl oder String) eingibt.
# Hier verlischt die Eingabe einfach nur ins Nichts, weil sie nicht in einer
# Variable gespeichert wird.
input()

#Diese Eingabe sollte man am besten in der Zeile darunter in einer Variable speichern. In
x = input()
#Das gibt mir die Eingabe dann einfach wieder aus
print(x)


# "This Command gets a Number as a string from input() and then
#converts it to an integer using int()" (S.69)

#-> Mit diesem Kommando legen wir fest, dass der Input eine Zahl sein muss.
# Wird ein String eigegeben, beendet Python das Programm
y = int(input())

print (y)
