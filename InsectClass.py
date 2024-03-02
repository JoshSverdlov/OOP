import random

class Insect:

    def __init__(self,w,l,n):
        self.__wings = w
        self.__legs = l
        self.__flight = 0
        self.__name = n

    def calc_flight(self): #mutator(changes value)
        self.__flight = random.randint(1,10)

    def get_miles(self): #accesor
        return self.__flight
    
    def get_name(self): #accesor
        return self.__name

#attribute = variable