formatter = "{} {} {} {}"

#Dieses .format funktioniert hier irgendwie nicht
#print formatter.format(1,2,3,4)
#Fehler oben: Print Befehl nicht in Klammern

#So ist's richtig und funktioniert, der
#.format Befehl plus die Zahlen in Klammern fügen sie in die Leeren Stellen von Format ein
print(formatter.format(1,2,3,5))

#Mehr als die oben definierten Leerstellen können allerdings nicht gefüllt werden,
# siehe Ausgabe (nur 4 "Felder" definiert)
print(formatter.format(1,2,3,5,6,4,3))

#Das Einfügen funktioniert genauso für Strings, die per Komma getrennt werden
print(formatter.format("One","Two", "Three", "Four"))

#Ebenso wie für Boolean-Werte...
print(formatter.format(True, False,False,True))

#Das hier ruft ja bei jedem der vier zu befüllenden Felder wieder die Formatter
#Funktion auf, d.h. es ergibt 4x4=16 eckige Klammern als Ausgabe
print(formatter.format(formatter, formatter, formatter, formatter))

#Wieder mal ein String in den vier Elementen
print(formatter.format("Try your", "Own Text", "Here", "Maybe"))
