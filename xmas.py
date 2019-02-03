def presentsOnDay(whatDay):
    n=whatDay
    acc=0
    for i in range(n+1):
        acc = acc + (i)
    return int(acc)

def presentsOnDayv2(day):
    return day*(day+1)//2

def presentsThroughDay(UptoDay):
    totalpresents=0
    for i in range(UptoDay+1):
        totalpresents = totalpresents + presentsOnDay(i)
    return totalpresents




#Day 3 should have 6 total
#Day 2 should have 3 total
#Day 1 should have 1 total
            
