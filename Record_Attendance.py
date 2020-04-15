import Choose_Again
import Load_data


# for each student:
#     store the status for today present/absent/absent+excuse
#     update the data for this person each of the lists
# store the lists back to the file.

def record_attendance(user_name):
    print("====Record attendance====")
    #request details on the class
    #which class do you wanna see
    #give list
    user_file = user_name+"_modulelist.csv"
    mod_name, mod_code = Load_data.load_module(user_file)
    choice = 1
    SELECT = []
    print("=========================================")
    print("Which module would you like to record?...")
    for i, name, code in mod_name, enumerate(mod_code):
        print(choice+". "+code+": "+name)
        choice + 1
        SELECT.append(choice)
    while True:
        choice = int(input("Choose a number.... "))
        if choice in SELECT:
            module = choice
            break
        else:
            print("Not a valid choice, Please try a number and press enter")
    for i, smodule in enumerate(SELECT):
        if smodule == module:
            record(mod_code[i],mod_name[i], user_name)
        else: print("Something went wrong, please restart")




def record(code, module, user_name):
    print("======="+code+"=======")
    print("=========="+module+"==========")
    print("Please update the students attendance records for...")
    codefile = code+".txt"
    student_name, latest_stat, no_present, no_absent, no_excuse = Load_data.load_attendees(codefile)
    destination = open(codefile, "w")
    for i, name in enumerate(student_name):
        print("Attendance record for "+name)
        menu = "Mark this student as" \
               "\n\t1: Present" \
               "\n\t2: Absent" \
               "\n\t3: Excused" \
               "\n==> "
        # create valid input variables to make sure you get the right choice
        SELECT = (1, 2, 3)
        # while loop to prompt until the correct choice is made
        while True:
            choice = int(input(menu))
            if choice in SELECT:
                break
            else:
                print("Not a valid choice, Please try a number and press enter")
        if choice == 1:
            #append on [1]
            no_present + 1
        elif choice == 2:
            #append on [2]
            no_absent + 1
        elif choice == 3:
            # append on [3]
            no_excuse + 1
        destination.writeline(student_name[i]+","+latest_stat[i]+","+no_present[i]+","+no_absent[i]+","+no_excuse)
    destination.close()
    Choose_Again.choose_again(user_name)
