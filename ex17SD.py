#Wir wollen das Script etwas einfacher machen:
from sys import argv

#Die Eingaben der Eingangs- und Ausgangsdatei werden der Reihe nach in
# argv gespeichert
script, from_file, to_file = argv

#We could do these two in one Line. How?

#Wir öffnen die input datei (in_file) und speichern die Daten in
# der neuen Variable in_data
# in_file = open(from_file)
#Wir lesen die geöffnete Datei (in_file) und speichern das Ergebnis in
# neuer Variablen indata
# indata = in_file.read()

#We could do these two in one Line. How?
# beide in einer Zeile:

indata= open(from_file).read()
#Jetzt haben wir die Daten der Inputdatei (from_file) in der Variablen
# indata gespeichert
#VORSICHT BEI DER KLAMMERSETZUNG! indata=open(from_file).read()
# !=  WRONG:                      indata=open(from_file.read())

#Wir öffnen die Ziel/Outputdatei im write Modus
out_file = open(to_file, "w")

#Wir schreiben in die Outputdatei die Daten der Inputdatei
out_file.write(indata)
