from sys import argv

script, input_file=argv


#Wir erstellen eine Funktion, die eine gesamte Datei "f" liest und anschließend
#ausgibt
def print_all(f):
    print(f.read())

#Keine Ahnung, wie das hier funktionert, aber es scheint die Datei umzudrehen
def rewind(f):
    f.seek(0)

#Diese Funktion hier gibt irgendeine Zeile aus
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Wir öffnen die Input Datei (die beim Aufrufen der Funktion angegeben werden
# muss) und speichern sie unter der neuen Variablen current_file
current_file=open(input_file)



print("First, let's print the whole file: \n")
#Wir rufen die Funktion print_all auf, und geben ihr als Parameter
# die vorher definierte Inputdatei
print_all(current_file)


print("Now let's rewind, like a tape: ")
#wir rufen die Funktion rewind auf und geben ihr als Parameter die vorher
# definierte Inputdatei
rewind(current_file)



print("Let's print three lines: ")
#Wir erstellen eine Variable, damit die Funktion print_a_line einen Input hat
current_line=1
#Wir rufen die Funktion print_a_line auf und verwenden als Input dir vorher
#definierte aktuelle Zeile und die Input Datei
print_a_line(current_line, current_file)

#Um die zweite Zeile zu drucken erhöhren wir die "Zählervariable" um 1, sind
# jetzt also in Zeile 2
current_line=current_line+1
#Wir rufen wieder die Funktion print_a_line auf, diesmal mit erhöhter
#Zählervariable
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line, current_file)
