import os

def badFunctionName(varOne,varTwo,varThree): # bad naming and no spaces
    if varOne>varTwo: # no spaces around >
        print(varOne,"is greater than",varTwo) # no spaces after commas
    else:
        print(varTwo,"is greater or equal to",varOne)

    for i in range(0,varThree): # magic number and no spaces
        print("Number:",i) # no spaces after colon
    # Unnecessary semicolon; using == for assignment in if statement; mixing single and double quotes
    list_example = [1, 2, 3, 4] 
    if (list_example[0] == 1): 
        list_example[0] = 'one' 
    elif list_example[0]=='1':
        list_example[0] = "one" 
    return varThree+varOne-varTwo # no spaces around operators and inconsistent use of operators for no reason