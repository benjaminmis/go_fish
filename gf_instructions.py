def gf_rules():
    cont = 'y'
    while cont == 'y':
        print('Here are the rules for this version of go fish.')
        print('You will have at least seven cards in your hand')
        print('at all times.')
        print('The goal is to get the most "pairs" of cards.')
        print('When you have two of the same cards in your hand,')
        print('you will put them down. The player with the most')
        print('pairs at the end of the game wins.')
        print('Would you like more instructions? Type y or n')
        cont=input('Do you want more instructions? Enter Yes or No: ').lower().startswith('y')
        print(cont)  
        if cont == False:
            break
        else:
            print('When it is your turn, ask for a card that is in your hand.')
            print('If the computer has the card, you get to make a pair.')
            print('Both you and the computer may have to draw,')
            print('and you get to go again. If the computer does not')
            print('have that card, you draw from the deck. If you')
            print('pick up the card that you had asked for, you get')
            print('to make a pair and you get to go again!')
            print('If the computer doesn''t have the card you asked for,')
            print('and you don''t draw that card from the deck, your')
            print('turn is over and the computer gets to go.')
            print('Have fun and thanks for playing!!!')

