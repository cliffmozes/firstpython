temp1=int(input("Enter Temp1: "))
temp2=int(input("Enter Temp2: "))
temp3=int(input("Enter Temp3: "))
def celcious_to_farenheight(degrees):
    farenheight = degrees * (9/5) + 32
    return farenheight

c=[temp1,temp2,temp3]
for tem in c:
    if celcious_to_farenheight(tem) < -275:
        
        print("Temp is too low")
        
    else:
            
        print(celcious_to_farenheight(tem))