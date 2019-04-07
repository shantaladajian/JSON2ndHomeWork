import json
import os

def loadSetupData():
    with open('gc_setup.json') as file:
        course = json.load(file)
    
    user_setup = course["course_setup"]["grade_breakdown"]
    return user_setup

def loadUserGradesData():
    a = os.listdir()
    if "gc_grades.json" in a:
        with open('gc_grades.json') as data_file:
            try:
                user_grades = json.load(data_file)
                return user_grades
            except json.decoder.JSONDecodeError:
                print('Your file is empty!')
    else:
        print('File doesnt exist!')



def askForAssignmentMarks(grades, current_grades):
    if current_grades is None:
        current_grades = {"mygrades": {}}
        for key in grades:
            print("\nPercent for", key, "is", grades[key])
            current_grades["mygrades"][key] = float(input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet"))
            if current_grades["mygrades"][key] > 100 or current_grades["mygrades"][key] < -1:
                print("Sorry. You must input an integer(your grade) between 0 and 100. Please insert -1 if you don't have a grade yet ")
                current_grades["mygrades"][key] = float(input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet"))
        else:
            for key in grades:
                print("\nPercent for", key, "is", grades[key])
                print("\nYour grade for", key, "is", current_grades["mygrades"][key])
    else:
        for key in grades:
            d = float(current_grades["mygrades"][key])
            if d > -1:
                print("your current grade for "+key+"is:", float(current_grades["mygrades"][key]))
                update = input("Do you want to change? Please answer in 'yes' or 'no'. ")
                if (update == "no" or update == "'no'"):
                    print(" Okey. You can change it whenever you want :) ")
                elif (update == "yes" or update == "'yes'"):
                    current_grades["mygrades"][key] = float(input("What is your Current Grade in numerical form,  for: " + key + " . Please insert -1 if you don't have a grade yet"))
                    if current_grades["mygrades"][key] > 100 or current_grades["mygrades"][key] <-1:
                        print("Sorry. You must input your grade between the numbers 0 and 100. Please insert -1 if you don't have a grade yet ")
                        current_grades["mygrades"][key] = float(input("What is your Current Grade in numerical form,  for: " + key + " . Please insert -1 if you don't have a grade yet"))

    return current_grades


def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades):
    curr_grade = 0
    if current_grades is None:
        print('Your GPA cant be calculated')
    else:
        for key in current_grades["mygrades"]:
            if float(current_grades["mygrades"][key]) != -1:
                calc_grade = int(current_grades["mygrades"][key]) * grades[key] / 100
                curr_grade = curr_grade + calc_grade
    print("\nYour GPA is: ", curr_grade)



def main():
    grades_setup = loadSetupData()
    user_grades = loadUserGradesData()
    printCurrentGrade(grades_setup, user_grades)
    current_grades = askForAssignmentMarks(grades_setup, user_grades)
    saveGrades(current_grades)
    printCurrentGrade(grades_setup, current_grades)

main()
