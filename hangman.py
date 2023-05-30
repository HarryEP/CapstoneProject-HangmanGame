'''
The plan is to either import a set of words or have a list of 50/100 words to choose from at random.
Then we will implement the game of hangman, using a system of lives for each wrong guess and showing all wrong guesses throughout
while continuining to display the word so far.
Then we can repeat this, and have a score for how many times the word is guessed vs not guessed.
Also, we will make sure not to repeat words.
'''

def main():
    
    wordbank = ['Harry','Molly','understanding']
    play = True
    while play:
        playGame()
        play = playAgain()
    print("Thanks for playing")

def playGame():
    pass

def selectWord():
    pass

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