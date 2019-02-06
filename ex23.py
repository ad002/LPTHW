import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line=language_file.readline()

    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)


def print_line(line, encoding, errors):
    next_lang =line.strip()
    raw_bytes =next_lang.encode(encoding, errors=errors)
    cooked_string=raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages=open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


#Kommentar zu Zeile 1-2
#Anstelle von "import sys from argv"
#und "script, input_encoding, error = argv" rufen wir nur die argv
#funktion von sys auf

#Kommentar Zeile 10
#Hier rufen wir die Funktion wieder mit sich selbst auf (?)

#Kommentar Zeile 13
#mit line.strip() scheinen wir in die nächste Zeile zu springen

#Kommentar Zeile 19
#Wir öffnen die Datei "languages" und öffnen irgendwas mit Encoding



#SEINE CODEKOMMENTARE

#1-2
#Wir starten mit den üblichen Kommandozeilenargumenten

#5
#Alles hauptsächliche definieren wir in der main-Funktion. Diese wird am
#Ende des Scrits aufgerufen, um die Dinge zum Laufen zu bringen.

#6
#Das erste, was die Funktion macht, ist eine Zeile der Language-Datei zu lesen
#Das ist nichts neues, haben wir vorher schon gemacht. Einfach nur "readline"

#8
#Jetzt verwenden wir etwas Neues: Ein if-Statement, mit dem wir die "Wahrheit"
#einer Variable testen können.
#In diesem Fall testen wir, ob die Zeile einen Inhalt hat.

#Die readline-Funktion gibt einen leeren String zurück, wenn wir am Ende der
#Datei angekommen sind und if-line testet auf diesen leeren String.

#Solange readline uns etwas zurückgibt, wird das so sein (True) und der darunter
#liegende Code (Zeilen 9-10) wird ausgeführt

#9
#Wir rufen eine seperate Funktion auf, die das "Printen" der Zeile übernimmt
#Das erleichtert den Code: Sofern ich verstanden habe, was print-line macht,
#kann ich sie ausser Acht lassen und einfach immer nur noch aufrufen, wenn ich
#sie brauche.

#10
#Wir rufen die Main Funktion innerhalb der Main Funktion auf. Eigentlich ist
# das verboten (Unendlicher Loop), aber wenn wir zurück auf Zeile 8 schauen
#sehen wir, dass das erneute Ausführen durch das if bedingt ist.

#13
#Wir starten die Defintion der print-line Funktion, die die tatsächliche
#Decodierung von jeder Zeile des Textdokuments vornimmt

#14
#Das ist ein simples "Strippen" der amhängenden \n auf dem Linienstring

#15
#Nun nehmen wir endlich die aus der Datei erhaltene Sprache und "encoden" sie
#in Rohbytes. DECODE BYTES, ENCODE STRINGS -> Die next_lang Variable ist ein
#String, um Rohbytes zu erhalten, müssen wir also .encode() aufrufen.

#16
#Wir machen einen Extraschritt, indem wir die Inverse von Zeile 15 zeigen und
#das machen wir, indem wir eine cooked_string Variable einführen. Wir decodieren
#Bytes und raw_bytes sind Bytes, also rufen wir .decode() auf, um einen String
#zu erhalten.

#18
#Wir geben beide einfach aus und zeigen, wie sie aussehen

#21
#Die Funktionsdefinition ist durch, jetztz wollen wir die languages.txt
#Datei öffnen, um die Funktion auf sie anzuwenden

#23
#Wir rufen die Main-Funktion auf und starten das Programm


#ZUSAMMENFASSUNG "HOW COMPUTERS WORK"

#Computer sind in ihrem Kern nur eine Ansammlung, ein Array, von Lichtschaltern
#(Nullen und Einsen)
#-> Diese Lichtschalter nennen wir "bits"

#Computer nutzen die Nullen und Einsen, um größere Zahlen zu Codieren (encode)
#z.B. Nutzen sie 8 Nullen und Einsen um 256 Zahlen zu codieren (0-255)
#Es gibt einen Standard: 00000000 = 0, 11111111=255
#-> Ein Byte ist eine Sequenz von 8 bits (8 Nullen und Einsen)
#-> Ein Byte kann 256 Numbern halten (0-255 oder 00000000-11111111)

#ASCII (American Standard Code for Information Interchange) ordnet jeder Zahl
#einen Buchstaben zu. So ist z.B. 90 ein Z, was in Bits 1011010 ist
#Da wir jetzt eine Methode haben, um Buchstaben mit 8 Bits darzustellen, können
#wir sie aneinander "stringen"(orig.: We can string them together to a word)
#z.B. "Zed A. Shaw" ist [90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119] als
#Sequenz von Bytes

