import Choose_Again

# for each student:
#     store the status for today present/absent/absent+excuse
#     update the data for this person each of the lists
# store the lists back to the file.

def record_attendance():
    print("====Record attendance====")
    #request details on the class
    #which class do you wanna see
    #give list
    user_file = user_name+"_modulelist.csv"
    print("Which module would you like to record?...")
    with open(user_file) as connection:
        for i, line in enumerate(connection):
            print(i+". "+connection)
                #create file name
        menu = "Choose a number.... "
        # create valid input variables to make sure you get the right choice
        SELECT = len(connection)
        # while loop to prompt until the correct choice is made
        while True:
            choice = int(input(menu))
            if choice in SELECT:
                module = connection[choice]
                break
            else:
                print("Not a valid choice, Please try a number and press enter")
    name_of_file = user_name+module+".txt"
    record_data(name_of_file, user_name, module)

def record_data(name_of_file, user_name, module):
    print("=========="+module+"==========")
    print("Please update the students attendance records for...")
    destination = open(name_of_file, 'w’)
    for name in user_name:
        menu = "Student #"+n+": "+name \
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
            destination.write()
        elif choice == 2:
            #append on [2]
            destination.write()
        elif choice == 3:
            # append on [3]
            destination.write()
    destination.close()

    # finish this by asking if you would like to exit or return to the main menu
    # choose which module to use
    # will read from the users modules list
    # file will be named name.modules.txt
    # Print out list
    # loadmoduledata() = variable
    # for each line, assign a number to each, incremental
    # return the index plus the

    # finish this by asking if you would like to exit or return to the main menu
    Choose_Again.choose_again(user_name)