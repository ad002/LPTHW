from sys import argv
print(argv)

#Run it like this: ex13_Vertiefung.py Hallo Hallo Hallo
#output: ['ex13_Vertiefung.py', 'Hallo', 'Hallo', 'Hallo' ]

# The sys package is a set of modules that allows your application
# to interact with the wider computer systems. Including File Accesses etc.


#-> Mit dem SYS Package kann ich mit meinem Programm (Text-)Dateien schreiben etc.


#The "argv" Attribute within the SYS Package is set when python first starts and
# is a list of all the components of the command line when the script was called

#-> Alles was ich beim Aufrufen meiner Funktion (python ex13.py ....) dahinter schreibe
#wird in einer List gespeichert

# In der Übung ex13 wird festgelegt, dass wir argv mindestens Vier (script, first
# second, third) Werte mitgeben
# müssen, die dann der Reihe nach den
# initialisierten Variablen script, first, second und third zugewiesen werden 
