# 1. print all integers from 0 to 150 

for x in range(0,151):
    print(x)



# 2. multiples of 5 

for x in range (5,1001,5):
    print(x)



# 3. counting, the dojo way 

for x in range (1, 101):
    if x%5 !=0 and x%10 !=0:
        print (x)
    elif x%10 == 0: 
        print ("Dojo")
    elif x%5 == 0:
        print("Coding")



# 4. whoa. that sucker's huge

sum = 0
x = []
for i in range (0, 5000000):
	if i%2 != 0:
		x.append(i)
		sum = sum + i
print ("Final sum is", sum)



# 5. countdown by fours 
for x in range(2018, 0, -4):
	print (x)



# 6. flexible counter 
lowNum = 2 
hiNum = 9 
mult = 3 

for x in range(lowNum, (hiNum+1)):
	if x%mult == 0:
		print(x)











