from sys import argv

# Hiermit werden am Anfang wieder 3 Argumente beim Aufrufen der FUnktion ex14.py verlangt
# Bzw script scheint er automatisch zu erkennen (scheint also das aktuelle Script zu sein, ich muss
# lediglich meinen Benutzernamen und mein Alter eingeben. Wenn ich das geschriebene Programm nicht kenne,
#kann der argv Befehl umständlicher sein. Denn dann weiß ich ja gar nicht, was ich dort gerade eingebe)

#Die Vorher in der Command Line mit eingegebenen Werte (nach ex14.py) werden
# der Reihe nach in user_name und age gespeichert
script, user_name, age = argv
prompt = "Text hier: "

print(f"Hi {user_name}, I'm the {script} script")
print(f"I'd like to ask you a few questions")
print(f"Do you like your name {user_name}?")
#Hier werden wieder wie vorher die Klammern des Input Befehls genutzt, um eine
# visuelle Ausgabe/sichtbare Abfrage auf dem Bildschirm zu haben, allerdings diesmal gefüllt
# mit der Variable prompt. Man könnte genauso gut schreiben: likes=input("> ")
likes=input(prompt)
#Hier eine Line um das zu testen und ja, es funktioniert, ist jetzt aber in der Ausgabe natürlich etwas
# Doppelt gemoppelt
likes=input("> ")

print(f"So you are {age} years old?")
bestaetigung = input("> ")

print(f"Where do you live {user_name}?")
ort=input(prompt)

print("What kind of computer do you have?")
comp= input(prompt)

print(f"""
alright, so you said {likes} about liking meself.
You live in {ort}. Not sure where that is
And you have a {comp} computer. And you told me you are {age} years old. Nice.""" )
