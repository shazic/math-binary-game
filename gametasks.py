# gametasks.py

from os import remove, rename

scoreFilename = 'userScores.txt'

def printInstructions(instructions):
    print(instructions)

def getUserScore(userName):
    try:
        scores = open(scoreFilename, 'r')
    except IOError as e:
        print(e)
        print(f'Creating file {scoreFilename}...')
        scores = open(scoreFilename, 'w')
        print(f'File {scoreFilename} created.')
        return -1

    for record in scores:
        attributes = record.split(',')
        user = attributes[0]
        score = int(attributes[1])
        if user.lower() == userName.lower():
            scores.close()
            return score

    scores.close()
    return -1

def updateUserScore(newUser, userName, score):
    if newUser:
        scores = open(scoreFilename, 'a')
        scores.write(f'{userName},{score}\n')
        scores.close()
        return 0
    else:
        userFound = False
        tmpScoresFilename = f'{scoreFilename}.tmp'
        tmpScores = open(tmpScoresFilename, 'w')
        scores = open(scoreFilename, 'r')
        for record in scores:
            attributes = record.split(',')
            user = attributes[0]
            userScore = int(attributes[1])
            if user.lower() == userName.lower():
                userFound = True
                newScore = userScore + score
                print(f'Updating score of {user} from {userScore} to {newScore}...')
                tmpScores.write(f'{userName},{newScore}\n')
            else:
                tmpScores.write(record)
        tmpScores.close()
        scores.close()
        remove(scoreFilename)
        rename(tmpScoresFilename, scoreFilename)
        if userFound:
            return 0
    
    return -1


