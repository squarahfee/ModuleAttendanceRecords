import Main_Menu

# used to redirect the user back to the main menu after completing choice
# seperate module used to avoid bad practice of importing the same module back and forth
# between two modules

def choose_again(Lname):
    name = Lname
    Main_Menu.main_menu(name)