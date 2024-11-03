'''Application name:GPA Analizer
   Author:  Jasmine Pulver
   Date: 10/28/2024
   Description: This program will ask the user to enter their last name, first name, and GPA.
   The program will then determine if the student made the Dean's List, Honor Roll, or neither.
   The program will continue to run until the user enters ZZZ as the last name.''' 

def StudentGPA():
    print("Welcome to the GPA Analysis")
    print()
    while True:
        l_name = input("Please enter last name: ")
        if l_name.upper() == "ZZZ": 
            break
        f_name = input("Please enter first name: ")
        gpa = float(input("Please enter GPA: "))
        # determines if the student's GPA is 3.5 or greater
        if gpa >= 3.5:
            print(f"{f_name} {l_name} has on the Dean's List!")
        # determines if the student's GPA is 3.25 or greater
        elif gpa >= 3.25:
            print(f"{f_name} {l_name} has on the Honor Roll!")
        # determines if the student's GPA qualifies
        else:
        # I put a response statement if they didnt make it
            print(f"Sorry {f_name} {l_name} you are not on the Dean's List or the Honor Roll.")
            continue
StudentGPA()