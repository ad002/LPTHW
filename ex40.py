#Getting things from things on 3 different ways

#1 - dict style
# mystuff['apples']

#2 – module style
# mystuff.apples()
# print(mystuff.tangerine)

#3 – class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)

class Song(object):
    #Defining a funtion for a whole class!
    def __init__(self, lyrics):
        self.lyrics = lyrics
#Why self when making __init__ or other functions for classes?
#If you don't have self, then it isn't clear, whether you mean the
#instance's attribute or a local variable.
# E.g you don't know if cheese = 'Frank' is the instance's cheese-attribute
#or a local variable named cheese. With self.cheese = 'Frank' it is very clear
# you mean the instance attribute self.cheese

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#die Variable happy b-day wird als Klasse Song initialisiert
#Somit hat sie automatisch die Funktion sing_me_a_song 'eingebaut'
                #Wichtig: We are passing a list of strings as the lyrics
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right here"])



bulls_on_parade = Song(["They rally areound tha family",
                            "with pockets full of shells"])

#Wir können auf die Variable 'happy_bday' die Funktion 'sing_me_a_song'
# der Klasse ‘song’ anwenden, da die Variable ‘happy_bday’ als eine
#variable der klasse ‘Song’ initialisert wurde.
happy_bday.sing_me_a_song()

#Gleiches gilt für bulls on Parade
bulls_on_parade.sing_me_a_song()

#STUDY DRILLS I
#Auch das geht! Also mit Zahl.
fuckmylife = Song([23, "Leck mich am arsch", "Du fptze"])
fuckmylife.sing_me_a_song()
#Ausgabe ist dann:
#23
#Leck mich am arsch
#Du fptze

#STUDY DRILLS II
#Put the lyrics in a separate variable, then pass that variable to
#the class to use instead.
text = ["Du kannst mich mal", "Am Arsch lecken", "Du HuSo"] #Text als Liste
doofsong= Song(text) #Doofsong den Text geben
doofsong.sing_me_a_song() #doofsong den Text ausgeben lassen
