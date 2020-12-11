import random
from GenClass import PWGenerator
passwordList = []
logInPW = []

def choice():
    ui = input("do you want to create a Password (y or n) ")
    if ui == "y":
        userPassword = input("Put your new Password: ")
        passwordList.append(userPassword)
    elif ui == "n":
        PWGenerator()

def logIn():
    username = input("What is ur username ")
    password = input("What is ur password ")

    if password in logInPW:
        choice()

def signUp():
    first = input("What is ur First name? ")
    last = input("What is ur last name ? ")
    username = input("What is ur username ")
    password = input("What is ur password ")

    print(f'''
    Your first name is {first}
    Your Last name is  {last}
    Your UserName is   {username}
    Your Password is   {password}
    ''')
    logInPW.append(password)

# def category():


# def updateData():


def PWGenerator():
    return PWGenerator(f'Here is your new generated password:\n{PWGenerator().createPW()}')

def pwChecker(password):
    passwordToCheck=password
    specialCharacters=[33,35,36,37,38,40,41,64,94]
    points = 0
    artPoints = ""
    lossPoints = ""
    #            [length,lower,upper,numbers,specials]
    reqList=[False, False,False,False,  False   ]
    #       abandon this idea because the for loop would reset the values everytime

    passCheckList=[]
    #.append() adds items to the list
    for i in range(len(passwordToCheck)):
        passCheckList.append(False)
    # print(passCheckList)

    if(len(passwordToCheck)>=6 and len(passwordToCheck)<=16):
        reqList[0]=True

        #iterating through passwordToCheck
    for i in range(len(passwordToCheck)):
        #print(passwordToCheck[i])   
        #a-z on ASCII is ....   range(97,123) remember range(start,stopANDnotInclude)
        #if the password has a lower letter then add a point
        if(ord(passwordToCheck[i]) in range(97,123)):
            passCheckList[i]=True
            reqList[1]=True


        #A-Z on ASCII is ....   range(65,91)    
        #if the password has a Capital letter then add a point 
        if(ord(passwordToCheck[i]) in range(65,91)):
            passCheckList[i]=True
            reqList[2]=True


        #0-9 on ASCII is ....   range(48,58)    
        #if the password has a number then add a point
        if(ord(passwordToCheck[i]) in range(48,58)):
            passCheckList[i]=True
            reqList[3]=True
        #if the password has a special character then add a point
        if(ord(passwordToCheck[i]) in specialCharacters):
            passCheckList[i]=True
            reqList[4]=True

    for i in reqList:
        if i == True:
            points += 1
            artPoints += "#"
        else:
            lossPoints += "-"
        score = [artPoints+lossPoints]
    strengthList.append(score)

    print(points, "Out of 5 points =", artPoints + lossPoints)
    if(False in passCheckList or False in reqList):         #this calculates how many points the password would get
        return "Your password did not meet the requirements"
    else:
        return "Your password met the requirements"



print("Welcome to your Password Manager")
ui = input("Do you need to make an account (y or n) ")
if ui == "y":
    signUp()
elif ui == "n":
    logIn()