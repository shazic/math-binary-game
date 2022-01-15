from tkinter import N
from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import MathGame, BinaryGame

NEGATIVE_RESPONSE = "n"
MAX_QUESTIONS = 10
MIN_QUESTIONS = 1

def startGame():
    mathInstructions ='\nIn this game, you will be given a simple arithmetic question.\nEach correct answer gives you 1 mark. No marks are deducted for wrong answers.'
    binaryInstructions = '\nIn this game, you will be given a number in base 10 and would be asked to convert it to base 2.\nEach correct answer gives you 1 mark. No marks are deducted for wrong answers.'

    bg = BinaryGame(MAX_QUESTIONS)
    mg = MathGame(MAX_QUESTIONS)

    userName = input('Enter your username:')

    score = int(getUserScore(userName))

    newUser = True if score < 0 else False
    if newUser: score = 0

    print(f'Welcome {userName}. Your current score is {score}')
    userChoice = 'Y'

    while userChoice.lower() != NEGATIVE_RESPONSE:
        game = getUserChoiceOfGame()
        numPrompt = getNumberOfQuestionsPerGame()

        if game == 1:
            mg.noOfQuestions = numPrompt
            printInstructions(mathInstructions)
            score += mg.generateQuestions()
        elif game == 2:
            bg.noOfQuestions = numPrompt
            printInstructions(binaryInstructions)
            score += bg.generateQuestions()

        userChoice = input('\nDo you wish to continue with another round (y/n)?')

    updateUserScore(newUser, userName, score)

    return 0

def getUserChoiceOfGame():
    return getUserChoice([1,2], '\n1 - Maths\n2 - Binary\nWhich game would you like to play?')

def getNumberOfQuestionsPerGame():
    validOptions = [x for x in range(MIN_QUESTIONS, MAX_QUESTIONS + 1)]
    return getUserChoice(validOptions, 'How many questions do you want per game (1 - 10)?')

def getUserChoice(validOptions, queryString):
    while True:
        try:
            userChoice = int(input(f'{queryString}'))
        except Exception as e:
            print("Please enter a valid numeric value")
        
        if userChoice in validOptions: break
        print("Please enter a valid numeric value")
    return userChoice

startGame()