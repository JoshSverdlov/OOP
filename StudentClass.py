from datetime import datetime

class Student:

    def __init__(self,id,n,d,c):
        self.__id = id
        self.__name = n
        self.__dob = d
        self.__classification = c
        self.__age = 0

    def calc_current_age(self):
        today = datetime.now().year
        splitdob = self.__dob.split('/')
        self.__age = today - int(splitdob[2])

    def calc_registration(self):
        if self.__classification == 'Senior':
            self.__reg = '4/1 thru 4/3'
        elif self.__classification == 'Junior':
            self.__reg = '4/4 thru 4/6'
        elif self.__classification == 'Sophomore':
            self.__reg = '4/7 thru 4/9'
        else:
            self.__reg = '4/10 thru 4/12'


    def get_current_age(self):
        return self.__age
    
    def get_registration(self):
        return self.__reg
    
    def get_name(self):
        return self.__name