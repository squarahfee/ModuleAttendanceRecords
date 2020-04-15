# loads username/password
def load_data():
    l_name = []
    l_passw = []
    data_file = open("Login_data.txt", "r")
    for user_data in data_file:
        user_data = user_data.rstrip()
        line_info = user_data.split(",")
        l_name.append(line_info[0])
        l_passw.append(line_info[1])
    return l_name, l_passw


# Loads the student record data
def load_attendees(student_data):
    student_name = []
    latest_stat = []
    no_present = []
    no_absent = []
    no_excuse = []
    data_file = open(student_data, "r")
    for user_data in data_file:
        user_data = user_data.rstrip()
        line_info = user_data.split(",")
        student_name.append(line_info[0])
        latest_stat.append(line_info[1])
        no_present.append(line_info[2])
        no_absent.append(line_info[3])
        no_excuse.append(line_info[4])
    return student_name, latest_stat, no_present, no_absent, no_excuse

# Loads Module data
def load_module(module_data):
    Mod_name = []
    Mod_Code = []
    data_file = open(module_data, "r")
    for user_data in data_file:
        user_data = user_data.rstrip()
        line_info = user_data.split(",")
        Mod_name.append(line_info[0])
        Mod_Code.append(line_info[1])
    return Mod_name, Mod_Code


