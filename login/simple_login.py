try:
    users = [['alvin', 'a123'],['ben', 'gh_3tw'],['Chris', '@quc98']]

    def login(users):
        while True:
            username = input("Please enter a username: ")
            password = input("please enter a password: ")

            for u in users:
                if username == u[0] and password == u[1]:
                    return username
            print("username or password is not correct. Please try again!")

    username = login(users)

    print(username, "has logged in.")
except:
    print("An exception occured.")