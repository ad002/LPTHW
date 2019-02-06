from sys import argv

script, input_file = argv


#Wir ertsellen eine Funktion, die eine bestimmte Zeile
# des Dokuments ausgibt
#Die Parameter sind "line" für die aktuelle Zeile
#und "file" für die Datei, die wir verwenden wollen
def print_this_line (line, file):
    #Hier verstehe ich nicht, warum man nicht file.read(zeilennummer) nimmt
    print(line, file.read())



#Wir öffnen die input_datei und speichern das in einer
#neuen Variable aktuelle Datei

#  aktuelle_datei=input_file.open() -> Fehler: Der Befehl heißt: open(Name)
aktuelle_datei=open(input_file)

#Wir legen eine aktuelle Zeile fest, die wir aus der Inputdatei
# auslesen wollen

aktuelle_zeile = 1

#ZEILE 1
#Wir rufen die Funktion print_this_line auf, um die
#erste Zeile auszugeben
print_this_line(aktuelle_zeile, aktuelle_datei)

#ZEILE 2
#Eine andere Art, das zu tun:
print_this_line(2, aktuelle_datei)
#Wir legen als aktuelle Zeile einfach 2 fest, ohne die vorher
#definierte Variable aktuelle_zeile zu verwenden
#Das gibt mit am Ende aber nur eine 2 aus? 

print("\n")

#ZEILE 3
#Wir müssen erst unsere "Zeilenzählervariable" aktuelle_zeile
# um eins erhöhen
#Dafür nutzen wir, wie im Study Drills gefordert den += Befehl
aktuelle_zeile+=1

# x=x+y =
# x+=y
#Wichtig: Der += Operator ruft das, was vor dem Gleich
#steht auf und nach dem Gleich muss das stehen, was ich zu dem
#was vor dem Gleich steht, dazuaddieren will
print_this_line(aktuelle_zeile,aktuelle_datei)
