#Jackson Keeley
#Michael Scheie
class Comment:
    #comment:(string,string)
    def __init__ (self,name,comment):
        self.name=name
        self.comment=comment

    #void->string
    def getCommentor(self):
        return self.name

    #void->string
    def getComment(self):
        self.comment

    #string->void
    def setCommentor(self,name):
        self.name=name

    #string->void
    def setComment(self,comment):
        self.comment=comment

    #_str_ :->string
    def __str__(self):
        return self.name + ": " + self.comment
