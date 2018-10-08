# Introduce todo list - give options
#note - the day entry and checking is repeated in each of the get and add sections. I would write a function for this but not yet
print("Welcome to your to-do list. Your options are: add, get and quit")
#Initialize entry and Dictionary with weekday names
loop = True
todo = {}
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
todo = dict.fromkeys(days)
#I used a for loop to initialize the lists for the days to avoid typing out all the empty lists for each item in the dictionary
for day in days:
    todo[day]=[]

#Loop while they don't want to quit
while loop:
    #ask what they want to do
    entry = input("What would you like to do? \n>")
    if entry.lower()=="quit":
        print("Ending program. Thank you for using the to-do list!")
        loop = False
    #add action
    elif entry.lower()=="add":
        #get day input
        day = input("What day? \n>")
        day2 = day.lower()
        #error check for day, repeat until correct
        while day2 not in days:
            print("Invalid entry - please enter a correct day of the week (like Monday or monday).")
            #get a corrected day
            day = input("What day? \n>")
            day2 = day.lower()

        #continue with adding and append to list for that day
        printday = "What would you like to add to "+day2.capitalize()+"'s to-do list? \n>"
        action = input(printday)
        todo[day2].append(action)

    #get action
    elif entry.lower()=="get":
        #get day input and do error checking
        day = input("What day? \n>")
        day2 = day.lower()
        #error check for day, repeat until correct
        while day2 not in days:
            print("Invalid entry - please enter a correct day of the week (like Monday or monday).")
            #get a corrected day
            day = input("What day? \n>")
            day2 = day.lower()

        #Output todo list for that day, check for empty list:
        if not todo[day2]:
            print("You have nothing to do that day. HAVE FUN!")
        elif len(todo[day2]) == 1:
            #print("On ", day2.capitalize()," you have to", todo[day2][0],".")
            print(f"On {day2.capitalize()} you have to {todo[day2][0]}.")
        else:
            print("On ",day2.capitalize()," you have to:")
            for item in range(len(todo[day2])):
                print(todo[day2][item].capitalize())

    #error check for invalid action
    else:
        print("Invalid entry. Please try again. Use add, get or quit")
