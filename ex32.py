the_count = [1,2,3,4,5]
#Anm.: Kann man wohl auch "" verwenden?
fruits=['apples', 'oranges', 'pears', 'apricots']
change=[1,'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes trough a list

for number in the_count:
    print(f"This is count {number}")

#same as above:
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go trough mixed lists too
#notice we have to use {} since we don't know what's in it

for i in change:
    print(f"You got {i}")
#Wie oben wird die Zählervariable aus der For-Schleife hier in die eckigen
#Klammern gesetzt. D.h. sie zählt so lange durch die Liste "change",
#bis die Liste zu Ende ist und füllt jeweils das i-te Element in die Klammer
#, printed also insgesamt für "change" 6 Zeilen mit "You got ---" aus



#we can also build lists, first start with an empty one
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list")
    #appent is a function that lists understand
    elements.append(i)

#ERKLÄRUNG Z. 31
# "in range" heißt für die Schleife: Solange wir noch nicht bei 6 angekommen
# sind bzw.: Mache alles hier in der Sschleife 7 mal

#ERKLÄRUNG Z. 32
#Das Vorgehen wird erst kommentiert ("Adding (z.B 1) to the list")
# i ist dann hier der aktuelle Stand der Zählervariablen i

#ERKLÄRUNG Z. 33
#elements.append(i) füllt in die Leere Liste elements den jeweils aktuellen Wert
#der Zählervariablen i ein, also in diesem Fall alle Zahlen in der Range von
#0 bis 6
#append = "Füllfunktion"
#What does APPEND do?
#"It simply appends to the end of the list."
#Append heißt übersetzt: Anhängen, hinzufügen 



#Now we can print them out, too:
for i in elements:
    print(f"Element was: {i}")



list_test=[1,2,3,4,6,8,9,5]
print(list_test.append(0))
#Das hier gibt output: None
