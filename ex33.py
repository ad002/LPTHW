i= 0

#Wir erstellen eine leere Liste
numbers=[]

while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)
    #i bei jedem Durchlauf der Schleife erhöhen, damit wir irgendwann auch bei
    #6 ankommen (while i<6)
    i+=1
    print("numbers are now: ", numbers)
    print(f"At the bottom i is {i}")


print(numbers)
#Ok, hiermit also nochmals confirmed: Append füllt den aktuellen Wert von
#i einfach in die Liste "numbers" ein, also füllt "numbers" von 0 bis 5,
#sodass wir am Ende den folgenden Output haben:
#[0, 1, 2, 3, 4, 5]


#ODER:
for num in numbers:
    print(num)
#Ich denke in Pseudo liest man das so:
#Solange in Numbers etwas drin ist, printe es und fange wieder von oben an

#der output ist dann folgendermaßen:
#0
#1
#2
#3
#4
#5
