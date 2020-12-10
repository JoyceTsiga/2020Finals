total=0                         #accumulative variable
krabbyPattySelected=False         #flag variable
beverageSelected=False
friesSelected=False
mealSelected=False
order=[]

#the menu (hint:make sure to type food as in menu)
kKM=print("\n")
print("\tKrabby Patty...........1.25            Krabby Meal........3.50")
print("\t   w/sea cheese........1.50            Double Krabby M....3.75")
print("\tDouble Krabby Patty....2.00            Triple Krabby Me...4.00")
print("\t   w/sea cheese........2.25            Salty Sea Dog......1.25")
print("\tTripple Krabby Patty...3.00            FootLong...........2.00")
print("\t   w/sea cheese........3.25            Sailors Surprise...3.00")
print("\t                                       Golden Loaf........2.00")
print("\t                                           w/sauce........2.50")
print("\tCoral Bits")
print("\tSmall..................1.00            Kelp Shake.........2.00")
print("\tMedium.................1.25               Seaform Soda")
print("\tLarge..................1.50                    Small......1.00")
print("\t                                               Medium.....1.25")
print("\t                                               Large......1.50")
print("\tKelp Rings.............1.50")
print("\t   Salty Sauce......... .50")


#krabby meals
krabbyMeal=input("Would you like a krabby meal? ")
if (krabbyMeal=="yes"): #if the user says y, then will give you a list of the meals
    mealSelected=True #ask user what meal they want if ui = yes
    krabbyMeal=input("Would you like a Krabby Meal for 3.50, a Double Krabby Meal for 3.75, a Triple Krabby Meal for 4.00,a Salty Sea Dog for 1.25, a FootLong for 2.00, a Sailors Surprise for 3.00, or a Golden loaf for 2.50?  ")
elif (krabbyMeal=="no"): #is n, then a meal is not added to your list
    mealSelected=False

#if the user selected on of the meal options, then its total will be added
if krabbyMeal=="Krabby Meal":
    total+=3.50
elif krabbyMeal=="Double Krabby Meal":
    total+=2.75
elif krabbyMeal=="Triple Krabby Meal":
    total+=4.00
elif krabbyMeal=="Salty Sea Dog":
    total+=1.25
elif krabbyMeal=="Footlong":
    total+=2.00
elif krabbyMeal=="Sailars Surprise":
    total+=3.00
elif krabbyMeal=="Golden Loaf":
    total+=2.00
order.append(krabbyMeal)#adds meal to receit

krabbyPatty=input("Would you like a krabby patty? ")
if krabbyPatty=="yes":
    krabbyPatty = input("What kind of Krabby Patty would you like? ")
#print(krabbyPatty)

if krabbyPatty=="Krabby Patty":
    krabbyPattySelected = True #if the user wants sea cheese on their patty then, the total would add .25 to the patty cost(this is with all the patty options)
    krabbyPatty2=input("Would you like sea cheese with that? ")
    if krabbyPatty=="yes":
        total += 1.50 #added .25 to the patty cost
    else:
         total += 1.25 #original patty cost
elif krabbyPatty=="Double Krabby Patty":
    krabbyPattySelected = True
    krabbyPatty2=input("Would you like sea cheese with that? ")
    if krabbyPatty=="yes":
        total += 2.25
    else:
         total += 2.00 
elif krabbyPatty=="Triple Krabby Patty":
    krabbyPattySelected = True
    krabbyPatty2=input("Would you like sea cheese with that? ")
    if krabbyPatty=="yes":
        total += 3.25
    else:
         total += 3.00
order.append(krabbyPatty)#adds patty to receit


beverage = input("Would you like a drink, yes or no? ")
if(beverage=="yes"):
    beverageSelected = True
    beverage=input("Would you like a kelp shake or a seafoam soda? ")
if(beverage=="seafoam soda"):
    beverage2=input("s for $1.00, m for $1.25, and l for $1.50 ")
elif beverage == "kelp shake":
    beverage2=False #seafoam soda is not picked
    total+=2.00

if beverage2=="s":
    total += 1.00
elif beverage2=="m":
    total += 1.25
elif beverage2=="l":
    total += 1.50
order.append(beverage)#adds drink to receit

#iteration 3 asking for fries
kelpFries = input("Would you like some fries, yes or no? ")
if(kelpFries=="yes"): 
    friesSelected = True
fries=input("Coral Bits or Kelp Rings? ")
if fries=="Coral Bits":
    coralBits=input("s for $1.00, m for $1.25, or l for $1.50? ")
elif fries=="Kelp Rings": #if kelp rings, then 2.00 is added, and no size picking is needed
    total += 1.50
        
#if coral bits is selected, then the user will pick the size of the fries    
if (coralBits == "s"):
    total = total + 1.00
elif (coralBits == "m"):
  total = total + 1.25
elif (coralBits == "l"):         #nested conditional statement
        total +=1.50
order.append(coralBits)


#iteration 4
#if you do not convert input() it will be a sequence or a string
saltySauce=int(input("How many salty sauces would you like? "))*.50
total+=saltySauce
order.append(saltySauce)
#but you could combine the top two lines into one


if(krabbyPattySelected and beverageSelected and friesSelected):      #and looks for 2 trues statements
#if variable==true And variable==true And variable==true
    total-=1

#print("Your total is",total)

#print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of '.format(sandwhich,beverage,fries,ketchup))

tax=0.07 #tax of your order
subTotal=total/(1+tax) #subtotal amount
taxAmount = subTotal*(1+tax/100) #the tax amount 

finalAmount = subTotal+taxAmount #the final amount

order=[]

#the receit
print(f'''
Your order is:
{krabbyMeal}, 
{krabbyPatty},
{beverage},
{fries},
{saltySauce} saltysauces
tax is {taxAmount}
Subtotal is {subTotal}
For a total of ${finalAmount}
'''.format(krabbyPatty,beverage,fries,saltySauce,total))

addOrdelete=False
addOrdelete=input("Would you like to add or delete anything on the order? Yes or No ") #ask the user if they want to delete or add to the receit
if addOrdelete=="No":
    addOrdelete=False
elif addOrdelete=="yes":
    addOrdelete=True
    addOrdelete=input("Add or Delete? ")
if addOrdelete==("add"):
    add=input("What would you like to add? ")
    while add!="q":
        order.append()
elif addOrdelete==("delete"):
    delete=input("What would you like to delete? ")
    while delete!="q":
        order.remove()

#print('${:,.2f}'.format(total)) #string formatting