#Boolean practice
#Vorausgegangen war eine Wiederholungsübung

#ERGEBNIS: 17/20 RICHTIG 

#1
True and True
#das ist false
#FALSCH: Das ist True

#2
False and True
#Auch false
#RICHTIG

#3
1 == 1 and 2==1
#aka: True and False: Also false
#RICHTIG

#4
"test"=="test"
#Das ist True
#RICHTIG

#5
1==1 or 2!=1
#aka True or True: True
#RICHTIG

#6
True and 1==1
#True and True = True
#RICHTIG

#7
False and 0!=0
#False and False: False
#RICHTIG

#8
True or 1==1
#True or True: True
#RICHTIG

#9
"test"=="Testing"
#false
#RICHTIG

#10
1!=0 and 2==1
#aka False and False: False
#RICHTIG

#11
"test"!="testing"
#True
#RICHTIG

#12
"test"==1
#False
#RICHTIG

#13
not(True and False)
#not(False): True
#RICHTIG

#14
not(1==1 and 0!=1)
#not(true and false)
#not(false)
#True
#FALSCH: FALSE ??? VERSTEHE ICH ABER NICHT

#nochmal:
#not(true and TRUE)
#not(TRUE)
#false
#FEHLER: 0!=1 ist TRUE, nicht FALSE!

#15
not(10==1 or 1000==1000)
#not (false or true)
#not(true)
#False
#RICHTIG

#16
not (1!=10 or 3==4)
#not (true or false)
#not True
#False
#RICHTIG

#17
not("testing"=="testing" and "Zed"=="Cool Guy")
#not (true and false)
#not(false)
#True
#RICHTIG

#18
1==1 and (not("testing"==1 or 1==0))
#True and (not (false or false))
#True and (not (false))
#True and (True)
#True
#RICHTIG

#19
"chunky"=="bacon" and (not(3==4 or 3==3))
#false and (not (false or true))
#false and (not(true))
#false and false
#False
#RICHTIG

#20
3==3 and (not("testing"=="testing" or "Python"=="Fun"))
#true and (not(true or false))
#true and not(true)
#true and true
#True
#FALSCH: FALSE

#nochmal:
# True and (not(true or false))
#true and not(true)
#true and false
#false!
#OK: FLÜCHTIGKEITSFEHLER OBVSLY













#meine Eselsbrücke für AND war: ANDe(Alphabet): F= false ist default, außer
#bei den "Doppelt-Gegenstücken zum Defaul" (in dem Fall True True) also
#   True and False = false
#   True and True= True
#   False and True= False
#   False and False= False

#Bei OR ist es genau anders herum: True als default außer beim Doppelten
#Gegenstück, die heben das auf (False False)
#   True or False: True
#   True or True: True
#   False or True: True
#   False or False: False
