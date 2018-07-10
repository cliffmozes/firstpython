#Advanced function {Functions with Multiple parameters}
input_mins = input("Please eater the number of minutes: ")
input_seconds = input("Please enter the number of seconds: ")

def minutes_to_hours(minutes,seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

#When you call the function, make sure all the parameters are passed
print(minutes_to_hours(int(input_mins),int(input_seconds)))