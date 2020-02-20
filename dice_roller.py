import random

def main():

	dice_rolls = int(input("how many dice would you like to roll"))
	dice_sizes = int(input('how do you want your dice size'))
	dice_sum = 0
	for i in range(0,dice_rolls):
		roll = random.randint(1,dice_sizes)
		dice_sum += roll
		if roll == 1:
			print(f'you rolled a {roll}! critical fail')
		elif roll == dice_sizes:
			print(f'you rolled a {roll}! critical success')
		else: 
			print(f'you rolled a {roll}')
	print(f'you have rolled a total of {dice_sum}')


if __name__== "__main__":
  main()