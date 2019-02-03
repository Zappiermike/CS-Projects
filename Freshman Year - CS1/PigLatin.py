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
    
    
    
