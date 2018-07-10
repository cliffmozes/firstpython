# defining the Function, Minutes here is the input, hours is the variable, the function returns the variable
input_mins = input("Please eater the number of minutes: ")

def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

print("In",int(input_mins),"There are",minutes_to_hours(int(input_mins)),"Hours")

#This function here returns the number of seconds in that hour from the function above
def hours_to_seconds(hours):
    seconds = hours * 60 * 60
    return seconds

b = minutes_to_hours(int(input_mins))

print(hours_to_seconds(b))

#Convert celcious to string
def celcious_to_farenheight(degrees):
    farenheight = degrees *(9/5) + 32
    return farenheight

degrees = input("Please enter the temp: ")

print("The temp in Farenheight is",celcious_to_farenheight(int(degrees)))

#length of string function
def length(word):
    wordlength = len(word)
    return wordlength
word = input("Please enter the word: ")

print("The length of th word is",length(word))
