import random
stamina=10
alive=True
def report(stamin):
    if stamin > 8:
        print "The alien is strong! It resists your pathetic attack!"
    elif stamin > 5:
        print "With a loud grunt, the alien stands firm."
    elif stamin > 3:
        print "Your attack seems to be having an effect! The alien stumbles!"
    elif stamin > 0:
        print "The alien is certain to fall soon! It staggers and reels!"
    else:
        print "That's it! The alien is finished!"


def fight(stam): # stamina
    while stam > 0:
      # won't enter this loop ever. The function will always return False.
        response = raw_input("> Enter a move 1.Hit 2.attack 3.fight 4.run ")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:
            less = random.randint(0, stam)
            stam = stam - less # subtract random int from stamina
            report(stam) # see function above
        elif "fight" in response:
            print "Fight how? You have no weapons, silly space traveler!"
            return True
        elif "run" in response:
            print "Sadly, there is nowhere to run.",
            print "The spaceship is not very big."
            return True
        else:
            print "The alien zaps you with its powerful ray gun!"
            return True
    return False

print "A threatening alien wants to fight you!\n"
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive == True:
    print "\nThe alien lives on, and you, sadly, do not.\n"
else:
    print "\nThe alien has been vanquished. Good work!\n"


playAgain= raw_input("you want to play again so press y/n ")
i=0
while i<5:
    if playAgain == "y":
        fight(stamina)
        continue
    elif playAgain == "n":
        break