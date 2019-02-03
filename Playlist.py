#Michael Scheie
#Jackson Keeley

import random
from song import *

class Playlist:
    #Playlist (str, list of Songs, boolean)
    def __init__(self, Name, Songs, Random):
        self.Name = Name
        self.Songs = Songs[:]
        self.Songs2 = Songs[:]
        self.Random = Random
    #getName (void -> str)
    def getName(self):
        return self.Name
    #getSongs (void -> ListofSongs)
    def getSongs(self):
        return self.Songs
    #getRandom (void -> Boolean)
    def getRandom(self):
        return self.Random
    #setName (str -> void)
    def setName(self, Name):
        if name.strip() == "":
            print ("Error, Please provide a name")
        else:
            self.Name = Name
    #setSongs (ListofSongs -> str or void)
    def setSongs(self,Songs):
        self.Songs = Songs[:]
    #setRandom (Boolean -> void)
    def setRandom(self,Random):
        self.Random = Random
    #addSongs (Songs->void)
    def addSong(self, newSong):
        self.Song.append(newSong)
    #void -> str
    def __str__(self):
        playlist = ""
        for i in self.Songs:
            playlist = playlist + str(i) + "\n"
        return ("Playlist: "+ self.Name + "\n" + playlist)

    def nextsong(self):
        if self.Random == False:
            newSong = self.Songs.pop(0)
            self.Songs.append(newSong)
            return newSong
        else:
            random.shuffle(self.Songs2)
            aSong = self.Songs2.pop(0)
            if len(self.Songs2) == 0:
                self.Songs2 = self.Songs
            return aSong

