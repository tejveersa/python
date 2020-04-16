"""
Tejveer Singh
CS 100 2015F Section 009 
HW 09 Cartoon Names
"""
#HW 1

def nameDictionary(lst):
    x = lst.split(",")
    nameD = {}
    for i in range(len(x)):
        if x[i] not in nameD and i %2 == 1:
            nameD(x[i]) += [x[i +1]]
    return(nameD)

namelist = ['Belcher, Bob', 'Simpson, Homer', 'Fry, Phillip', 'Cartman, Eric', 'Hill, Hank']

print(nameDictionary(namelist))

            
def familyDictionary(lst):
    diction = {}
    for x in lst:
        last = x.split(', ')[0]
        first = x.split(', ')[1]
        if last not in diction:
            diction[last] = []
        diction[last].append(first)
    return diction
        
namelist = ['Simpson, Homer', 'Gryffin, Peter', 'Simpson, Marge', 'Gryffin, Lois', 'Simpson, Bart', 'Simpson, Lisa', 'Simpson, Maggie', 'Gryffin, Chris', 'Gryffin, Meg', 'Gryffin, Stewie', 'Gryffin, Brian']
print(familyDictionary(namelist))

def familySize(lst):
    d = {}
    x = lst.split(",")
    i = 0
    while i < len(x):
        if x[i] == x[i+2]:
            count +=1
            d[x[i]] = count
            i += 2
        else:
            i += 2
            continue

#HW 2
import random

def getPlayerNames():
    print()
    player1 = input('Name of first player: ')
    player2 = input('Name of second player: ')
    return player1, player2

def boardSetup(boardSize, numTrapdoors, numCatapults):
    trapdoors = {}
    catapults = {}
    while len(trapdoors) < numTrapdoors:
        trapdoorSpace = random.randint(1, boardSize-2)
        if trapdoorSpace in trapdoors:
            continue
        destination = random.randint(0, trapdoorSpace-1)
        while destination in trapdoors:
            destination = random.randint(0, trapdoorSpace-1)
        trapdoors[trapdoorSpace] = destination


    while len(catapults) < numCatapults:
        cataSpace = random.randint(1, boardSize-3)
        if ( cataSpace in catapults or cataSpace in trapdoors ):
            continue
        destination = random.randint(cataSpace, boardSize-2)
        while (destination in catapults or destination in trapdoors):
            destination = random.randint(cataSpace, boardSize-2)
        catapults[cataSpace] = destination

    return trapdoors, catapults

def rollDie():
    return random.randint(1, 6)

def switchPlayer(currentPlayer, player1, player2):
    if currentPlayer == player1:
        return player2
    else:
        return player1

def playGame():
    boardSize = 100
    numCatapults = 10
    numTrapdoors = 10
    player1, player2 = getPlayerNames()
    trapdoors, catapults = boardSetup (boardSize, numTrapdoors, numCatapults)
    position = {player1:0, player2:0}
    currentPlayer = player1
    while True:
        print()
        print('Player is', currentPlayer)
        print(currentPlayer, 'is on', position[currentPlayer])
        move = rollDie()
        print(currentPlayer, 'rolls a', move)
        
        targetPosition = position[currentPlayer] + move

        if targetPosition >= boardSize:
            print('Sorry', targetPosition, 'is off the board. No can do,', currentPlayer)
            currentPlayer = switchPlayer(currentPlayer, player1, player2)
            continue
        position[currentPlayer] = targetPosition
        print(currentPlayer, 'moves to', position[currentPlayer])

        if position[currentPlayer] == 99:
            print(currentPlayer + " WINS!!")
            break


        if position[currentPlayer] in trapdoors:
            position[currentPlayer] = trapdoors[position[currentPlayer]]
            print('Trapdoor!', currentPlayer, 'falls to', position[currentPlayer])
            currentPlayer = switchPlayer(currentPlayer, player1, player2)
            continue

        if (position[currentPlayer] in catapults):
            position[currentPlayer] = catapults[position[currentPlayer]]
            print('Catapult!', currentPlayer, 'flung to', position[currentPlayer])
            currentPlayer = switchPlayer(currentPlayer, player1, player2)
            continue
playGame()
