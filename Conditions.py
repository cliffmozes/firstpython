age = input("Enter your age: ")
if int(age) < 40:
    if int(age) < 10:
        if int(age) < 2:
            print("infant")
        else:
            print("baby")
    else:
        print("young man")

else:
    print("Old Man")

