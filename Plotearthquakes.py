##Jackson Keeley
##Michael Scheie


#str -> boolean
def betweenDates(firstDate, middle, endDate):
    """Take in three dates formatted as a string and return boolean indicating whether the first date is on or after the second date and before the third date"""
    if firstDate >= middle and firstDate < endDate:
        return True
    else:
        return False
    
import urllib.request
import cTurtle


def parseEarthquakeData(date1, date2):
    page = urllib.request.urlopen("http://www.choongsoo.info/teach/mcs177-sp12/projects/earthquake/earthquakeData-02-23-2012.txt")
    list1 = []
    for aline in page:
        data = aline.decode("ascii")
        newlist = data.split(",")
        listC = [i for i in newlist if i!= ""]
        if betweenDates(listC[0], date1, date2):
            if listC[4] != "":
                magnitude = float(listC[4])
                listC[5].strip()
            depth = float(listC[5])
            longitude = float(listC[3])
            latitude = float(listC[2])
            list1.append([latitude, longitude, magnitude, depth])
    return list1
    
    
def colorCode(depth):
    if depth in range (0,34):
        return "orange"
    elif depth in range (34,71):
        return "yellow"
    elif depth in range (71,151):
        return "green"
    elif depth in range (151,302):
        return "blue"
    elif depth in range (302,500):
        return "purple"
    else:
        return "red"

def plotEarthquakeData(date1, date2):
    sally = cTurtle.Turtle()
    sally.bgpic("worldmap.gif")
    sally.setWorldCoordinates(-180, -90, 180, 90)
    data = parseEarthquakeData(date1, date2)
    sally.up()
    sally.speed(10)
    sally.hideturtle()
    for i in data:
        sally.goto((i[1]), (i[0]))
        sally.dot((i[2]*4), (colorCode(i[3])))
    sally.exitOnClick()





    
