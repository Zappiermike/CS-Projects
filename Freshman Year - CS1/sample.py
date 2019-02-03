#Jackson Keeley
#Michael Scheie

from song import *
from Playlist import *

a= Song("Lady Gaga", "The Fame", "Just Dance", "file", "pop")
b= Song("Lady Gaga", "Born This Way", "Americano", "file", "pop")
c= Song("Lady Gaga", "The Fame", "Paparazzi", "file", "pop")
d= Song("Drake", "Hotline Bling", "Hotline Bling", "file", "R&B")
e= Song("Adele", "25", "Hello", "file", "Soul Music")
f= Song("Wiz Khalifa", "Furious 7", "See You Again", "file", "Hip-Hop")


sample = Playlist("Lady Gaga Mix",[a,b,c],False)
sample2 = Playlist("Lady Gaga Mix",[c,d,e,f],True)
