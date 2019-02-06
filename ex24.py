print("Let's practice everything")
#Der \' verhindert, dass der Print-Befehl geschlossen wird print('') und wir
#ein ' als Satzzeichen verwenden können
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and\t tabs.')

#Das \t fügt einfach nur einen Tab ein:     Like this!

#Just a multiple Line String
poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passio from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    #Anfangs/Initialisiertungswert *500 ist die Anzahl jelly Beans
    jelly_beans=started*500
    #in ein Glas passen also 1000 jelly_beans
    jars=jelly_beans/1000
    #In eine Kiste passen also 100 Kisten
    crates=jars/100
    return jelly_beans, jars, crates

#Wir erstellen eine Variable Startpunkt
start_point=10000
#Da die Funktion secret_formula die LOKALEN, funktionsinternen Variablen
# jelly_beans, jars und crates zurückgibt,
#speichern wir diese werte direkt in GLOBALEN Varible, um sie nachher noch
#nutzen zu können, mit folgendem Befehl: (also wird die Funktion mit Wert 1000)
#ausgeführt, jelly_beans (LOKAL) aus der Funktion wird in beans (GLOBAL)
# jars(LOKAL) in jars (GLOBAL) gespeichert
beans, jars, crates = secret_formula(start_point)



#Remeber that this is another way to format a string:
#Wir geben einfach nur den Startpunkt, den Anfangswert aus, allerdings
#mit einem anderen Befehl. In die leere Klammer wird der in einen String
#Formatierte Zahlwertt von start_point eingefügt
print("with this starting point of: {}".format(start_point))
#it's just like with the f"" string:
print(f"We have {beans} beans, {jars} jars and {crates} crates.")


start_point=start_point/10

print("We can also have it this way: ")
#Wir rufen die Funktion secret_formula auf und speichern das Ergebnis in formula
formula= secret_formula(start_point)


#This is an easy way to apply a list to a format string
#In die leeren Klammern {} können wir mit dem Formatter Befehl Werte einfügen,
#die wir direkt aus der Funktion secret_formula entnehmen. Da wir 3 Klammern
#haben und 3 Werte, die secret_formula ausspuckt, kommt das hin
#Die Funktion selbsz wird in diesem Fall allerdings schon vorher ausgeführt Und
#anscheinend ihre 3 unterschiedlichen Werte in der Variablen formula gespeichert
#(Siehe Line 60)
print("We have {} beans, {} jars and {} crates".format(*formula))

#BREAKING THE CODE
#Wenn man den * weglässt, erhält man folgenden Error:

#print("We have {} beans, {} jars and {} crates".format(formula))
#IndexError: tuple index out of range

#Hier handelt es sich also um irgendwelche Tuples.
