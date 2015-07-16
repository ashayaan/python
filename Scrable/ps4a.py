# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------


def getWordScore(word, n):
    score=0
    score2=0
    length=len(word)
    if length==n:
        score+=50
    for i in range(length):
        score2+=SCRABBLE_LETTER_VALUES[word[i]]
    score2=score2*length
    score+=score2
    return score



def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              
    print                               


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
	y={}
	x=hand.copy()
	for i in word:
		y[i]=y.get(i,0)+1
	for letter in x.keys():
		if letter in word:
			x[letter]-=y[letter]
	return x



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    if word not in wordList:
        return False
    sup = 0
    handCopy = hand.copy ()
    for char in word:
        if char in handCopy:
            if handCopy [char] != 0:
                handCopy [char] -= 1
                sup += 1
    if sup == len(word):
        return True
    else:
        return False


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    length=0
    for i in hand.keys():
        length+=hand[i]
    return length




def playHand(hand, wordList, n):
    score=0
    total=0
    word=''
    while calculateHandlen(hand)>0:
        displayHand(hand)
        word=raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word==".":
            print "  Goodbye! Total score: "+str(total)+" points"
            break
        if isValidWord(word, hand, wordList):
            score=getWordScore(word, n)
            total+=score
            print str(word)+" earned "+str(score)+" points. "+"Total: "+str(total)
            hand= updateHand(hand, word)
        else:
            print "Invalid word, please try again."
            continue
    if (calculateHandlen(hand)==0):
        print "Run out of letters. Total score: "+str(total)+" points "

def playGame(wordList):
    n=HAND_SIZE
    choice=''
    hand={}
    temp={}
    count=0
    while choice != 'e':
        choice=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice=='n':
            hand=dealHand(n)
            temp=hand.copy()
            count+=1
            playHand(hand, wordList,n)
        elif choice=='r':
            if count==0:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                playHand(temp, wordList,n)
        elif choice=='e':
            break
        else:
            print "Invalid choice"
            continue
    print
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
