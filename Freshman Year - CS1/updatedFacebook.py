#Jackson Keeley
#Michael Scheie
from Comment import*
from Status import*
from User import*

class Facebook:
    #Facebook(string,string,listofstrings,listofcomments)
    def __init__ (self):
        self.userDict={}
        self.statusList=[]
        self.User= ""
    #string->string
    def registerUser (self,name,email):
        if name in self.userDict:
            print ("That name is already in use")
        else:
            self.userDict[name]=User(name,email,[])
    #string->void
    def login(self,name):
        if self.User.strip()=="":
            self.User=name
        else:
            print("The last user must log out before you can log in")
    #string->void
    def logout(self):
        if self.User.strip()!="":
            self.User=""
        else:
            print("There is no other user currently logged in.")
    #string->void
    def addFriend (self, newFriend):
        if self.User.strip()!="":
            self.userDict[newFriend].addFriend(self.userDict[self.User])
        else:
            print("No user is currently logged in.")
    #void->string
    def viewProfile(self):
        if self.User.strip()=="":
            print("No user is currently logged in.")
        else:
            print (self.userDict[self.User])
            
    #string->string
    def postStatus(self,status):
        if self.User=="":
            print("No user is currently logged in.")
        else:
            self.statusList.append(Status(self.User,status,[],[]))
            
    #void->string
    def viewStatus(self):
        counter = 0
        if self.User.strip()=="":
            print ("There is no user currently logged in.")
        else:
            for i in range(0, len(self.statusList)):
                name = self.userDict[self.statusList[i].getName()]
                if self.userDict[self.User].isFriend(name) or name == self.userDict[self.User]:            
                    print ("(" + str(counter)+ ") " + name.getName()+ " " + str(self.statusList[i]))
                counter  = counter + 1

    #void->void
    def likeStatus(self,statusID):
        if self.User=="":
            print ("There is no user currently logged in.")
        else:
            name = self.userDict[self.statusList[statusID].getName()]
            if self.userDict[self.User].isFriend(name) or name ==  self.userDict[self.User]:
                self.statusList[statusID].addLike(self.User)
                
    #string->void
    def commentOnStatus(self,statusID,commentstring):
        if self.User.strip()=="":
             print ("There is no user currently logged in.")
        else:
            name = self.userDict[self.statusList[statusID].getName()]
            if self.userDict[self.User].isFriend(name) or name == self.userDict[self.User]:
                self.statusList[statusID].addComment(Comment(self.User, commentstring))
            else:
                ("This person either doesn't exist or is not your friend.")
