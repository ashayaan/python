from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    maxscore=0
    score=0
    bestWord=None
    for word in wordList:
        if isValidWord(word, hand, wordList):
           score=getWordScore(word, len(word))
           if score>maxscore:
               maxscore=score
               bestWord=word
    return bestWord
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    score=0
    total=0
    word=''
    while word != None:
        displayHand(hand)
        word=compChooseWord(hand, wordList, n)
        if isValidWord(word, hand, wordList):
            score=getWordScore(word, n)
            total+=score
            print '"'+str(word)+'"'+" earned "+str(score)+" points. "+"Total: "+str(total)
            hand= updateHand(hand, word)
    print "Total score: "+str(total)
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    n=HAND_SIZE
    choice=''
    hand={}
    temp={}
    count=0
    user=''
    while choice != 'e':
        choice=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice=='n':
            while user != None:
                user=raw_input("Enter u to have yourself play, c to have the computer play:") 
                if user == 'u':
                    hand=dealHand(n)
                    temp=hand.copy()
                    count+=1
                    playHand(hand, wordList,n)
                    break;
                elif user == 'c':
                    hand=dealHand(n)
                    temp=hand.copy()
                    count+=1
                    compPlayHand(hand, wordList, n)
                    break;
                else:
                    print "Invalid command."
                    continue
        elif choice=='r':
            if count==0:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                while user!=None:
                    user=raw_input("Enter u to have yourself play, c to have the computer play:")
                    if user == 'u':
                        playHand(temp, wordList,n)
                        break
                    elif user == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                        print "Invalid command."
                        continue
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