#Problem mit ASCII: Es kodiert nur Englisch. Da ein Byte 256 Numbern halten kann
#und es in allen Sprachen der Welt deutlich mehr als 256 Zeichen gibt, gibt es
#den UNICODE. Ein Universal Coding für alle Sprachen der Welt.
#-> Man kann 32 Bits benutzen, um Unicode zu kodieren
#-> 32 Bits bedeutet 4.294.967.295 Zeichen (2^32)
#-> 32 Bits sind 4 Bytes (32/8 == 4)
#-> Das bedeutet: Viel verschwendeter Platz. Wir können auch 16 Bits (2 Bytes)
#verwenden, die Lösung sind aber 8 Bits
#-> 8 Bits beinhaltet die meist häufigsten Zeichen und die Lösung flüchtet
#in höhere Bitzahlen, falls mehr benötigt werden

#-> In Python ist die Konvention zur Codierung von Text "utf-8" (Unicode
#Transformation Format 8 Bits)





#WHAT TO KNOW ABOUT THIS SCRIPT

#Das ex23.py Script nimmt due Bytes, die im b'' (byte String) geschrieben sind
#und konvertiert sie zu UTF-8 (oder alles andere, das du beim Aufrufen der
#Funktion festlegst)
#Aufrufen der Funktion in der Konsole: python ex23.py utf-8 strict

#Auf der linken Seite ist die Nummer für jeden Byte von UTF-8 (angezeigt in
#Hexadezimal) und die rechte Seite hat den tatsächlichen Zeichenoutput in
#UTF-8





#ERKÄRUNG HEXADEZIMAL – EXKURS
#Source: https://de.wikibooks.org/wiki/Mathematik:_Schulmathematik:
#_Zahlensysteme:_Hexadezimale_Zahlen

#lat. für Sechzegn (hexa=6 und decem=10) ist ein IT-Zahlensystem

#Besteht aus 16 Ziffern (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)

#In der IT beliebt, da  Umrechnung in Binärzahlen sehr einfach, weil es
#ebenfalls 2 als Basis (2^4 = 16) hat, aber platzsparender ist, da 4 Binärzahlen
#einer Hexadezimalzahl entsprechen

#Um Hexadezimalzahlen zu kennzeichnen, fügt man ein "h" oder den Index "16"
#hinzu


#Binär
#   (8421)      als sonst nicht sichtbare "Legende" über den Binärzahlen
#    0000       So ausgegebene Zeichen auf dem Screen
#-> 1. Stelle steht für 8, zweite für 4, dritte für 2 und vierte für 1
#-> Ergo: 1 ist in Binär: 0001, 2 ist 0010 usw., 3 ist 0011, vier ist 0100



#UMRECHNUNG Binär -> Hexadezimal
#Wie erwähnt: Beide Zahlensysteme 2 als Basis, wegen 2^4=16 können wir nun,
#von hinten beginnend, immer 4 Ziffern unserer Binärzahl zusammenfassen und in
#eine Ziffer unserer Hexadezimalzahl umschreiben

#   0001b = 1h         (b für binär, h für hexadezimal)
#   1001b = 9h
#   1010b = Ah
#   1100b = Ch
#   1111b = Fh

#Analog könenn wir verfahren, wenn es sich um größere Binärzahlen handelt
#   0001 0000b = 10h
#   0001 1101b = 1Dh
#   1010 1101b = ADh

#UMRECHNUNG Hexadezimal -> Dezimal
#Exemplarisch wandeln wir die Hexadezimalzahl 3E8h in das Dezimalsystem um
#Das Prinzip ist die einzelnen Hexadezimalziffern als Faktor vor die
#entsprechende Potenz von 16 zu schreiben und dementsprechend aufzusummieren

#3E8h -> 3*16^2 + E*16^1 + 8*16^0 = 3*16^2 + 14*16^1 + 8*16^0 = 768+244+8 = 1000



#BACK TO THE SCRIPT
#Linke Seite von <===> : Python Numerische Byte oder die "Raw-Bytes" die Python
#nutzt,um einen String zu speichern

#Rechte Seite von <===> : "Raw-Bytes" "gekocht" oder "gar", sodass ich echte
#Zeichen in der Console sehen kann

#z.B. (output)
#b'Afrikaans' <===> Afrikaans
#b'\xe1\x8a\xa0\xe1\x88\xad\xe1\x8a\x9b' <===> áŠ áˆ›áˆ­áŠ›
#b'Aragon\xc3\x83\xc2\xa9s' <===> AragonÃ©s
#b'Arpetan' <===> Arpetan

#DISCRETING THE CODE

#In Python ist ein String eine in UTF-8 codierte Sequenz von Zeichen. Die Bytes
#sind die "Rohsequenz" an Bytes die Python nutzt, um den UTF-8 String zu
#speichern.

#Das b' am Anfang sagt Python, dass wir mir Roh-Bytes arbeiten. Dies ist eine
#Konvention für die Textverarbeitung in Python.



#ALLES WAS ICH WISSEN MUSS

#Wenn ich Rohbytes habe, muss ich .decode() benutzen, um den String zu erhalten.
#-> Python sagen: Dies in einen UTF-String decodieren.
#-> MERKHILFE "DBES" (Decode Bytes, Encode Strings)
