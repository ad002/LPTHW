#a dictionairy associates one thing to another! No matter, what it is
#e.g. print(states['Oregon'])
#out: 'OR'
#Zu verstehen wie: Gebe mir das aus dem Dict mit dem Namen 'States'
#aus, was mit dem Wert 'Oregon' assoziiert wurde

#Syntax: nameDict = [wert1 : assoziierter Wert 1, wert2 : assoziierter Wert 2]
#Ausgabe eines Werts: nameDict[wert1] -> output: assoziierter Wert 1
#Andersrum geht nicht: nameDict[assoziierter Wert1] -> output Wert1 !/!
#DAS GEHT NICHT!

#Also nur: print(states['Oregon']) -> out: OR
#NICHT! print(states['OR']) -> out: Key Error

states = {
    "Oregon" : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}


#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Michigan',
    'FL': 'Jacksonville',
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#Die hier landen als neue Einträge im cities dictionairy. Falls diese Einträge
#unter gleichem Namen schon existieren sollten, werden sie wahrscheinlich
#+berschrieben I guess
#Sie werden also 'appended', einfach angehängt. Let's check:
print(cities)
#Yes! Output: {'CA': 'San Francisco', 'MI': 'Michigan', 'FL': 'Jacksonville',
#               'NY': 'New York', 'OR': 'Portland'}

#print out some cities:
#Nur Kosmetik:
print('-' *10)
#out: ----------
print('NY State has: ', cities['NY'])
#out: NY State has:  New York
print('OR state has: ', cities['OR'])

#print some states
print('-'*10)
#Abbreviation = Abkürzung
print("Michigan's abbreviation is: ", states['Michigan'])
#out: Michigan's abbreviation is:  MI
print("Florida's abbreviation is: states", ['Florida'])


#Do it by using the States and Cities Dict!
print("Michigan has ", cities[states['Michigan']])
#Von hinten nach vorne lesen: Wir geben erst die Abkürzung des Staates Michigan
#aus, in diesem Fall 'MI' und rufen damit Cities an enstsprechender Stelle auf
#also im Endeffekt cities['Mi']
#Out: Michigan has  Michigan
print("Florida has", cities[states['Florida']])
#Out: Florida has Jacksonville

#Print every state abbreviation
print("-"*10)
#Solange state und abbrev in der Liste States vorkommen:
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#out:
#CA has the city San Francisco
#MI has the city Michigan
#FL has the city Jacksonville


#Print every city in state
print("-"*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
#out:
#CA has the city San Francisco
#MI has the city Michigan
#FL has the city Jacksonville
#NY has the city New York
#OR has the city Portland

#Both at the same time:
print("-"*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    #Gib dass 'abbriev.te' element von cities aus
    print(f"and has city {cities[abbrev]}")
#out:
#Oregon state is abbreviated OR
#and has city Portland
#...


print("-"*10)
#Safely get a abbreviation by state that might not be there:
state=states.get("Texas")
if not state:
    print("Sorry Texas")

#get a city with a default value
city= cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
#The city for the state 'TX' is: Does not exist
