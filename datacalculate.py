import os
os.system('cls')
print("Warning! Defult unit is iB(1024B=1KB)")
inputdataunit = input("Please enter input data unit(ex: G, GG(G*G), T): ")
unit = list(inputdataunit)
inputmultiplier = 0
for i in range(len(inputdataunit)):
    if unit[i] == 'K':
        inputmultiplier += 10
    elif unit[i] == 'M':
        inputmultiplier += 20
    elif unit[i] == 'G':
        inputmultiplier += 30
    elif unit[i] == 'T':
        inputmultiplier += 40
    elif unit[i] == 'P':
        inputmultiplier += 50
    elif unit[i] == 'E':
        inputmultiplier += 60
    elif unit[i] == 'Z':
        inputmultiplier += 70
    elif unit[i] == 'Y':
        inputmultiplier += 80
    elif unit[i] == 'R':
        inputmultiplier += 90
    elif unit[i] == 'Q':
        inputmultiplier += 100
inputnumber = input(f"Please enter number(<here>{inputdataunit}iB): ")
recheck = input(f"Are you sure input number is {inputnumber}{inputdataunit}iB?(Y/N): ")
if recheck == "Y" or recheck == "y":
    outputdataunit = input("Please enter output data unit(ex: G, GG(G*G), T): ")
    unit = list(outputdataunit)
    outputmultiplier = 0
    for i in range(len(outputdataunit)):
        if unit[i] == 'K':
            outputmultiplier += 10
        elif unit[i] == 'M':
            outputmultiplier += 20
        elif unit[i] == 'G':
            outputmultiplier += 30
        elif unit[i] == 'T':
            outputmultiplier += 40
        elif unit[i] == 'P':
            outputmultiplier += 50
        elif unit[i] == 'E':
            outputmultiplier += 60
        elif unit[i] == 'Z':
            outputmultiplier += 70
        elif unit[i] == 'Y':
            outputmultiplier += 80
        elif unit[i] == 'R':
            outputmultiplier += 90
        elif unit[i] == 'Q':
            outputmultiplier += 100
    print(inputmultiplier)
    print(outputmultiplier)
    print(f"{inputnumber}{inputdataunit}iB = {int(inputnumber) * (2 ** (inputmultiplier - outputmultiplier))}{outputdataunit}iB, ")
    print(f"{inputnumber}{inputdataunit}iB = {int(inputnumber)} * (2 ** {inputmultiplier})B")
    print(f"{inputnumber}{inputdataunit}iB = {int(inputnumber) * (2 ** inputmultiplier)}B")
    print(f"{inputnumber}{inputdataunit}iB = {int(inputnumber) * (2 ** inputmultiplier) * 8}b")
    print(f"The number of numbers that can come from {inputnumber}{inputdataunit}iB = {int(inputnumber) * (2 ** inputmultiplier) * 256}")
else:
    os.system('cls')