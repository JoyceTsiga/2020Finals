<<<<<<< HEAD
print("Welcome to  your password manager")



import random
password=""
capLttr=input("How many capital letters do you want? ")
regLttr=input("How many regular letters do you want? ")
number=int(input("How many numbers do you wants? "))
symbols=("How many symbols do you want? ")
specialCharacters=[33,35,36,37,38,40,41,64,94]

if (capLttr > "0"):
    for i in range(capLttr):
        print (str(random.randint(65,90)))

if (regLttr > "0"):
  for i in range(regLttr):
    print (str(random.randint(65,122)))

if (number > "0"):
  for i in range(number):
    print (random.randint(48,57))

if (symbols > "0"):
  for i in range(symbols):
    print (str(random.randint(specialCharacters)))

#            [length,lower,upper,numbers,specials]
reqCheckList=[False,False,False,False,False]
#       abandon this idea because the for loop would reset the values everytime
passwordStrengthList=[False,False,False,False,False] #sets the strength level to start as 0
again=True
while(again!="stop"): #if user inputs stop, the loop with cancel
    passwordToCheck=input("input a password ")
    passwordToCheckLIST=[]
    #.append() adds items to the list
    for i in range(len(passwordToCheck)): 
        passwordToCheckLIST.append(False)
    #print(passwordToCheckLIST)
    if(len(passwordToCheck)>=6 and len(passwordToCheck)<=16):
        reqCheckList[0]=True
        passwordStrengthList[0]=True    #if true, adds a strength level
        #iterating through passwordToCheck
        for i in range(len(passwordToCheck)):
            #print(passwordToCheck[i])
            #a-z on ASCII is.... range(97-123) remember range(start, sop, AND not include)
            if(ord(passwordToCheck[i]) in range(97,123)):
                passwordToCheckLIST[i]=True
                reqCheckList[1]=True
                passwordStrengthList[1]=True
            #A-Z on ASCII is.... range(65-91)
            elif(ord(passwordToCheck[i]) in range(65,91)):
                passwordToCheckLIST[i]=True
                reqCheckList[2]=True
                passwordStrengthList[2]=True
            #0-9 on ASCII is.... range(48-58)
            elif(ord(passwordToCheck[i]) in range(48,58)):
                passwordToCheckLIST[i]=True
                reqCheckList[3]=True
                passwordStrengthList[3]=True
            elif (ord(passwordToCheck[i]) in specialCharacters):
                passwordToCheckLIST[i]=True
                reqCheckList[4]=True
                passwordStrengthList[4]=True
    print(passwordToCheckLIST)

    if(False in passwordToCheckLIST or False in reqCheckList):
        print("Password did not met the requirements")
        print('{} out of 5'.format(reqCheckList.count(True))) #prints out the number of points out of 5
    else:
        print("Password met the requirements")
        print('{} out of 5'.format(reqCheckList.count(True)))

    passwordStrength=["#"*passwordStrengthList.count(True) + "-"*passwordStrengthList.count(False)] #puts the strong strength level next to the weak level
    print(passwordStrength)     #prints the strength level

    again=input("Another password? (stop to cancel) ") #askes he user if they want to type i another password
=======
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
    return(f'Here is your new generated password:\n{PWGenerator().createPW()}')

def pwChecker():
    passwordToCheck=input("input a password ")



print("Welcome to your Password Manager")
print("if You are a new user enter 1, if you already have an account enter 2")
userInfo = input("")
logIn = input("Would you like to login? (y or n) ")
if logIn == "y":
    first = input("What is ur First name? ")
    last = input("What is ur last name ? ")
    username = input("What is ur username ")
    password = input("What is ur password ")

while logIn!="y":
    ("Would u like to login? (y/n) ")

print(f'''
    Your first name is {first}
    Your Last name is  {last}
    Your UserName is   {username}
    Your Password is   {password}




''')
#IS this info correct 
>>>>>>> 81b19bf03bfce794900c56c5183f79d95b84f8e7
