import lpass_check

def login():
    print("Welcome to Module Attendance Records")
    print("====================================")
    Lname = input("Please provide your login name...")
    Lpassw = input("Please provide you user password...")
    lpass_check.pass_check(Lname, Lpassw)


def main():
    login()

main()