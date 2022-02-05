import time
from deck_class import Deck
class Player():
    
    def __init__(self, name='You'):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
            self.all_cards.sort(key=lambda x: x.value)
        else:
            self.all_cards.append(new_cards)
            self.all_cards.sort(key=lambda x: x.value)
                        
    def show_hand(self):
        for c in range(len(self.all_cards)):    
            print(self.all_cards[c])
    
    def ask_for_card(self):
        f = False
        while f == False:
            g = input('Ask for a card that is in your hand: ')
            f = self.check_for_card(g)  
        print(f'You asked for a {g}')
        time.sleep(.5)
        return g        
    
    def check_for_card(self,g):
        for i in range(len(self.all_cards)):
            if g == str(self.all_cards[i]):
                return True
        return False
   
    def get_index(self,g):
        for i in range(len(self.all_cards)):
            if g == str(self.all_cards[i]):
                return i
   
    def fill_hand_start(self,Deck):
        while len(self.all_cards) < 7:
            self.add_cards(Deck.deal_one())
        self.all_cards.sort(key=lambda x: x.value)  
        
    def fill_hand(self,Deck):
        if len(self.all_cards) < 7 and len(Deck.all_cards) > 0:
            print(f'{self.name} has fewer than 7 cards so {self.name} will have to draw.')
            time.sleep(1.5)
        while len(self.all_cards) < 7 and len(Deck.all_cards) > 0:
            self.add_cards(Deck.deal_one())
            if len(Deck.all_cards) == 0:
                print('The deck is out of cards.')
        self.all_cards.sort(key=lambda x: x.value)    
            