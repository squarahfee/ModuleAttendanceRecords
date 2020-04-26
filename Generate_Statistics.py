import Choose_Again
import Load_data
import time

# for each student:
#     store the status for today present/absent/absent+excuse
#     update the data for this person each of the lists
# store the lists back to the file.

def generate_statistics(user_name):
    print("====Generate Statistics====")
    time.sleep(.1)
    #request details on the class
    #which class do you wanna see
    #give list
    user_file = user_name+"_modulelist.csv"
    mod_name, mod_code = Load_data.load_module(user_file)
    choice = 1
    SELECT = []
    print("=========================================")
    time.sleep(.1)
    print("Which records would you like to view?...")
    time.sleep(.1)
    for i, code in enumerate(mod_code):
        print(str(choice)+". "+code+": "+mod_name[i])
        choice = choice + 1
        SELECT.append(choice)
    while True:
        choice = int(input("Choose a number.... "))
        time.sleep(.1)
        if choice in SELECT:
            module = choice
            break
        else:
            time.sleep(.1)
            print("Not a valid choice, Please try a number and press enter")
    for i, smodule in enumerate(SELECT):
        if smodule == module:
            generate(mod_code[i],mod_name[i], user_name)





def generate(code, module, user_name):
    print("======="+code+"=======")
    time.sleep(.1)
    print("=========="+module+"==========")
    time.sleep(.1)
    print("Statistics for the module  are as follows:")
    time.sleep(.1)
    codefile = code+".txt"
    student_name, latest_stat, no_present, no_absent, no_excuse = Load_data.load_attendees(codefile)
    destination = open(codefile, "r")
    student_len = number_of_students(student_name)
    attend_avg = average_attendance(no_present, student_len)
    lowest = low_attendars(student_name, no_present, latest_stat[1])
    highest = best_attendars(student_name, no_present, latest_stat[1])
    for i, name in enumerate(student_name):
        print("Attendance record for "+name)
        time.sleep(.1)
        print("Number of present: "+no_present[i])
        time.sleep(.1)
        print("Number of absent: "+no_absent[i])
        time.sleep(.1)
        print("Number of excused absent: "+no_excuse[i])
        time.sleep(.1)
        print("=====================================")
        time.sleep(.1)
        print("=====================================")
        time.sleep(.1)
    print("Latest statistics for this class are: ")
    time.sleep(.1)
    print("Number of students in this module = "+str(student_len))
    time.sleep(.1)
    print("Number of classes = ".join(latest_stat[1]))
    time.sleep(.1)
    print("Average class attendance = "+attend_avg)
    time.sleep(.1)
    print("Lowest attender = ")
    time.sleep(.1)
    for person in lowest:
        print("=="+person)
        time.sleep(.1)
    print("Highest attender = ")
    time.sleep(.1)
    for person in highest:
        print("=="+person)
    destination.close()
    Choose_Again.choose_again(user_name)

#gets the number of student records and returns as int
def number_of_students(number):
    #num of stud
    result = len(number)
    return result

#calculate the average attendance
#takes a list of the attendances
#sums them, then divides by the num of students
def average_attendance(no_present, student_len):
    #tpresent = int(no_present)
    #tpresent = sum(tpresent)
    #total = tpresent/student_len
    total = "2"
    return total

def low_attendars(student_name, no_present, classtotal):
    #under 70%
    present = no_present
    print(present)
    people = []
    a = int(classtotal)
    #get 70% of the classtotal for comparison
    seventy_percent = a / 0.70
    for i, student in enumerate(student_name):
        if int(present[i]) < seventy_percent:
            #if the example is less than, append it to the list to be returned
            people.append(student)
    return people

#takes the students total attendences
#compare them to see if they match the total classes
#return a list of names who match
#if no matchs, return "No Students" string
def best_attendars(student, student_record, total):
    people = []
    for i, student in enumerate(student):
        if student_record[i] == total:
            people.append(student)
    if not people:
        people = ["No students"]
        return people


