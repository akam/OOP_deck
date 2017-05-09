from random import shuffle 
import csv

def log(old_func):
	def new_func(*arg):
		with open ('deck.txt','a+') as file:
			file.write('{}\n'.format(old_func.__name__))
			print(file.read())
		return old_func(*arg)
	return new_func


class Deck():
	def __init__(self):
		suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
		self.cards = [Cards(suit, value) for suit in suits for value in values]

	@log
	def shuffle_cards(self):
		"""Shuffles deck"""
		if len(self.cards) > 0:
			shuffle(self.cards)
			return self.cards

	@log
	def deal(self):
		if len(self.cards) > 0:
			return self.cards.pop()

	@log
	def save(self):
		with open ('deck_state.csv', 'w+') as file:
			data = ['suit', 'value']
			writer = csv.DictWriter(file, fieldnames=data)
			writer.writeheader()
			for cards in self.cards:
				writer.writerow({
	    			'suit': cards.suit,
	    			'value': cards.value
	    		})

	@log
	def load(self):
		with open ('deck_state.csv', 'r') as file:
			reader = csv.DictReader(file)
			rows = list(reader)
			self.cards = [Cards(row['suit'], row['value']) for row in rows]

	def __str__(self):
		for card in self.cards:
			print(card)
		return ''

	def __iter__(self):
		self.__i = -1
		return self

	def __next__(self):
		if self.__i < len(self.cards) -1:
			self.__i += 1
			return self.cards[self.__i]
		else:
			raise StopIteration


class Cards():
	def __init__(self, suit, value):	
		self.suit = suit
		self.value = value
	def __str__(self):
		return "{} {}".format(self.suit, self.value)



d = Deck()
d.load()

for card in d:
    print(card)