import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
    secretNum=secretNum+ str(numbers[i])
    sum=secretNum
    print sum
  return secretNum

def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  
  if guess == secretNum:
    return 'You got it!'

  clue = []
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
    if len(clue) == 0:
      print 'None'
  return ' '.join(clue)
#print getClues("345",secretno) 


def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False

    for i in num:
        if i  not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            flag=False
        else:
            flag=True
    if flag == False:
        return False
    else:
        return True


def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = raw_input("Do you want to play again? Yes or No?") 
  a=play.startswith("y")
  return a

MAXGUESS=10
NUMDIGITS=3

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print 'I have thought up a number. You have %s guesses to get it.' % (MAXGUESS)
    numGuesses = 1
    guess = raw_input("Guess Again")
    while numGuesses <= MAXGUESS:
        if len(guess) != NUMDIGITS or isOnlyDigits(guess):
            print 'Guess' + str(numGuesses)
            #guess = r

        else:
          clue = getClues(guess, secretNum)
          print clue
          if guess == secretNum:
            break
        numGuesses=numGuesses+1

        if numGuesses > MAXGUESS:
          print 'You ran out of guesses. The answer was ' + secretNum

    
    else:
      if not playAgain():
        break
      
  

