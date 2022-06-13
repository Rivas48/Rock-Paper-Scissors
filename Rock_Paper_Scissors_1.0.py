import random

mylist = ['rock', 'paper', 'scissors']

Computer = random.choice(mylist)
User = input('rock paper scissors and shoot: ')

def is_win(User, Computer):
	# return true if player wins
	# rock > scissor, scissors > paper, paper > rock
	if (User == 'rock' and Computer == 'scissors') or (User == 'scissors' and Computer == 'paper') or (User == 'paper' and Computer == 'rock'):
		print('you win')
		newgamestatus = input('would you like to play again?')
		if( newgamestatus == 'yes' or newgamestatus == 'y'):
			Computer = random.choice(mylist)
			User = input('rock paper scissors and shoot: ')
			is_win(User, Computer)
	if(User == Computer):
		print('you tied')
		newgamestatus = input('would you like to play again?')
		if( newgamestatus == 'yes' or newgamestatus == 'y'):
			Computer = random.choice(mylist)
			User = input('rock paper scissors and shoot: ')
			is_win(User, Computer)
	else:
		print('you lose')
		newgamestatus = input('would you like to play again?')
		if( newgamestatus == 'yes' or newgamestatus == 'y'):
			User = input('rock paper scissors and shoot: ')
			is_win(User, Computer)

is_win(User, Computer)
