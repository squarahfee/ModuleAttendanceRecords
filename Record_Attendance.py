import Choose_Again
import Load_data
import time


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
    choice = 0
    SELECT = []
    print("=========================================")
    print("Which module would you like to record?...")
    for i, code in enumerate(mod_code):
        print(str(choice)+". "+code+": "+mod_name[i])
        choice = choice + 1
        SELECT.append(choice)
    print(SELECT)
    while True:
        choice = int(input("Choose a number.... "))
        if choice in SELECT:
            module = choice
            break
        else:
            print("Not a valid choice, Please try a number and press enter")
            time.sleep(.1)
    for i, smodule in enumerate(SELECT):
        if smodule == module:
            print(mod_code[i], mod_name[i], user_name)
            record(mod_code[i],mod_name[i], user_name)
        else: print("Something went wrong, please restart")
        time.sleep(.1)




def record(code, module, user_name):
    print("======="+code+"=======")
    print("=========="+module+"==========")
    print("Please update the students attendance records for...")
    codefile = code+".txt"
    destination = open(codefile, "r+") #using r+ to both read and write to the file
    student_name, latest_stat, no_present, no_absent, no_excuse = Load_data.load_attendees(codefile)
    final_student = []
    try:
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
            final = ""
            if choice == 1:
                no_present = int(no_present[i])
                new_present = str(no_present + 1)
                new_excuse = str(no_excuse[i])
                new_absent = str(no_absent[i])
                latest_stat = int(latest_stat[i])
                new_stat = str(latest_stat + 1)
                # no_excuse[i] = sum(int(no_excuse), 1)
                final = "".join(student_name)+",".join(new_stat)+",".join(new_present)+",".join(new_absent)+",".join(new_excuse)+""
            elif choice == 2:
                #append on [2]
                no_absent = int(no_absent[i])
                new_absent = str(no_absent + 1)
                n_excuse = str(no_excuse[i])
                new_present = str(no_present[i])
                latest_stat = int(latest_stat[i])
                new_stat = str(latest_stat + 1)
                # no_excuse[i] = sum(int(no_excuse), 1)
                final = "".join(student_name)+",".join(new_stat)+",".join(new_present)+",".join(new_absent)+",".join(n_excuse)+""
            # no_absent[i] = sum(int(no_absent), 1)
            elif choice == 3:
                # append on [3]
                no_excuse = int(no_excuse[i])
                new_excuse = str(no_excuse+1)
                new_absent = str(no_absent[i])
                new_present = str(no_present[i])
                latest_stat = int(latest_stat[i])
                new_stat = str(latest_stat+1)
                # no_excuse[i] = sum(int(no_excuse), 1)
                final = "".join(student_name)+",".join(new_stat)+",".join(new_present)+",".join(new_absent)+",".join(new_excuse)+""
            final_student.append(final)
        for record1 in final_student:
            destination.write(record1)
    except:
        time.sleep(.1)
        print("--------------------NOTICE----------------------------------------")
        time.sleep(.1)
        print("I was unable to complete this section without error getting an error")
        time.sleep(.1)
        print("I am able to update the the first line for the first student, however, this seems to clear the lists I created from reading the file.")
        time.sleep(.1)
        print("I am left with an empty list (from what I understand)")
        time.sleep(.1)
        print("I added this catch all to make it look a bit nicer instead of erroring out")
        print("--------------------NOTICE----------------------------------------")
    destination.close()
    Choose_Again.choose_again(user_name)
