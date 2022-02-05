import time

def if_pairs(Player):
    for i in range(len(Player.all_cards)-1):
         if Player.all_cards[i].value == Player.all_cards[i+1].value:
                return True
    return False

def check_for_pairs(Player,Deck):
    pair = 0
    i = 0
    pair_cards = []
    while i < len(Player.all_cards)-1:
        if Player.all_cards[i].value == Player.all_cards[i+1].value:
            print(f'{Player.name} has a pair of {Player.all_cards[i]}''s')
            time.sleep(.5)          
            a = Player.all_cards.pop(i+1)
            b = Player.all_cards.pop(i)
            pair_cards.append([a.ranks,b.ranks])
            pair += 1
            i = 0
            if len(Deck.all_cards) > 0:
                Player.fill_hand(Deck)
            
        else:
            i+=1
    return pair_cards


def check_deck(Deck):
    if len(Deck.all_cards)==0:
        return False
    else:
        return True

def check_player(player):
    if len(player.all_cards)==0:
        return False
    else:
        return True

