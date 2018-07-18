# for loops
# array
fnames = ["moses@gmail.com", "Cliff@gmail.com ", "Mwanga@hotmail.com"]

# name is a variable for each item in the array
for name in fnames:

    if "gmail" in name:
     print(name)


# loop in in a function with user input
an = input("Enter Lower number: ")
bn = input("Enter Upper number: ")
def mylist(lower,upper):
 
    return an,bn
#Convert input values in an array
c =[an,bn]    
for n in c:
    print(n)
# 2. loop in in a function with user input
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
# looping in multiple lists
# for loops
# array
fnames = ["moses", "Cliff", "Mwanga"]
snames= ["Hello","This","Is"]

# name is a variable for each item in the array
for f,s in zip(fnames,snames):
    
    #if "gmail" in name:
     print(f,s)
    
#For loop in function

temp=[10,-10,-289,100]

def celcius_to_farenheight(degrees):
    farenheight = degrees * (9/5) + 32
    return farenheight


for tem in temp:
    if celcius_to_farenheight(tem) < -275:
        
        print("Temp is too low")
        
    else:
            
        print(celcius_to_farenheight(tem))

