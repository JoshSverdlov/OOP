class Car:
        
    def __init__(self,y,m):
        self.__year_model = y
        self.__make = m
        self.__speed = 0

    def calc_accelerate(self):
        self.__speed += 5

    def calc_break(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make