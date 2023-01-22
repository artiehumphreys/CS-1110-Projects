#Artie Humphreys
#bsg6vr
def card_to_value(card):
    """

    :param card: takes in a card
    :return: its numeric value based on the values assigned to cards during a game of blackjack
    """
    if card in ['2','3','4','5','6','7','8','9']:
        val = int(card)
    elif card in ['T','J','Q','K']:
        val = 10
    elif card == 'A':
        val = 1
    return(val)

def hard_score(hand):
    """

    :param hand: A string of different cards
    :return: The hard value of that hand (aces = 1)
    """
    value = 0
    for i in range (0, len(hand)):
        value = value + card_to_value(hand[i])
    return (value)

def soft_score(hand):
    """

    :param hand: A string of different cards
    :return: The soft value of that hand (first ace = 11, all others = 1)
    """
    value = 0
    acount = 0
    for i in range (0, len(hand)):
        if (hand[i] == 'A' and acount < 1):
            acount = acount +1
            value = value + 11
        else:
            value = value + card_to_value(hand[i])
    return (value)
