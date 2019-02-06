#Einfach ein String mit ein paar aneinandergereihten Elementen
ten_things = "Apples Oranges Crows Telefphone Light Sugar"

print("Wait, there are not 10 things in the list. Lets fix that.")


#Wir "zerreißen" den String ten_things mithilfe von split und (' ')
#Genauer gesagt: Python macht aus
#Apples Oranges Crows folgendes:
#'Apples' 'Oranges' 'Crows'
stuff=ten_things.split(' ')
#UND NOCH VIEL WICHTIGER: SPLIT MACHT AUS DEM STRING EINE LISTE!
#print(stuff)
#OUTPUT: ['Apples', 'Oranges']

#Eine Liste mit verschiedenen String-Elementen
#Anscheinend kann man eine Liste problemlos über mehrere Zeilen strecken
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
"Banana", "Girl", "Boy"]
#print(more_stuff)
#Output ist in dem Fall dann: ['Day', 'Night' etc

#Solange in der Liste stuff weniger als 10 Elemente drin sind
while len(stuff) !=10:
    #.pop entfernt, sofern wie hier kein index spezifiziert ist pop(), das
    #letzte Element einer Liste und gibt es aus
    #Also: Wir entfernen das letzte Element von more_stuff und speichern es
    #zwischen in next_one
    next_one = more_stuff.pop()
    #wir sagen dem Benutzer, dass wir es jetzt anhängen
    print("Adding: ", next_one)
    #und wir hängen das Element jetzt an Stuff an
    stuff.append(next_one)
    #Und: Wir geben an, wie viele Elemente jetzt in stuff drin sind mithilfe des
    #len() Befehls, der die Länge einer Liste ausgibt und damit die Anzahl der
    #darin enthaltenen elemente
    print(f"There are {len(stuff)} items now")

#Was hier jetzt im konkreten Fall passiert:
#in stuff sind bislang 6 Elemente, also werden noch vier aus
#more_stuff hinzugefügt

#Nach dem while loop haben wir also jetzt mit stuff eine Liste von
# ['Apples', 'Oranges', 'Crows', 'Telefphone', 'Light', 'Sugar', 'Boy', 'Girl',
# 'Banana', 'Corn']

#Wir zeigen dem Nutzer den aktuellen Stand von stuff:
print("There we go: ", stuff)

print("Let's do some things with stuff")

#Wir geben das zweite Element von Stuff aus. Das müsste in diesem Fall oranges
#sein
print(stuff[1])

#Das gibt das letzte Element von Stuff aus, also das Element vor dem ersten
# was ja stuff[0] wäre, in diesem Fall dann 'Corn'
print(stuff[-1])

#Wir schmeißen das letzte Element aus stuff raus und returnen es (wieder 'Corn')
print(stuff.pop())

#Das hier ist der exakte Gegenbefehl zu dem .split(' ') Befehl vom Anfang:
#Er macht aus der Liste stuff einen String
print(' '.join(stuff))

#Das hier nimmt die Elemente an den Stellen 3 bis 5 von Stuff udn verbindet sie
#mit einem #. Das sind in diesem Fall dann die Elemente 'Telephone', und ganz
#WICHTIG: auch das ' '  zählt anscheinend als Element! (aus dem Join Befehl)
#, denn der output hiervon ist:
#Telephone#Light
print('#'.join(stuff[3:5]))
#Seine Dokumentation im Buch:
#Thate xtracts a ”slice” from the stuff list that is from element 3 to
#element 4, meaning it does not include element 5. It’s similar to
#how range(3,5) would work.
