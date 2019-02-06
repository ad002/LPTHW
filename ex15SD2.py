filename = input("Gib den Dateinamen ein: ")

filename = open(filename)


print(filename.read())


#Learning:
#der open Befehl wird mit open(Dateiname) ausgeführt
#der read Befehl mit dateiname.read()
#Der Vorgang kann komplett mit einer Variablen geschehen
# Der eingegebene String war in diesem Fall dann ex15_sample.txt und
# der darin enthaltene Text wurde mit dem print und filename.read() ausgegeben 
