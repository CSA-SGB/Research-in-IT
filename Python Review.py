import random

def random_numbers():
    numbers=[] #Empty list to hold numbers
    x=0 #Starting places for the while loop

    while x<10:
        num=random.randrange(0, 50, 1) #Creates a random number between 0 & 50
        #Checks list for the created number
        #If the created number is already there do nothing with it
        if num not in numbers:
            numbers.append(num)
            x=x+1
    print (numbers)

def car_example():
    class Car:

        def __init__(self, color, year, top_speed): #Initializing the class
            self.color=color
            self.year=year
            self.top_speed=top_speed

        def set_color(self, color): #Changes color to the input
            self.color=color

        def set_year(self, year): #Changes year to the input
            self.year=year

        def set_top_speed(self, top_speed): #Changes top speed to the input
            self.top_speed=top_speed

        def print_car(self): #Prints off the car with all entered traits
            print("You have a "+self.color+" car from "+self.year+" that can go "+self.top_speed+" miles per hour.")



    car1= Car("none", "0000", "00") #Setting up a 'blank' car

    color=input("What color is the car?: ") #Gets color
    car1.set_color(color)

    year=input("What year is the car?: ") #Gets year
    car1.set_year(year)

    top_speed=input("Whar is the car's top speed?: ") #Gets speed
    car1.set_top_speed(top_speed)

    car1.print_car() #Calls print_car in Car class


random_numbers()
car_example()
