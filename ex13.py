#Diese Zeile importiert argv, das heißt ausgeschrieben argument variable und
#diese variable "hält" das Argument, das ich ihr im Laufe des Scripts übergeben
#It means “from the module sys, import the function or parameter argv”.
from sys import argv
#-> Mit dem SYS Package kann ich mit meinem Python-Programm
# (Text-)Dateien schreiben etc.





#The "argv" Attribute within the SYS Package is set when python first starts and
# is a list of all the components of the command line when the script was called

#-> Alles was ich beim Aufrufen meiner Funktion (python ex13.py ....) dahinter schreibe
# wird in einer List gespeichert

#Diese Zeile "entpackt" argv, sodass argv nicht alle in der Kommandozeile
# eingegeben Argumente "hält", sondern
# die eingegenen Argumente werden der Reihe nach den
# vier Variablen script, first, second und third zugewiesen

# It just says: ”Take whatever is in argv, unpack it, and assign it to all of
# these variables on the left in order.”

script, first, second, third, fourth = argv

#Die Variable script wird automatisch als Name des Scripts (ex13.py) gesetzt
# Kann also vernachlässigt werden, wir müssen beim Aufrufen
# nur noch genug Werte für first, second, third und fourth mitgeben, also vier

#Diese Dinge, die wir importiert haben, werden MODULE genannt oder LIBRARIES

print("The first script is called:", script)
print("your first Variable is: ", first)
print("your second variable is: ", second)
print("your third variable is: ", third)
