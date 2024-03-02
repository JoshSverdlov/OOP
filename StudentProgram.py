import StudentClass as s

def main():
    my_student = s.Student(8911155,'John','02/28/1999','Junior')

    my_student.calc_current_age()
    my_student.calc_registration()
    print(f"{my_student.get_name()} you are {my_student.get_current_age()} years old. You may register on the following dates: {my_student.get_registration()}")

main()
