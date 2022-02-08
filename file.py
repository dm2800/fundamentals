num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # boolean
string = 'Hello World' # initialize string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # tuple
print(type(fruit)) # log statement 
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # log statement 
person['name'] = 'George'# list, initialize
person['eye_color'] = 'blue' # list, initialize 
print(fruit[2]) # log statement 

if num1 > 45: # if 
    print("It's greater") # log statement
else: # else 
    print("It's lower") # log statement

if len(string) < 5: # if 
    print("It's a short word!") # log statement
elif len(string) > 15: # else if 
    print("It's a long word!") # log statement 
else: # else 
    print("Just right!") # log statement 

for x in range(5): # for loop 
    print(x) # log statement 
for x in range(2,5): # for loop 
    print(x) # log statement 
for x in range(2,10,3): # for loop 
    print(x) # log statement 
x = 0 # initialize 
while(x < 5): # while loop 
    print(x) # log statement 
    x += 1 # increment 

pizza_toppings.pop() # list, add value
pizza_toppings.pop(1) # list, add value 

print(person) # log statement 
person.pop('eye_color') # dictionary, add value 
print(person) # log statement 

for topping in pizza_toppings: # for loop 
    if topping == 'Pepperoni': # if 
        continue # for loop, continue 
    print('After 1st if statement') # for loop, log statement 
    if topping == 'Olives': # if 
        break # break 

def print_hello_ten_times(): # function 
    for num in range(10): # for loop 
        print('Hello') # log statement 

print_hello_ten_times() # log statement 

def print_hello_x_times(x): # function
    for num in range(x): # for loop 
        print('Hello') # log statement 

print_hello_x_times(4) # log statement 

def print_hello_x_or_ten_times(x = 10): # function 
    for num in range(x): # for loop 
        print('Hello') # log statement 

print_hello_x_or_ten_times() # log statement 
print_hello_x_or_ten_times(4) # log statement  


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)