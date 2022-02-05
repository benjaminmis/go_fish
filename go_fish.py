import time
from gf_instructions import gf_rules
from gf_functions import check_for_pairs, check_player, check_deck
from IPython.display import clear_output
from player_class import Player
from deck_class import Deck

print('Welcome to Go Fish!')
np = Player(input('What is your name? '))
print(f'Welcome {np.name}!')
time.sleep(.5)
gf_rules()
print(f'{np.name}, you are going to receive 7 cards.')
cp = Player('computer')
gfdeck = Deck()
gfdeck.shuffle()
np.fill_hand_start(gfdeck)
cp.fill_hand_start(gfdeck)
np_pair_cards = []
cp_pair_cards = []
time.sleep(.5)
print('Let''s see if you drew any pairs!')
time.sleep(1)
np_pair_cards.extend(check_for_pairs(np,gfdeck))
print(f'You have {len(np_pair_cards)} pair(s).')
time.sleep(1)
print('Let''s see if the computer drew any pairs!')
time.sleep(1)
cp_pair_cards.extend(check_for_pairs(cp,gfdeck))
time.sleep(.5)
print(f'The computer has {len(cp_pair_cards)} pair(s).')
time.sleep(1)
print('You go first.')
clear_output()
time.sleep(.5)
gameon = True
player_turn = True
cp_turn = False

while gameon == True:
    
    while player_turn == True:
        if check_player(np) == False:
            player_turn = False
            break
        clear_output()
        print('This is your current hand:')
        time.sleep(1)
        np.show_hand()
        time.sleep(.5)
        print('You have these pairs so far:')
        time.sleep(.5)
        print(np_pair_cards)
        time.sleep(1)
        pguess = np.ask_for_card()
        pcomp_set = cp.check_for_card(pguess)
        time.sleep(.5)
        
        if pcomp_set == True:
            print(f'The computer has a(n) {pguess}. You now have a pair of {pguess}s')
            time.sleep(2)
            p_ind = np.get_index(pguess)
            a = np.all_cards.pop(p_ind)
            c_ind = cp.get_index(pguess)
            b = cp.all_cards.pop(c_ind)
            np_pair_cards.append([a.ranks,b.ranks])

            if check_deck(gfdeck) == True:
                print('You get to go again.')
                time.sleep(1.5)
                np.fill_hand(gfdeck)
                cp.fill_hand(gfdeck)
                np_pair_cards.extend(check_for_pairs(np,gfdeck))
                cp_pair_cards.extend(check_for_pairs(cp,gfdeck))

        else: 
            if check_deck(gfdeck) == True:
                print('The computer does not have that card. GO FISH!')
                time.sleep(2)
                c = gfdeck.deal_one()
                np.add_cards(c)
                
                if str(c) != pguess:
                    print(f'You drew a(n) {str(c)}.')
                    time.sleep(2)
                    player_turn = False
                    cp_turn = True
                
                else: 
                    print(f'You drew a(n) {str(c)}. That''s what you asked for')
                    print('so you get to go again!')
                    time.sleep(2)
                
            else: 
                print('The computer does not have that card.')
                print('There are no more cards in the deck. Next turn.')
                time.sleep(2)
                player_turn = False
                cp_turn = True
                
            np.all_cards.sort(key=lambda x: x.value)
            np_pair_cards.extend(check_for_pairs(np,gfdeck))
            cp_pair_cards.extend(check_for_pairs(cp,gfdeck))

    print('End of your turn.')
    time.sleep(1)
        
    while cp_turn == True:
        if check_player(cp) == False:
            cp_turn == False
            break
        time.sleep(.5)
        clear_output()
        time.sleep(.5)
        cguess = str(cp.all_cards[0])
        print(f'The computer asks for a(n) {cguess}.')
        time.sleep(1.2)
        ccomp_set = np.check_for_card(cguess)
        
        if ccomp_set == True:
            print(f'You have a {cguess}. The computer now has a pair of {cguess}s')
            time.sleep(1.2)
            c_ind = cp.get_index(cguess)
            a = cp.all_cards.pop(c_ind)
            p_ind = np.get_index(cguess)
            b = np.all_cards.pop(p_ind)
            cp_pair_cards.append([a.ranks,b.ranks])

            if check_deck(gfdeck) == True:
                cp.fill_hand(gfdeck)
                np.fill_hand(gfdeck)
                np_pair_cards.extend(check_for_pairs(np,gfdeck))
                cp_pair_cards.extend(check_for_pairs(cp,gfdeck))

        else: 
            if check_deck(gfdeck) == True:
                print('You do not have that card. The computer has to GO FISH!')
                time.sleep(1.5)
                cc = gfdeck.deal_one()
                cp.add_cards(cc)
                
                if str(cc) != cguess:
                    cp_turn = False
                    player_turn = True
                
            else: 
                print('You do not have that card.')
                print('There are no more cards in the deck. Next turn.')
                time.sleep(1.5)
                cp_turn = False
                player_turn = True
            cp.all_cards.sort(key=lambda x: x.value)
            cp_pair_cards.extend(check_for_pairs(cp,gfdeck))
            np_pair_cards.extend(check_for_pairs(np,gfdeck))
    print('End of the computer''s turn.')
    time.sleep(1)
            
    if check_deck(gfdeck) == False:
        gameon = False

print('game over')
print(f'The player has {len(np_pair_cards)} pairs.')
print(f'The computer has {len(cp_pair_cards)} pairs.')
if len(cp_pair_cards) > len (np_pair_cards):
    print('The computer wins!')
elif len(cp_pair_cards) < len (np_pair_cards):
    print('The player wins!')
else: 
    print('It''s a tie!')