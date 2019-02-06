my_name = "Adrian "
my_age = 20
my_height = 180
my_weight=60
my_eyes="brown"
my_teeth="yellow"
my_hair="Brown"

#Den String beginnen wir mit "f" und packen die Variable in geschweifte Klammern
print(f"Lets talk about {my_name}")

#Mit Kommas getrennt funktioniert es aber genauso
print("Let's talk about", my_name)

#Frage ist, was praktischer ist
print("I'm", my_height, "Centimers tall")
#da muss man mehr Anführungszeichen machen, mit dem f aber die geschweiften
#Klammern, das ist auch krampfig

print("My teeth are usually", my_teeth,"depending on my toothbrush")

total = my_age + my_height + my_weight

print("If I add my height, my age and my weight I get total, which is", total)
