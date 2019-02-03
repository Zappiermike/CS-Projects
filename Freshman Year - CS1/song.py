#Michael Scheie
#Jackson Keeley

class Song:
    #Song (str,str,str,str,str)
    def __init__(self, Artist, AlbumTitle, SongTitle, MP3, Genre):
        self.Artist = Artist
        self.AlbumTitle = AlbumTitle
        self.SongTitle = SongTitle
        self.FileName = MP3
        self.Genre = Genre
    #getArtist: void->str
    def getArtist(self):
        return self.Artist
    #getAlbumTitle: void -> str
    def getAlbumTitle(self):
        return self.AlbumTitle
    #getsongTitle: void->str
    def getsongTitle(self):
        return self.SongTitle
    #getFileName: void->str
    def getfileName(self):
        return self.FileName
    #getGenre: void->str
    def getgenre(self):
        return self.Genre
    #setArtist: str->void
    def setArtist(self, Artist):
        if Artist.strip() == "":
            print ("Error: Please provide an Artist")
        else:
            self.Artist = Artist
    #setAlbumTitle: str->void
    def setAlbumtitle(self, AlbumTitle):
        if AlbumTitle.strip() == "":
            print ("Error: Plase provide an Album title")
        else:
            self.AlbumTitle = AlbumTitle
    #setSongtitle: str->void
    def setSongtitle(self, SongTitle):
        if SongTitle.strip() == "":
           print ("Error: Please provide a Song Title")
        else:
            self.SongTitle == SongTitle
    #setMP3: str->void
    def setMP3(self, MP3):
        if MP3.strip() == "":
            print ("Error: Please provide a file name")
        else:
            self.FileName = MP3
    #setGenre: str->void
    def setGenre(self, Genre):
        if Genre.strip() == "":
            print("Error: Please provide a Genre")
        else:
            self.Genre = Genre
    #void -> str
    def __str__(self):
        return (self.SongTitle + " in " + self.AlbumTitle + " by " + self.Artist)




                
        
