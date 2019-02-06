#Ich will das lästige manuelle Erstellen einer Input Datei loswerden

#Keine Ahnung, hab ich jetzt noch nicht hinbekommen, siehe Fehler in Zeile 18
#War aber auch eine "over the top" Aufgabe, die ich mir selbst gestellt habe

#Wir geben Inhalt in eine Variable ein
Input = input("Gib einen Text ein, den du in eine OutputDatei übertragen willst: \n > ")

#Wir geben der Output Datei einen Namen und öffnen sie im write Modus
outputDatei=input("Bitte gib der Output Datei einen Namen: ")

#Wir öffnen die output datei im Write Modus
open(outputDatei, "w")

#Wir übertragen die Daten der InputDatei in unserer Outputdatei
outputDatei.write(Input)

#Fehler:    outputDatei.write(Input)
#           AttributeError: 'str' object has no attribute 'write'

# Recherche im Netz ergibt:
# f.write(string) writes the contents of string to the file,
# returning the number of characters written.
# So it returns an integer.
