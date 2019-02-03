def timeToMow(depth, length):
    area=abs(depth*length)
    totalTime=((area/2)/3600)
    return(totalTime)



def roundedTimeToMow(depth):
    length=depth*(9/16)
    timeToMow(depth, length)
    return round(timeToMow(depth, length))



        




    




