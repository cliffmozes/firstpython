from Test_functions import weather
temp1=int(input("Enter Temp1"))
temp2=int(input("Enter Temp2: "))
temp3=int(input("Enter Temp3: "))


c=[temp1,temp2,temp3]
for tem in c:
    if weather(tem) < -275:
        
        print("Temp is too low")
        
    else:
            
        print(weather(tem))