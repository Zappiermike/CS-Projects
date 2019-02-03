#0Jackson Keeley
#Michael Scheie

from cImage import *
Picture = FileImage("landscape.gif")

def sepiaTone(oldPixel):
    R = oldPixel.getRed()
    G = oldPixel.getGreen()
    B = oldPixel.getBlue()
    newR = min(255, int(R*.393 + G*.769 + B*.189))
    newG = min(255, int(R*.349 + G*.686 + B*.168))
    newB = min(255, int(R*.272 + G*.534 + B*.131))
    newPixel = Pixel(newR, newG, newB)
    return (newPixel)
    
def convertToGamma(oldPixel, gammaValue):
    R = oldPixel.getRed()
    G = oldPixel.getGreen()
    B = oldPixel.getBlue()
    Y = (0.00117 * R + 0.00230 * G + 0.000447 * B) ** gammaValue 
    U = -0.000577 * R - 0.00113 * G + 0.00171 * B
    V = 0.00241 * R - 0.00202 * G - 0.00039 * B
    newPixel = Pixel(Y, U, V)
    newR = 255 * (Y + 1.13983 * V)
    newG = 255 * (Y - 0.39465 * U - 0.58060 * V)
    newB = 255 * (Y + 2.03211 * U)
    if newR <= 0:
        newR = 0
    if newG <= 0:
        newG = 0
    if newB <= 0:
        newB = 0
    finalR = min(255, newR)
    finalG = min(255, newG)
    finalB = min(255, newB)
    return Pixel(finalR, finalG, finalB)


#Pixel->Pixel
def gammaTwo(Pixel):
    newImage = convertToGamma(Pixel, 2.0)
    return newImage

#Pixel->Pixel
def gammaHalf(Pixel):
    newImage = convertToGamma(Pixel, 0.5)
    return newImage

#Image, Function->Pixel
def transformPixels(Image, Function):
    ei = EmptyImage(Image.getWidth(), Image.getHeight())
    for i in range(0, Image.getWidth()):
        for j in range(0, Image.getHeight()):
            originalPicture = Image.getPixel(i,j)
            newPixel = Function(originalPicture)
            ei.setPixel(i,j,newPixel)
    return ei


#Image->Image
def rotateImage90(Image):
    ei = EmptyImage(Image.getWidth(), Image.getHeight())
    
    for i in range(0, Image.getWidth()):
        for j in range(0, Image.getHeight()):
            originalPixel = Picture.getPixel(i,j)
            ColumstoRow = ei.setPixel(Image.getHeight() - j,i,originalPixel)
    return ei


def drawImages(Title, listofImages):
    totalWidth = 0
    maxHeight = 0
    for i in listofImages:
        totalWidth = totalWidth + i.getWidth() + 1
        if i.getHeight() > maxHeight:
            maxHeight = i.getHeight()
    myWindow = ImageWin(Title, totalWidth, maxHeight)
    Pictures = 0
    for i in listofImages:
        i.setPosition(Pictures,0)
        i.draw(myWindow)
        Pictures = Pictures + i.getWidth() + 1
    myWindow.exitOnClick()

drawImages("Princess Bride", [Picture, transformPixels(rotateImage90(Picture), sepiaTone)])

