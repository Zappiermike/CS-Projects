def makeDictionary(keys, values):
    d1 = {}
    for i in range(len(keys)):
        d1[keys[i]] = values[i]
    return d1

        
myIMDb = {}


#str->void
def addMovie(title, characters, actors):
    """This function takes in the movie name including the characters and actors as well. It adds everything to our global list of IMDb"""
    dictofpeople = makeDictionary(characters, actors)
    myIMDb[title] = dictofpeople
   

#void->list of string
def listMovies():
    """This function looks at myIMDb and returns all the titles contained inside that dictionary"""
    newlist = list(myIMDb.keys())
    return newlist

#str->str
def findActor(movie, character):
    """This fucntion takes in the the movie and character's name and finds/prints who the actor is for that character"""
    if movie not in myIMDb:
        print('No such movie found')
    elif character not in (myIMDb[movie]):
        print ('No such character found')
    else:
        actorName = (myIMDb[movie])[character]
        print (actorName)
        
#str->str
def showCast(movie):
    """This function takes in the movie name and returns a table that shows the whole cast of the movie, including their character's name"""
    if movie not in myIMDb:
        print ('No such movie found')
    else:
        print('Character', 'Actor/Actress'.rjust(23))
        print('-'*37)
        keys = list(myIMDb[movie].keys())
        keys.sort()
        for i in keys:
            print (i.ljust(19), myIMDb[movie][i])

        
            



addMovie('The Martian',['Mark Watney'],['Matt Damon'])
addMovie('The Sixth Sense',['Cole Sear', 'Dr. Malcolm Crowe', 'Lynn Sear', 'Vincent Grey'],['Haley Joel Osment', 'Brue Willis', 'Toni Collette', 'Donnie Wahlberg'])
addMovie('American Sniper',['Chris Kyle', 'Taya', 'Marc Lee'],['Bradley Cooper', 'Sienna Miller', 'Luke Grimes'])
addMovie("Harry Potter and the Sorcerer's Stone", ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Albus Dumbledore'],['Daniel Radcliffe', 'Emma Watson', 'Rupert Grint', 'Richard Harris'])

