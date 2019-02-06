from sys import argv

script, file_in, file_out = argv

#Alles in einer Zeile:
open(file_out, "w").write(open(file_in).read()))



#Erklärung
# 1.
#open(file_out, "w")
#Die Ausgangsdatei wird im write Modus geöffnet

# 2.
#.write(open(file_in).read()))
#Und dirket überschrieben mit der Inputdatei (file_in), die wir öffnen und lesen
