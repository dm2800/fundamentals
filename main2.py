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
    }
]

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

for movie in movies: 
    if movie['title'] == "Back to the Future":
        print("Yay you found my favorite Movie")
    elif movie ['title'] == "Rambo 1st Blood":
        print("this one is ok")
    else:
        print ("sorry ran out of movies")

