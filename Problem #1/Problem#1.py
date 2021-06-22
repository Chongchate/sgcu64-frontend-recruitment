
#Lists that store the display symbols for each line
firstLine  =  [" __ ","    "," __ "," __ ","    "," __ "," __ "," __ "," __ "," __ "]
secondLine =  ["|  |","   |"," __|"," __|","|__|","|__ ","|__ ","   |","|__|","|__|"]
thirdLine  =  ["|__| ","   |","|__ "," __|","   |"," __|","|__|","   |","|__|"," __|"]

while(True):
    inputTime = input("Enter an input in format of xx:xx:xx \n--> ")

    #Check if the input is valid then display the corresponding time
    if((0<=int(inputTime[:2])<=99) and (0<=int(inputTime[3:5])<=59) and (0<=int(inputTime[6:8])<=59) and (inputTime[2]==inputTime[5]==":")):
        print(firstLine[int(inputTime[0])],firstLine[int(inputTime[1])]," ",firstLine[int(inputTime[3])],firstLine[int(inputTime[4])]," ",firstLine[int(inputTime[6])],firstLine[int(inputTime[7])])
        print(secondLine [int(inputTime[0])],secondLine [int(inputTime[1])],"·",secondLine [int(inputTime[3])],secondLine [int(inputTime[4])],"·",secondLine [int(inputTime[6])],secondLine [int(inputTime[7])])
        print(thirdLine [int(inputTime[0])],thirdLine [int(inputTime[1])],"·",thirdLine [int(inputTime[3])],thirdLine [int(inputTime[4])],"·",thirdLine [int(inputTime[6])],thirdLine [int(inputTime[7])])

    else:
        print("        ·          ·        ")
        print("__  __  ·  __  __  ·  __  __")

