# for loops
# array
names = ["moses@gmail.com", "Cliff@gmail.com ", "Mwanga@hotmail.com"]

# name is a variable for each item in the array
for name in names:

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