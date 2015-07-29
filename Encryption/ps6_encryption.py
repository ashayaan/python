import string
import random

WORDLIST_FILENAME = "words.txt"
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    return random.choice(wordList)

def randomString(wordList, n):
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------
# Encryption
def buildCoder(shift):
	s1=string.ascii_lowercase
	s2=string.ascii_uppercase
	dic={}
	for i in string.ascii_uppercase:
		dic[i]=' '
	for i in string.ascii_lowercase:
		dic[i]=' '
	for i in dic.keys():
		if i in s2:
			dic[i]=s2[(s2.index(i)+shift)%26]
		else:
			dic[i]=s1[(s1.index(i)+shift)%26]
	return dic

def applyCoder(text, coder):
	ans=""
	for char in text:
		if char in coder.keys():
			ans+=coder[char]
		else:
			ans+=char
	return ans

def applyShift(text, shift)	:
    return applyCoder(text, buildCoder(shift))


# Decryption
def findBestShift(wordList, text):
    text=text.lower()
    realword=0
    bestkey=0
    count=0
    word=" "
    for key in range(26):
        count=0
        word=applyShift(text,key)
        l=word.split()
        for i in l:
            if isWord(wordList, i):
                count+=1
        if count>realword:
            realword=count
            bestkey=key
    return bestkey
def decryptStory():
    wordList=loadWords()
    text=getStoryString()
    key=findBestShift(wordList, text)
    x=applyShift(text, key)
    print x
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    #To test decryptStory, comment the above four lines and uncomment this line:
    decryptStory()
