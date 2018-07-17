password = ""
c=["moses","Cliff"]
while password not in c:
    password = input("Please enter you password: ")
    if password in c:
        print("logged in")
    else:
        print("Wrong Password")
