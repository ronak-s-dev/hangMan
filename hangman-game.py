#Hangman is a word game in which the player is trying to guess a secret word.
#The player guesses letters, one at a time, and is told where each such letter
#appears in the secret word. If a guessed letter does not appear at all, it is
#considered a mistake. If the player makes six mistakes in total, the game is lost
#(you can, of course, make the game easier or harder by allowing more or fewer
#mistakes). If the player successfully guesses all the letters in the secret word,
#the player wins

#This is my(ronaksdev.web.dev@gmail.com) version of this classic game. 

import random
#Create hangman ASCII art (copied this part from Invent Your Own Computer Games using python
HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
  O  |
 /|\ |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''','''
 +---+
[O  |
/|\ |
/ \ |
 ===''', '''
 +---+
[O] |
/|\ |
/ \ |
 ===''']

#update words list using dictonary method
words = {
    'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
    'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()
}

def generateRandomWord():
    key = random.choice(list(words.keys()))                     #randomly selects a key from the words dictionary
    wordPosition = random.randint(0, len(words[key]) - 1)       #selects the index value randomly in the given range
    return [words[key][wordPosition], key]                      #returns the word and the key it is associated with

#def randomWord():
    #wordPosition = random.randint(0 , (len(words)) - 1)
    #return words[wordPosition]

secretWord, secretSet = generateRandomWord() #store the secret word


def displayConsole(correctLetters,missedLetters,secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters: ', end = '')
    for letter in missedLetters:
        print(letter, end= '')
    print()
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:        
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end = '')
    print()

alphabets = "abcdefghijklmnopqrstuvwxyz" 
def getUserGuess(alreadyGuessed):
    while True:
        print()
        guess = input("Guess a letter:").lower()
        if len(guess) != 1:
            print("Please enter a single character!")
        elif guess not in alphabets:
            print("Please enter an alphabet!")
        elif guess in alreadyGuessed:   #checks if the letter was already entered before
            print("You have already entered this character. Try again!")
        else:
            return guess
def playAgain():
    print('R E S T A R T  G A M E?')
    return input().lower().startswith('y')
        
print('H A N G M A N')
correctLetters = '' #contains all the letters that match with the secretword
missedLetters = ''  #contains all the letters that dont match with the secretword
gameEnded = False

while True:
    print('The secret word is in the category: ', secretSet)
    displayConsole(correctLetters,missedLetters,secretWord)
    guess = getUserGuess(missedLetters + correctLetters)  #pass argument of all entered letters into the getUserGuess function

    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    
    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundCorrectLetters = True          
        for i in range(len(secretWord)):            #check whether all the letters in the secret word are matching with the correct guesses
            if secretWord[i] not in correctLetters:
                foundCorrectLetters = False
                break
        if foundCorrectLetters:
            print('You have WON!, The secret word was', secretWord)
            gameEnded = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:                     #give user a limited number of chances to guess
            displayConsole(correctLetters, missedLetters, secretWord)
            print('Missed Guesses = ', str(len(missedLetters)))
            print('Correct Guesses = ', str(len(correctLetters)))
            print('The secret word was: ', secretWord)
            gameEnded = True

    if gameEnded:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameEnded = False
            secretWord, secretSet= generateRandomWord()
        else:
            break

