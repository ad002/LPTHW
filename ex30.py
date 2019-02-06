people = 30
cars=40
trucks=15


#elif sorgt dafür, dass ich nach der ersten if-Abfrage noch eine if-Bedingung
#aufrufen kann, sofern sich die erste eben nicht erfüllt hat.

#Das else wird dann aufgerufen, wenn KEINE der beiden ifs sich bewahrheitet hat
 

if cars>people:
    print("We should take the cars")

elif cars<people:
    print("We should not take the cars")

else:
    print("We can't decide")




if trucks>cars:
    print("Too many trucks")

elif trucks<cars:
    print("Maye we could take the trucks")

else:
    print("We still can't decide")



if people>trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then")
