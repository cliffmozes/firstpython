# defining the Function, Minutes here is the input, hours is the variable, the function returns the variable
a = input("Please eater the number of minutes: ")
def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

print("In",int(a),"There are",minutes_to_hours(int(a)),"Hours")

#This function here returns the number of seconds in that hour from the function above
def hours_to_seconds(hours):
    seconds = hours * 60 * 60
    return seconds

b = minutes_to_hours(int(a))

print(hours_to_seconds(b))