import random 
from collections import Counter 

someWords = '''apple pineapple apricot banana peach'''

someWords = someWords.split(' ')

word = random.choice(someWords)		 
if __name__ == '__main__': 
	print('Guess the word! HINT: word is a name of a fruit') 
	
	for i in word:  
		print('_', end = ' ')		 
	print() 

	playing = True 
	letterGuessed = ''				 
	chances = len(word) + 2
	correct = 0
	flag = 0
	try: 
		while (chances != 0) and flag == 0:
			print() 
			chances -= 1

			try: 
				guess = str(input('Enter a letter to guess: ')) 
			except: 
				print('Enter only a letter!') 
				continue
 
			if not guess.isalpha(): 
				print('Enter only a letter') 
				continue
			elif len(guess) > 1: 
				print('Enter only a single letter') 
				continue
			elif guess in letterGuessed: 
				print('You have already guessed that letter') 
				continue

 
			if guess in word: 
				k = word.count(guess) 
				for _ in range(k):	 
					letterGuessed += guess 

			for char in word: 
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
					print(char, end = ' ') 
					correct += 1
				elif (Counter(letterGuessed) == Counter(word)):  
																
					print("The word is: ", end=' ') 
					print(word) 
					flag = 1
					print('congratulations you have won the game') 
					break  
					break  
				else: 
					print('_', end = ' ') 

			

		
		if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
			print() 
			print('sorry you lost') 
			print('The word was {}'.format(word)) 

	except KeyboardInterrupt: 
		print() 
		print('bye bye try again..') 
		exit()
