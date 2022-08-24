Loop = True
while Loop:
    InputNumber = input("Enter any number to begin sequence. Type '?' for help. You cannot use special characters.")
    if InputNumber.isalpha():
        print("You can only enter numbers.")
    elif InputNumber == "0":
        print('You cannot enter 0. This will trigger an infinite loop of 0s.')
    elif InputNumber == '?':
        print("This is the program for the '3x + 1' equation, which states that any number will return to a loop of 4; 2; 1 if it follows these rules: Even numbers are divided by 2. Odd numbers are multiplied by 3 and added one to. This is yet to be proven or disproven.")
    else:
        InputNumber = int(InputNumber)
        break
OutputNumber = 0
print(InputNumber)
while not OutputNumber == 1:
    if InputNumber % 2 == 1:
        OutputNumber = InputNumber * 3 + 1
        OutputNumber = int(OutputNumber)
        print(OutputNumber)
        InputNumber = OutputNumber
    else:
        OutputNumber = InputNumber / 2
        OutputNumber = int(OutputNumber)
        print(OutputNumber)
        InputNumber = OutputNumber
print('The 4; 2; 1 loop has been initiated.')

