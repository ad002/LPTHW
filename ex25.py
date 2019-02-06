def break_words(stuff):
    #Gespannt, ob das hier beim Aufrufen der Funktion mit gedruckt wird
    #Die Dinger heißen "documentation comments" und wenn wir die Funktionen
    #über die Console aufrufen und z.b. help(ex25) eingeben, könenn wir
    #Sie über den Funktionsdefinitionen sehen als Hilfestellung
    """This function will break up words for us"""
    #Die Eingangsworte werden mit .split geteilt und in words gespeichert
    words=stuff.split(' ')
    return words

#Werden hier wohl die vorher ausgegebenen, bereits "gebrochenen"/gesplitteten
#Worte verwendet (Line 6)oder ist words nur eine neue, lokale variable für
#genau diese eine Funktion?
def sort_words(words):
    """Sort the words"""
    #anscheinened gibt es eine funktion die sorted heißt??
    return sorted(words)



def print_first_word(words):
    """Print the first word after popping it off"""
    #Die Eingangsworte werden "gepoppt", an Stelle 0? und in einer Variable
    #word gespeichert -> Gut, den code rückwärts zu lesen
    word=words.pop(0)
    #Hier wird mal "geprinted", anstatt nur zu "returnen". Ob das einen Unter-
    #schied macht?
    print(word)

def print_last_word(words):
    """This is the last word after popping it off."""
    #Hier "poppen" wir an einer anderen Stelle, an -1
    word=words.pop(-1)
    print(words)

def sort_sentence(sentence):
    """Takes in a full sentence and returns sorted words"""
    #Wir rufen die vorher definierte Funktion auf (Zeile 1) und speichern
    #das Ergebnis in der Variablen words
    #Der Satz wird also in einzelne Wörter zerbrochen
    words=break_words(sentence)
    #Wir nutzen die print_first_word Funktion, um das erste Element auszugeben
    print_first_word(words)
    print_last_word(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
