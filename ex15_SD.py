#5. Use only input and try the script that way


from sys import argv
script = argv

#Hier soll der Nutzer den zu lesenden Dateinamen eingeben
filename = input("Bitte Dateinamen eingeben: ")

#Wir öffnen die Datei und speichern ihren Inhalt in der Variable
# txt
# Dies erstellt ein sog. "File object".
# Wir müssen Dateien erst öffnen und
# in einer Variablen speichern, um sie später auslesen zu können
txt = open(filename)


# Jetzt rufen wir die read funktion auf die wir mit sys importiert haben
# und können jetzt, da wir txt vorher geöffnet haben, nun
# txt auslesen (erscheint dank print direkt auf dem Bildschirm)

print(txt.read())


#Vorher: print(filename.read()), folgender Fehler:
#AttributeError: 'str' object has no attribute 'read'
#Erklärung: Wir haben die geöffnete Datei (filename) ja unter einer
# neuen Variable txt gespeichert, die wir jetzt logischerweise auch
# aufrufen müssen

#Dateien müssen auch geschlossen werden
txt.close()

#NEXT CHALLENGE: OHNE EXTRA VARIABLE TXT AUSFÜHREN
