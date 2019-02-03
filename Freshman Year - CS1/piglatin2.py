#str->str
def unPigWord(word):
    """This function converts strings from Pig Latin to English"""
    hyphen = word.find("-")
    first = word[:hyphen]
    second = word[hyphen+1:-2]
    return(second+first)
    
#str->str  
def findVowel(word):
    """This fucntion finds the first vowel in the word given, if none exist it will return the total number of letters"""
    vowel = "aeiou"
    word.lower()
    for i in word:
        if i in vowel:
            return word.index(i)
    return len(word)
    
#str->str
def pigWord(English):
    "This fucntion takes the given English word and translates it into Pig Latin"""
    transition = findVowel(English)
    firstpart = English[transition:]
    second = English[0:transition]
    return (firstpart+"-"+second+"ay")
    
    
#str->str    
def unPig(string):
    """This function takes in the given Pig Latin sentence/string and converts it to English"""
    var = string.split(" ")
    newlist = []
    for i in var:
        total = unPigWord(i)
        newlist.append(total)
    return " ".join(newlist)

#str->str
def pig(english):
    """This function takes in the given English sentence/string and converts it to Pig Latin"""
    var = english.split(" ")
    newlist = []
    for i in var:
        total = pigWord(i)
        newlist.append(total)
    return " ".join(newlist)

#EXTRA CREDIT

def join(string):
    list1 = string.split(" ")
    fullsen=""
    for i in list1:
        fullsen = fullsen + i + " "
    return fullsen[:len(fullsen)-1]


#>>>join(['this', 'is', 'Pig', 'Latin'])
#'this is Pig Latin'

