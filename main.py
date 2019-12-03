from nltk.corpus import words

def addCharToDict(letter, dictSet):
    """
    Adds a character to a given dictionary

    Parameters:
    list (char): A letter in a string
    dictSet (dict)
    """

    if letter not in dictSet:
        dictSet[letter] = 1
    else:
        dictSet[letter] += 1


def getCharsInWord(word):
    """
    Turns a string into a dictionary with the key as a character the the value as the number of instances of the character

    Parameter:
    word (string)

    Returns:
    dictionary
    """

    dictSet = {}

    for letter in word:
        addCharToDict(letter, dictSet)

    return dictSet    
    

def getBestWords(wordSet, charSet, startLetter, endLetter):
    """
    Finds the words that can be used based on user contraints

    Parameters:
    wordSet (list): List of words in a dictionary
    charSet (dict): Dictionary of a user's characters
    startLetter (char): User's start letter. Default: ""
    endLetter (char): User's ending letter. Defualt: ""

    Returns:
    usableWords (dict): Dictionary of words. Key: length of word, Value: word
    """

    usableWords = {}

    for word in wordSet:
        copyCharSet = charSet.copy()
        skipWord = False

        if startLetter != "" and word[0] == startLetter:
            addCharToDict(startLetter, copyCharSet)
        elif startLetter != "":
            skipWord = True

        if endLetter != "" and word[len(word)] == endLetter:
            addCharToDict(endLetter, copyCharSet)
        elif endLetter != "":
            skipWord = True  

        if len(word) <= len(copyCharSet) and skipWord == False:
            dictSet = getCharsInWord(word)

            flag = 1

            for char in word:
                if char not in copyCharSet:
                    flag = 0
                    break
                else:
                    if dictSet[char] > 0 and copyCharSet[char] > 0:
                        dictSet[char] -= 1
                        copyCharSet[char] -= 1
                    else:
                        flag = 0
                        break    
            if flag == 1 and len(word) > 1:
                if len(word) not in usableWords:
                    usableWords[len(word)] = [word]
                else:
                    usableWords[len(word)].insert(0, word)    
    return usableWords        

def main():
    dictionary = words.words()
    userCharSet = {}

    userCharInput = input("What is your set of letters?: ")
    userCharSet = getCharsInWord(userCharInput)

    userStartLetter = input("Does your word start with a letter, if so, which? If none hit enter: ")

    userEndLetter = input("Does your word end with a letter, if so, which? If none hit enter: ")

    result = getBestWords(dictionary, userCharSet, userStartLetter, userEndLetter)

    charExtension = 0

    if userStartLetter != "" and userEndLetter != "":
        charExtension += 2
    elif userStartLetter != "" or userEndLetter != "":
        charExtension += 1    

    for i in range(2, len(userCharSet) + 1 + charExtension):
        if i in result:
            print(str(i) + " letters words:")
            for word in result[i]:
                print(word, end=" ")
            print("")
        else:
            print("There are no words available with " + str(i) + " letters.")      
main()
