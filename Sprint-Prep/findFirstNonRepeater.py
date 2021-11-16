
#Fastest most efficient performer
def firstNoneRepeater2(string):
    charCountDict = dict()
    
    for eachChar in string:
        if eachChar in charCountDict.keys():
            charCountDict[eachChar] += 1
        else:
            charCountDict[eachChar] = 1
            
    for eachChar in string:
        if charCountDict[eachChar] == 1:
            return eachChar
        
    return ""

# second fastest of the three alternatives        
def firstNoneRepeater1(string): # O(n)best O(n^2)worst
    checkedSet = set()
    for eachChar in string:
        if eachChar not in checkedSet:
            if string.count(eachChar) == 1: # this causes the first one to be faster
                return eachChar

            checkedSet.add(eachChar)
    return ""

# slowest performer
def firstNoneRepeater3(string):
    for eachChar in string:
        if string.count(eachChar) == 1: #O(n^2)
            return eachChar

