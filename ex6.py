types_of_people = 10

#Eine andere Art, einen String mit Variable in der Mitte zu initialisieren
x=f"There are {types_of_people} types of people."

#Geht aber genauso gut so, nur dass dann um "There are" in der Ausgabe Klammern
#erscheinen: (Auskommentieren um es zu Checken)
#x= "There are", types_of_people,"types of people"
#print(x)

binary = "binary"
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}."

print (x)
print(y)

#der f Befehl ist einfach nur etwas mehr convenient wenn es um Zeichensetzung geht
print (f"I said {x}")
print (f"I also said {y}")

joke_evaluation = "Isn't that Joke funny=! {}"

#Keine Ahnung, was das Format "hilarious" sein soll, kennt Python nicht,
#let's skip it

#print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

#Zwei Strings (w und e) können problemlos miteinander addiert werden
print (w+e)
