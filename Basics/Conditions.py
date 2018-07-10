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


#Condition within a function
def celcious_to_farenheight(degrees):
    farenheight = degrees * (9/5) + 32
    return farenheight


degrees = int(input("Please enter the temp: "))
if celcious_to_farenheight(degrees) > -273:
    print("The temp in Farenheight is", celcious_to_farenheight(degrees))
else:
    print("The temp is too low")
    
    

# length of string function