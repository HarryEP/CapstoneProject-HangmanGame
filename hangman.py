'''
The plan is to either import a set of words or have a list of 50/100 words to choose from at random.
Then we will implement the game of hangman, using a system of lives for each wrong guess and showing all wrong guesses throughout
while continuining to display the word so far.
Then we can repeat this, and have a score for how many times the word is guessed vs not guessed.
Also, we will make sure not to repeat words.
'''

import random

def main():
    
    wordbank = ['Harry','Molly','understanding'] #random words while we test
    play = True
    while play:
        playGame(wordbank)
        play = playAgain()
    print("Thanks for playing")

def letterGuess(guessedLetters):
    userGuess = input("Which letter would you like to guess?: ")
    guessedLetters.append(userGuess.upper())
    return guessedLetters

def playGame(wordbank):
    guessedLetters = []
    secretWord = selectWord(wordbank)
    guessedLetters = letterGuess(guessedLetters)
    hangmanToDisplay = ""
    for letter in secretWord:
        for guess in guessedLetters:
            if letter == guess:
                print(f"Letter {letter} = guess {guess}")
                hangmanToDisplay += letter
            else:
                hangmanToDisplay += "_"
        print(letter)
    print(hangmanToDisplay)

def randomNumberGenerator(num):
    return random.randint(1,num)

def selectWord(words):
    selectedWord = words[randomNumberGenerator(len(words)) - 1]
    return selectedWord.upper()

def playAgain():
    invalidAnswer = True
    while invalidAnswer:
        userAnswer = input("Would you want to play again ('Yes'/'No')?: ")
        if userAnswer.upper() == "YES":
            return True
        elif userAnswer.upper() == "NO":
            return False
        else:
            print("Please answer either 'yes' or 'no'.")

main()