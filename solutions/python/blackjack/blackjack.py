"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    #definir o valor das cartas: JQK = 10, A= 1 e as demais o valor da mesma
    if card in "JQK":
        return 10
    elif card =="A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    #criar duas variáveis para receber o card_one e o card_two.
    #Descobrir qual das cartas é a maior e retornar a de maior valor.
    #Se as duas cartas forem de valores iguais, retornar os dois valores.
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
   
    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else: 
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # Soma das 3 cartas não pode ultrapassar 21 pontos
    # Se a soma das (cartas 1 e 2) + carta 3 <= 21
    #    É as
    # else é 11
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if card_one == "A":
        value_one = 11
    if card_two == "A":
        value_two = 11
        
    total = value_one + value_two
    
    if total <= 10:
        return 11
    else: 
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
       
    card_one_is_ten_card = card_one in "JQK" or card_one == "10"
    card_two_is_ten_card = card_two in "JQK" or card_two == "10"
    card_one_is_ace_card = card_one == "A"
    card_two_is_ace_card = card_two == "A"

    if card_one_is_ten_card and card_two_is_ace_card:
        return True
    
    elif card_two_is_ten_card and card_one_is_ace_card:
        return True

    else: 
        return False