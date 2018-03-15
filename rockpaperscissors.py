#Yuchen Jin
#Rock Paper Scissors

from random import randint
import sys

win_pairs = [("rock","scissors"),
		     ("scissors","paper"),
		     ("paper","rock")]

options = ["rock", "paper", "scissors"]

def welcome():
	while True:
		response = input("Welcome to Rock Paper Scissors! Would you like to play? \n"
			"Please enter Y/N: ")
		if response.lower() != 'y' and response.lower() != 'n':
			print("Sorry invalid response. Please enter 'y' or 'n'")
			continue
		elif response.lower() == 'n':
			print("Alright you don't want to play :( Exiting...")
			sys.exit()
		else:
			break
	while True:
		try:
			num_rounds = int(input("Enter the number of rounds you want to play: "))
			rps(num_rounds)
		except ValueError:
			print("Numbers only! Please try again.")
			continue
		else:
#			return num_rounds
			break

		
def rps(num_rounds):
	
	player_points = 0
	cpu_points = 0
	r = 1 #counter used to display which round the user is on
	while num_rounds > 0:
		print("Round {}\nRock, Paper, Scissors, says shoot!".format(r))
		player_choice = input("Enter your choice: ")
		if player_choice.lower() not in options:
			print("Invalid choice. Please enter 'rock', 'paper' or 'scissors'")
		else:
			cpu_choice = options[randint(0,2)]
			print ("The computer chose: ", cpu_choice)
			pair = player_choice,cpu_choice
			if player_choice.lower() == cpu_choice:
				print("This round is a tie!")
			elif pair in win_pairs:
				player_points += 1
				print("You win this round!")
			else:
				cpu_points += 1
				print("You lose this round!")
			num_rounds -= 1
			r += 1
	if player_points > cpu_points:
		print("You win, {} to {}".format(player_points,cpu_points))
	elif cpu_points > player_points:
		print("You lose, {} to {}".format(player_points,cpu_points))
	else:
		print("You tied, {} to {}".format(player_points,cpu_points))

welcome()