# close             Closes the file like File>Save in editor
# read              Reads the content of file and you can assign result to a variable
# readline          Reads just one line of a text file
# truncate          Empties the file. Watch out with this one.
# write('Stuff')    Writes 'Stuff' to file
# seek(0)           Move the read/write location to the beginning of file

from sys import argv

#Beim Start müssen wir argv einen Dateinamen mitgeben
script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you dont want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN")

#Der input Befehl wird aufgerufen und ein Fragezeichen ausgegen
input("?")

print("Opening the file...")

#Die am Start eingegebene Datei (filename)wird geöffnet, wir
# erzeugen ein sog. "File Object"
# D.h. Der Inhalt der Datei wird nicht returnt, sondern nur geöffnet
#Das "w" ist ein extra Parameter für die open Funktion ("Write-mode")
# Der Default modus von open(filename) ist "r"
#Es gibt noch den "r" Modus für read und "a" für append
target = open(filename, "w")

print("Truncate the file. Goodbye!")

#der Inhalt der Variable target wird mit .truncate gelöscht / So gehen wir sicher,
#dass wir eine leere Datei haben. Ist im Endeffekt unnötig, weil wir die textdatei mit
# einggebebenem  Dateinamen gerade erst erzeugt haben, aber ist für später interessant
target.truncate()

#Wir speichern drei Eingaben mithilfe des Input Befehls unter entsprechenden variablen
line1=input("Line 1: ")
line2=input("Line 2: ")
line3=input("Line 3: ")

print("I'm going to write these to the file")

#Wir schreiben den String aus line1 in unsere Target-Zieldatei
target.write(line1)
#Es wird ein Absatz "geschrieben" bzw. eingefügt
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("And finally, close it.")
#Wir schließen die Datei
target.close()

# Wir starten das Programm mit: python ex16.py test.txt
# test.txt ist der spätere Dateiname, den wir in  der current directory erzeugen
# Wir können uns aussuchen, wie die Datei heißen soll
# Dank "sys import argv" können wir im System Dateien schreiben
# Mit diesem Programm haben wir dank dem ".write(variable)" eine Textdatei in unserer Directory erzeugt. 
