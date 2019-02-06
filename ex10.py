# Der Befehl \t erzeugt einen String, der einen Tab nach rechts gerückt ist
tabby_cat = "\tI'm tabbed in."

#Der Befehl \n teilt die Zeile hinter sich
persian_cat="I'm split\non a line"

#Hier haben wir einen Slash \a\ eingeschoben
backslash_cat ="I'm \\ a\\ cat"

# Hier wird eine "Liste", aber eher eine grafische Aufzählung erzeugt,
#die einen Tab nach rechts gerückt ist und mit einem * als Aufzählungszeichen beginnt
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#ESCAPE SEQUENCES
# \\          Backslash
# \'          Single Quote (')
# \''         Double Quote ('')
# \a          ASCII bell (BEL)
# \b          ASCII backspace (BS)
# \f          ASCII formfeed (FF)
# \n          ASCII linefeed (LF)
# \N{name}    Character named name in the Unicode database (Unicode only)
# \r          Carriage return (CR)
# \t          Horizontal Tab
# \uxxxx      Character with 16-bit hex value xxxx
# \Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx
# \v          ASCII vertical tab (VT)
# \ppp        Character with octal value ooo
# \xhh        Character with hex value hh
