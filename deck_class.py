from card_class import Card
import random
ranks= ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
class Deck():
    
    def __init__(self):
        self.all_cards = []
        for r in ranks:
            for i in range(4):
                self.all_cards.append(Card(r))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        if len(self.all_cards) > 0:
            return self.all_cards.pop()
        else:
            print('The deck is out of cards')
    
            