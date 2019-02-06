from sys import argv
from os.path import exists

#Hier muss ich beim Aufrufen des Programms
# in der Command-Zeile also eingeben, welche die Ausgangsdatei Ist,
# aus der ich etwas herauskopieren will (from_file) und was die Zieldatei ist (to_file)
# in der ich etwas ablegen möchte (to_file)


script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


#We could do these two on one Line. How?

#from_file wird geöffnet und in neuer Variablen in_file gespeichert
in_file= open(from_file)
#Datei from_file, jetzt als geöffnet in in_file gespeichert, wird jetzt
# gelesen und in neuer Datei indata gespeichert
indata =in_file.read()

#Erstmal ohne die lästigen Variablen drumherumself.
# Ist wahrscheinlich nicht "die feine Art" zu coden, da die Variable
#from_file immer wieder neu überschrieben wird

#from_file=open(from_file)
#from_file=from_file.read()

#in einer Zeile: (Gleichzeitig öffnen und lesen)
# in_file = open(from_file.read())

#Wir messen, wie "lang" die oben eingegebene Datei ist
print(f"the input file is {len(indata)}) bytes long")

#Wir prüfen mit der importierten exists Library, ob die
# Output Datei, in die wir hineninkopieren wollen, überhaupt
# exisitiert
#Die Funktion gibt "True" zurück, wenn die Datei existiert
print(f"Does the output file exist? {exists(to_file)}")

#Das hier ist ziemlicher Quatsch, weil wir nur nach einem input
# fragen, aber ihn nicht "quantifizieren", also sein Ergenis
# interpretieren
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#Wir öffnen die output Datei im "write"/Bearbeitungsmodus
out_file=open(to_file, "w")

#Wir schreiben die vorher eingelesenen Daten (siehe Z.18),
# die wir in "indata" gespeichert haben, aus der Input
# Datei in unsere Output Datei
out_file.write(indata)

# Die Funktion hat jetzt eine zweite Datei mit dem Vorher eingegebenen
# Namen in der Current Directory mit gleichem Text wie in der input
# Datei erstellt

out_file.close()
in_file.close()
