movies = [
    {
        'id': 1, 
        'title': "Back to the Future",
        'year': 1984, 
        'actors': [
            {'name': 'Michael J Fox '},
            {'name': 'Christopher Lloyd'}
        ],
        'genre': 'Sci-Fi'
    },
    {
        'id': 2, 
        'title': 'Rambo 1st Blood',
        'year': 1982,
        'actors': [
            {'name': 'Sylvester Stallone'},
            {'name': 'David Caruso'},
            {'name': 'Brian Denning'}
        ],
        'genre': 'Action'
    },
    {
        'id': 3,
        'title': 'Teen Wolf',
        'year': 1985,
        'actors': [
            {'name': 'Sylvester Stallone'},
            {'name': 'David Caruso'},
            {'name': 'Brian Denning'}
        ],
        'genre': "Sci-Fi Drama"
    }
]


# Use a for loop when you expect there to be more than 1 result 


#Check to see if a movie in the list has christopher lloyd as an actor listed 

"""""
    Step 1: loop thru all the movies 
    Step 2: Check each movie to see if it has Chrisopher Lloyd listed as one of its actors 
    Step 3: If yes add movie to a list 
    Step 4: Print back the list of movies 

"""

# def checkActors(l, n): #pass in the list of movies and the name we want to check against. 
#     myList = [] # creating an empty list to stor the True results 
#     for m in l: #Looping thru the entire list of movies => Should always the bigger list that containst the smaller list 
#         for a in 




#Create a funciton that prints back the whole list of movies 
def printList(x): # Function taking 1 parameter
    print("Whole list: ", x) # print statement to print back what is being passed in 



#printList(movies) # Activating the function and passing in the desired list or data set 

    # The functions will be called through the front end or a form typically on the webpage 


# Print back just the titles of all the movies contained in the list 
def printTitles(x):
    for i in x: # because we know we might get more than 1 result, we use a for loop 
            print("All the movie titles: ", i['title']) # Here because we will use the calling of the function to narrow down what dictionary to look in we can say just print back the list of actors 




#Print the list of actors in 1 Movie 
def movieActors(x):
    print("the selected movies actor list: ", x['actors'])


movieActors(movies[0]) # Here we are calling just 1 instance from our data set 
movieActors(movies[1])
movieActors(movies[2])

# Check to see if a given movie instance has a specific actor in it 
def checkActor(x,y):
    for i in x: # going to loop thru the list of actors in the chosen movie
        if i['firstName'] == y:# checks each actor's first name against the chosen name and runs these instructions if true 
            print(y, "is in this movie") #if true will print the actors name 
            return # because we don't need to keep checking the list of actors this will stop the loop 
        else: # this will only run if the above is false 
            print('Sorry', y, "isn't in this movie") # this will print for each actor that is in the loop where the if failed to stop the function. 

checkActor(movies[0]['actors'], "Michael J") # activating function by passing in 1 movie and just its list of actors and also a name for an actor to check 

# print(movies)



# # print back to the future only 
# print("just back to the future: ", movies[0])

# greatMovie = movies[0]['actors']


# aList = []
# print("before function: ", aList)
# def actorList(var): 
#         for a in var:
#             aList.append(a['name'])
#         print("the list of actors inside function: ", aList)


# actorList(greatMovie)
# print("after function", aList)

# for movie in movies: 
#     if movie['title'] == "Back to the Future":
#         print("Yay you found my favorite Movie")
#     elif movie ['title'] == "Rambo 1st Blood":
#         print("this one is ok")
#     else:
#         print ("sorry ran out of movies")

