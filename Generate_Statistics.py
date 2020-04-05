import Choose_Again

# calculate and store the total number of enrolled
# calculate and store the total number of classes to date
# identify and store the names of any non-attender(s)
# identify and store the names of the best attender(s)
# calculate and store the average attendance
# rate overall identify and store the names of student(s) with an attendance rate of under 70%
# Print all this data to the screen and to a file


# Module: SOFT_6017
# Number of students: 3
# Number of Classes: 10
# Average Attendance: 5.0 days
# Low Attender(s): under 70.0 %
# Alan Lowe
# Non Attender(s):
# Alan Wilson
# Best Attender(s):
# Attended 10/10 days
# Mary Martin

def generate_statistics(user_name):
    print("====Generate Statistics====")
    #request details on the class
    #which class do you wanna see
    #give list
    user_file = user_name+"_modulelist.csv"
    print("Which subject would you like to view?...")
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
    read_data(name_of_file, user_name)
    # finish this by asking if you would like to exit or return to the main menu


def read_data(name_of_file, user_name):
    names_list = []
    present_list = []
    absent_list = []
    excused_list = []
    with open(name_of_file) as connection:
        for line in connection:
            line_data = line.split(',')
            names_list.append(line_data[0])
            present_list.append(int(line_data[1]))
            absent_list.append(int(line_data[2]))
            excused_list.append(int(line_data[3]))
    return names_list, present_list, absent_list, excused_list
    for i, names in enumerate(names_list):
        print("The student "+names+" has been present for "+present_list[i]+" classes, absent "+absent_list[i]+" times and excused "+excused_list+" times")
    Choose_Again.choose_again(user_name)

