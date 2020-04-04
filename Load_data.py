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



