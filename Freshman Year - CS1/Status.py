#Jackson Keeley
#Michael Scheie
class Status:
    #Status(str,str,list-of-str,list-of-comments)
    def __init__(self,name,status,likes,comments):
        self.name=name
        self.status=status
        self.likes= likes
        self.comments= comments
    #void->string
    def getName(self):              #Changed this from Name to getName  due to viewstatus error
        return self.name
    #:string->void
    def setName(self, newName):
        self.name=newName
    #void->string
    def getStatus(self):
        return self.status          #changed from self.message to self.status to fix viewstatus error
    #string->void
    def setStatus(self,newStatus):
        self.status=newStatus
    #void->listofstrings
    def getLikes(self):
        return self.likes
    #listofstrings->void
    def setLikes(self, listoflikes):
        self.likes=listoflikes
    #listofstrings->void
    def addLike(self,name):
        self.likes.append(name)
    #void->listofcomments
    def getComments(self):
        return self.comments
    #setComments:listofstrings->void
    def setComments(self, listofcomments):
        self.comments=listofcomments
    #addcomment:Comment object->void
    def addComment(self,comment):
        self.comments.append(comment)
    def __str__(self):
        newStatus = self.name + " " + self.status + "\n"
        acc1 = ""
        acc2 = ""
        for i in range(0, len(self.likes)):
            acc1 = acc1 + str(self.likes[i]) + " liked this " + "\n"
        for i in range(0, len(self.comments)):
            acc2 = acc2 + str(self.comments[i]) + "\n"
        return newStatus + str(acc1) + str(acc2)
