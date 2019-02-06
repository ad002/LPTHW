things = ['a', 'b', 'c', 'd']
print(things[1])
#= b

things[1]='z'
print(things[1])
#=z
print(things)
#output:['a', 'z', 'c', 'd']

#lists = you can only use numbers to get items out of a list
#e.g. things[1]

#dict = lets you use anything, not just numbers. It associates one thing
#to another, no matter what it is

stuff = {'name' : 'Zed', 'age' : 39, 'height' : 6*12+2}
print(stuff['name'])
#Output: Zed

print(stuff['age'])
#Output: 39

print(stuff['height'])
#Output: 74

stuff['city'] = "SF"
#Wird das Element einfach hinten angehängt??????????
#Ja, wird es. Es folgt auf 'height'
print(stuff)
#Out: {'name': 'Zed', 'age': 39, 'height': 74, 'city': 'SF'}

print(stuff['city'])
#Output: SF

#As you see we use strings to say what we want from the stuff dictionary
#The syntax is:
# name = { 'element' : 'associated value' , 'next element' : 'assoc. value'}

#You dont have to use only strings. You can also do stuff like this:

stuff[1] = "Wow"
stuff[2] = "Neato"
#Zu beachten: Mit diesen Befehlen wird hinten angehängt: (!!!)
# [...], 'SF', 1: 'Wow', 2: 'Neato'}
print(stuff)
#Output also:
#{'name': 'Zed', 'age': 39, 'height': 74, 'city': 'SF', 1: 'Wow', 2: 'Neato'}
#Also ganz anders als bei den Listen, wo jetzt das 2. Element mit List[1] durch
#"Wow" ersetzt werden würde!


print(stuff[1])
#Output: Wow
print(stuff[2])
#Output: Neato
print(stuff)
#-> You see: You can use numbers or strings as keys to the dict


#Here's how you delete Stuff:
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
#output: {'name: 'Zed', 'age': 39, 'height': 74}
#Also wurden hier das Element mit der Bez. City, sowie das Element mit dem
# Namen (!!) 1 und das Element mit dem "Namen" 2 ! Siehe z.39 bis 47!
