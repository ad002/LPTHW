cars = 100

#Variablen könenn als Int initialisiert werden
space_in_car = 4

#Oder als Float
space_in_car=4.0

drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passenger_per_car = passengers/ cars_driven

#Auch Variablen könenn im Print Befehl mit aufgenommen werden,
#wenn sie mit , getrennt werden
print("There are", cars, "cars available")

print("There are only", drivers, "drivers available")

print("There will be", cars_not_driven, "Cars available")

print("We have", passengers,"to carpool today")

print("We need to put about", average_passenger_per_car, "persons in each car")
