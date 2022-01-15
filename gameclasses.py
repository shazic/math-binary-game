from ast import operator
from random import randint


class Game:
    MIN_QUESTIONS = 1
    MAX_QUESTIONS = 10

    def __init__(self, noOfQuestions):
        self._noOfQuestions = noOfQuestions
    
    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < self.MIN_QUESTIONS:
            print(f'Minimum number of questions is {self.MIN_QUESTIONS}, hence setting it to {self.MIN_QUESTIONS}')
            self._noOfQuestions = 1
        elif value > self.MAX_QUESTIONS:
            print(f'Maximum number of questions can be {self.MAX_QUESTIONS}, hence setting it to {self.MAX_QUESTIONS}')
            self._noOfQuestions = 10
        else:
            self._noOfQuestions = value

    def generateQuestions(self, questionGenerator, userResponseBase = 10):

        score = 0

        for i in range(self._noOfQuestions):
            expression = questionGenerator()
            attempts = 0
            while True:
                userResult = input(f"What is {expression['expression']}?")
                attempts += 1
                try:
                    userAnswer = int(userResult, base=userResponseBase)
                except Exception as e:
                    if attempts > self.MAX_ATTEMPTS:
                        print('Too many incorrect attempts, moving on.')
                        print(f"The correct answer was {expression['result']}")
                        break
                    else:
                        print('Please use numeric value for your response')
                        continue

                if userAnswer == expression['result']:
                    print('Correct response.')
                    score += 1
                    break
                
                if attempts > self.MAX_ATTEMPTS:
                    print('Too many incorrect attempts, moving on.')
                    print(f"The correct answer was {expression['result']}")
                    break

                print('Incorrect, try again.')
        
        return score



class BinaryGame(Game):
    MAX_ATTEMPTS = 3

    def generateQuestions(self):
        score = 0
        
        for i in range(self._noOfQuestions):
            base10 = randint(1, 100)
            attempts = 0
            while True:
                userResult = input(f'What is the binary equivalent of {base10}?')
                attempts += 1
                try:
                    userAnswer = int(userResult, base=2)
                except Exception as e:
                    if attempts > self.MAX_ATTEMPTS:
                        print('Too many incorrect attempts, moving on.')
                        print('The correct answer was {:b}.'.format(base10))
                        break
                    else:
                        print('Please use valid binary notation for your response')
                        continue

                if userAnswer == base10:
                    print('Correct response.')
                    score += 1
                    break
                
                if attempts > self.MAX_ATTEMPTS:
                    print('Too many incorrect attempts, moving on.')
                    print('The correct answer was {:b}.'.format(base10))
                    break

                print('Incorrect, try again.')
        
        return score

class MathGame(Game):
    MAX_ATTEMPTS = 3

    def generateQuestions(self):
        score = 0

        for i in range(self._noOfQuestions):
            expression = self.generateExpression()
            attempts = 0
            while True:
                userResult = input(f"What is {expression['expression']}?")
                attempts += 1
                try:
                    userAnswer = int(userResult)
                except Exception as e:
                    if attempts >= self.MAX_ATTEMPTS:
                        print('Too many incorrect attempts, moving on.')
                        print(f"The correct answer was {expression['result']}")
                        break
                    else:
                        print('Please use numeric value for your response')
                        continue

                if userAnswer == expression['result']:
                    print('Correct response.')
                    score += 1
                    break
                
                if attempts >= self.MAX_ATTEMPTS:
                    print('Too many incorrect attempts, moving on.')
                    print(f"The correct answer was {expression['result']}")
                    break

                print('Incorrect, try again.')
        
        return score

    def generateExpression(self):
        expression = {}

        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"}

        for i in range(5):
            numberList[i] = randint(1, 9)

        for i in range(4):
            symbolList[i] = self.selectRandom(operatorDict)
            
            # Make sure that there are no consecutive exponential operations as this is a confusing situation
            if i > 0:
                while symbolList[i] == '**':
                    if symbolList[i - 1] != '**':
                        break
                    symbolList[i] = self.selectRandom(operatorDict)

        queryString = str(numberList[0])            
        for i in range(4):
            queryString += ' ' + symbolList[i] + ' ' + str(numberList[i + 1])
        
        expression['expression'] = queryString.replace('**', '^')
        expression['result'] = eval(queryString)

        return expression

    def selectRandom(self, dictionary, start = 1, last = 4):
        return dictionary[randint(start, last)]