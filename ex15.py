#Wir importieren die Library
from sys import argv

#Wir entpacken die Library und nutzen argv, um den Dateinamen zu erhalten
#Der vorher eingegeben Dateiname wird unter Filename gespeichert
script, filename = argv

#Die Variable txt kriegt die Werte zugeweisen,
# die der open Befehl aufruft und die im Dateinamen (ex15_sample.txt) enthalten sind
txt = open(filename)

print(f"Here's your file {filename}")

#Wir rufen die Funktion von txt auf, die read heißt
#Was wir von open zurückerhalten ist eine Datei
print(txt.read())

#Hier soll einfach nochmal der Dateiname eingegeben werden
#Dieser muss stimmen, denn die Funktion open() kann anscheinend nur auf
#Dateien angewendet werden, die wir vorher geladen haben
print(f"Type the filename again:")

#Der eingegebene Wert wird unter file_again gespeichert
file_again = input("> ")

#open ruft den vorher eingegebenen Dateinamen auf und öffnet die Datei,
#das Ergenis wird unter txt_again gespeichert
txt_again = open(file_again)

#.read ruft den Text aus txt_again auf und gibt es aus
print(txt_again.read())

#Study drill 0.7
txt_again.close()
txt.close()
