class Car:
    condition = 'new'

    def __init__(self, model, colour, apg):

        self.model = model
        self.color = colour
        self.apg = apg

    def display_car(self):

        """print("this car is a {0} {1} with {2} apg".format(self.color, self.model,self.apg))"""
        #  print( "the car is a", self.color, "colour car of model", self.model, "with apg", self.apg)

    def drive_car(self):
        self.condition = 'used'


class Electric(Car):
    """ def __init__(self, battery_type, model, colour, apg):
        self.battery = battery_type
        self.model = model
        self.color = colour
        self .apg = apg"""

    def __repr__(self):   # we cannot return a value from _init_ but it can be done by _repr_
        return "this car is a {0} {1} with {2} apg".format(self.color, self.model, self.apg)

    def drive_car(self):
        self.condition = 'like new'
        return self.condition

my_car = Electric('pmw', 'red', 'ss')
print(my_car.condition)
# print(my_car.drive_car())
# print(my_car.condition)
print(my_car.model)
print(my_car.color)
# my_car.display_car()
print(my_car)   # returns the statement to the object from the Electric class





