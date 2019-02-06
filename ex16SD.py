from sys import argv

#Wir fordern den Nutzer auf, die Datei zu benennen
dateiname= input("Wie soll die Datei heißen, die wir erzeugen?" )

#Ich habe hier bewusst darauf verzichtet, dateiname = argv zu verwenden
# und führe die "Namensgebung" für die Datei mit dem Input Befehl aus

#Wir fragen ab, was in der ersten Zeile stehen soll und speichern dass
#in einer Variable. Die Eingabe erfolgt unter dem ausgegebenen Text (\n)
# und wird mit einem > eingeleitet

zeile1=input("Was soll in der ersten Zeile stehen?\n > ")
zeile2=input("Wie soll's weitergehen?\n >")


# dateiname.write(zeile1)
# dateiname.write(zeile2)
# Ergibt folgenenden Fehler:
# 'str' object has no attribute 'write'

#vielleicht muss die Datei, obwohl wir sie neu erstellt haben,
# erst geöffnet werden?
#Ja, muss sie. Siehe Zeile 27. Zusätzlich muss noch das Attribut "w" eingfügt werden

#Wichtig ist auch, dass wir das  ,"w" ergänzen. Nur mit dem ,"w"
# Der open Befehl wird im Default Modus ja mit "r" für Read ausgeführt
# das ,"w" ist ein extra Parameter, den wir mitgeben müssen, denn Python
# will sicher gehen, dass wir wirklich in die Datei schreiben wollen

#Das w sagt: Öffne die Datei im "Write" Modus
dateiname=open(dateiname, "w")

#So werden die Strings einfach aneinandergereiht, man könnte jetzt hier auch
# noch ein dateiname.write("\n") einfügen, um einen Zeilenumbruch dazwischen
# zu haben

dateiname.write(zeile1)
dateiname.write(zeile2)
dateiname.write("Leck mich am Sack")


dateiname.close()
