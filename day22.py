with open('input22.txt') as f:
    inputs = f.read()
    player1, player2 = inputs.split('\n\n')
    player1 = player1.replace('Player 1:\n','')
    player2 = player2.replace('Player 2:\n','')
    player1 = [int(c) for c in player1.split('\n')]
    player2 = [int(c) for c in player2.split('\n')]
print(player1)
print(player2)

def play_game(deck1, deck2):
    past_decks = []
    while not(len(deck1) == 0 or len(deck2) == 0):
        if deck1 in past_decks or deck2 in past_decks:
            print('DEFAULT')
            return True
        past_decks.append(deck1[:])
        past_decks.append(deck2[:])

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            result = play_game(deck1[:card1], deck2[:card2])
        else:
            result = card1 > card2
        if result:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])

    return len(deck1) > len(deck2)

winner = play_game(player1, player2)
end_deck = player1 if winner else player2
total = 0
for i, c in enumerate(end_deck[::-1]):
    total += c*(i+1)
print(total)