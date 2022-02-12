# 1. countdown 

list = []

def countdown(n): 
    for x in range (n,-1,-1):
        list.append(x)
    print(list)

countdown(5)



# 2. print and return 

def print_and_return(list):
    print(list[0])
    return (list[1])

print_and_return([1,2])
print(print_and_return([1,2]))



# 3 

def first_plus_length(list):
    return (list[0] + len(list))

first_plus_length([1,2,3,4,5])

print(first_plus_length([1,2,3,4,5]))

#4 

def values_greater_than_second(list):
    list2 = []
    for i in range(0, len(list)):
        if len(list) < 2:
            print("False")
        elif (list[i]>list[1]):
            list2.append(list[i]) 
   
    print (len(list2))
    return (list2)

values_greater_than_second([5,2,3,2,1,4])
print (values_greater_than_second([5,2,3,2,1,4]))
values_greater_than_second([3])



#5 
def length_and_value(size, value):
    list = []
    for i in range(0,size):
        list.append(value)
    print(list)

length_and_value(4,7)
length_and_value(6,2)


