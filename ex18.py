#FUNCTIONS

# Um einen Funktion zu erstellen, def Funktionsname (ARGUMENT):
#                                     was macht die Funktion

#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#Hier werden arg1 und arg2 gleich dem Eingangsargument gesetzt, damit Wir
# zwei Ausgabeargumente haben. Warum auch immer. Der * ist unnütz, s.u.


#ok, that *args is actually pointless, we can just do This
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")

# this just takes ONE ARGUMENT
def print_one(arg1):
    print(f"arg1: {arg1}")

#This takes NO ARGUMENTS
def print_none():
    print("I got nothin to do with no argument initialized")


#Das hier ruft die Funktion print_two auf und gibt ihr zwei Strings mit.
# Ob das wohl funktioniert? Ich glaub nicht. Denn es wird bei der
# Erstellung der FUnktion nur ein Argument "*args" initialisiert,
# da können wir jetzt nicht auf einmal mit zweien kommen

#Update: Es funktioniert und gibt folgendes aus:
#arg1: Zed, arg2: Shawn
#Why?
#Because the * (Line 7) tells Python to take all the arguments! to the
# Function and then put them in args as a list. Genau wie bei dem argv, das
# wir schon benuttzt haben, sorgt der Befehl arg1, arg2 = args (line 8) dafür
#, dass arg1 und arg2 sukzessive in die args liste eingefügt werden! 
print_two("Zed", "Shawn")

#So geht's richtig, print_two_again wurde mit 2 Argumenten initialisiert,
# also müssen wir auch zwei Argumente zum Ausführen mitgeben
print_two_again("Zed", "Shawn")

#Mit einem Attribut/Argument gehts gut
print_one("First!")

#Hier passiert nur der Einfache Print Befehl
print_none()
