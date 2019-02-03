#Jackson Keeley
#Michael Scheie
class User:
    #user(str,str,listofusers)
    def __init__(self,name,email,listoffriends):
        self.name=name
        self.email=email
        self.listoffriends= [] ##listoffriends

    #void->string
    def getName (self):
        return self.name

    #string->void
    def setName(self,newName):
        self.name=newName

    #void->string
    def getEmail (self):
        return self.email

    #string->void
    def setEmail (self, newEmail):
        self.email=newEmail

    #void->listofobjects
    def getFriendList(self):
        return self.listoffriends

    #listofobjects->void
    def setFriendList(self, listoffriends):
        self.listoffriends = listoffriends

    #object->void
    def addFriend(self, newFriend):
        self.listoffriends.append(newFriend)
        newFriend.listoffriends.append(self)

    #object->boolean
    def isFriend (self, friend):
        return (friend in self.listoffriends)

    #__str__ :void->string
    def __str__(self):
        start= self.name + " ("+ self.email +")\nFriends: "
        acc = ""
        for i in range (0, len(self.listoffriends)):
            if len(self.listoffriends)== 0:
                return start + "None"
            else:
                acc = acc + (self.listoffriends[i].getName() + " and ")
        return start + acc[0:len(acc)-4]


