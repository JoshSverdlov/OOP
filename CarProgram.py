import CarClass as c
def main():
    car_obj = c.Car(2015, 'Toyota')

    car_obj.calc_accelerate()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_accelerate()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_accelerate()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_accelerate()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_accelerate()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")

    car_obj.calc_break()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_break()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_break()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_break()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")
    car_obj.calc_break()
    print(f"The {car_obj.get_year_model()} {car_obj.get_make()} is currently going {car_obj.get_speed()}mph!")

main()