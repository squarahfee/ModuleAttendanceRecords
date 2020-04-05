import Load_data
import Main_Menu

# to check the login/password, we will need 4 bits of data
# 1. User's input login name = (u_lname)
# 2. User's input password  = (u_lpass)
# 3. Login  name list   = (name_l)
# 4. Password list  = (pass_1)

# first get the required data and load it to the password check

def pass_check(u_lname, u_lpass):
    # get the lists from 'Load data'
    name_l, pass_l = Load_data.load_data()
    # create a variable as false to handle no True return
    # start a for loop to match the login name and get its index number
    state = "yes"
    for i, lname in enumerate(name_l):
        if u_lname == lname:
            # change the check variable to True
            # if the username exists in the list, return it's index
            final_check(i, u_lpass, pass_l, u_lname)
            state = "not"
            # state gets changed to different string
            # if the wrong name is used, the state will remain 'yes' and prompt again for login
    if state == "yes":
        print("Login doesn't exist, please try again")
        # send's you back to the login again
        # uses the login without the introduction
        login_two()


# the same as login(), but used when a login/pass is incorrect
# Doesn't have the welcome greeting
def login_two():
    Lname = input("Please provide your login name...")
    Lpassw = input("Please provide you user password...")
    pass_check(Lname, Lpassw)

# The final check finds the associated password for the login by index
# If else statement used
# If the password matches you get sent to the main menu
# Else, they are sent back to the login menu (without the greeting)
def final_check(i, u_lpass, pass_l, u_lname):
    print("checking password")
    fpass = pass_l[i]
    if (u_lpass == fpass):
        print("Password correct, redirecting you to the main menu...")
        Main_Menu.main_menu(u_lname)
    else:
        print("Password incorrect, please enter your credentials again")
        login_two()
