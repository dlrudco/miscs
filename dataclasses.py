def example_dataclass():
	from dataclasses import dataclass

	@dataclass
	class Card:
	    rank: str
	    suit: str
	    
	card = Card("Q", "hearts")

	print(card == card)
	# True

	print(card.rank)
	# 'Q'

	print(card)
	Card(rank='Q', suit='hearts')