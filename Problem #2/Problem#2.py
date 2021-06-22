database = {}   
# A dict. to store phone numbers with checked-in place 
freq = {"Mahamakut Bld." : 0, "Sara Phra Keaw" : 0, "CU Sport Complex" : 0, "Sanam Juub" : 0, "Samyan Mitr Town" : 0}
# A dict. to store frequencies of each place
places = ["Mahamakut Bld.", "Sara Phra Keaw", "CU Sport Complex", "Sanam Juub", "Samyan Mitr Town"]

# return a place where that phone number checked in, or "" if not.
def CheckedInAt(phoneNum):
    if phoneNum in database:
        return database[phoneNum]
    return ""
    
# if a phone number is in the database, remove it and decrease the population of the place- 
# where that number belong to.
def checkOut(phoneNum):
    if phoneNum in database:
        freq[database[phoneNum]] -= 1
        database.pop(phoneNum)
        print(phoneNum,"is checking out")
    else:
        print("You've not checked in yet!")

# if a phone number haven't checked in yet, add it to database with corresponding place and update population
# or, change the location and population if that number checks in to new place
# or, print warning message if that number check in at the same place 
def CheckIn(phoneNum, place):
    if (CheckedInAt(phoneNum) == place):
       return print("You've already checked in at",place)
    elif (CheckedInAt(phoneNum) == ""):
        database[phoneNum] = place
        freq[database[phoneNum]] += 1
        return print(phoneNum,"is checking in at",place)
    else:
        freq[database[phoneNum]] -= 1   # reduce the population of the old place by 1
        database[phoneNum] = place      # change database of the number to new place
        freq[database[phoneNum]] += 1   # add the population to the new place
        return print(phoneNum,"is checking in at",place)
        
#print current population for each place
def CurrentPop():
    for i in range(5):
        print(f"{i+1}. {places[i]} : {freq[places[i]]}")
    
#looping to show the menu for user
while(True):
    print("Welcome to CHULA CHANA")
    print("Available features : \n\t0. Exit the program\n\t1. Check in\n\t2. Check out\n\t3. Current Population")
    inputNum = input("Please select a number : ")
    print("----------------------------------")

    if(inputNum == "0"):
        break
    if(inputNum == "1"):
        print("Menu -> Check in\n")
        phoneNum = input("Please enter your phone number : ")
        print("\t1. Mahamakut Bld.\n\t2. Sara Phra Keaw\n\t3. CU Sport Complex\n\t4. Samyan Mitr Town\n\t5. Sanam Juub")
        placeNum = int(input("Select a place to check in: "))
        CheckIn(phoneNum, places[placeNum-1])
        print("----------------------------------")
    elif(inputNum == "2"):
        print("Menu -> Check out\n")
        phoneNum = input("Please enter your phone number : ")
        checkOut(phoneNum)
        print("----------------------------------")
    elif(inputNum == "3"):
        print("Menu -> Current Population\n")
        CurrentPop()
        print("----------------------------------")
    else:
        print("Please select a valid number!!")
        print("----------------------------------")

