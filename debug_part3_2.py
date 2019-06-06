from random import randint

def win():
	print "you win"
def loss():
	print "you loss"

while True:
	player_choice = raw_input("enter you things (rock,paper scissors) ")
	player_choice.strip()

	random_move=randint(0,2)
	option_list=["rock","paper","scissors"]
	computer_choice=option_list[random_move]
	
	if player_choice not in option_list:
		print "invalid player choice you choose again"
		continue 

	elif player_choice ==computer_choice:
		print "drow!"
	elif player_choice == "rock" and computer_choice == "scissors":
		win()
	elif player_choice == "scissors" and computer_choice == "rock":
		loss()
	elif player_choice == "paper" and computer_choice == "rock":
		win()
	elif player_choice == "rock" and computer_choice == "paper":
		loss()
	elif player_choice == "scissors" and computer_choice == "paper":
		win()
	elif player_choice == "paper" and computer_choice == "scissors":
		loss()

	again = raw_input("enter your choice (y/n)")
	if again == "y":
		continue
	elif again == "n":
		break
