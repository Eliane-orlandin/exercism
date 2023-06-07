"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """ 
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else: 
        return False
    
def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    #cartas = hand
    #quantidade_de_cartas = len(hand)
    #soma_das_cartas = sum(cartas)
    #return soma_das_cartas / quantidade_de_cartas
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.
    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    media = (hand[0] + hand[-1])/2
    carta_do_meio = hand[len(hand) // 2]
    card_average = sum(hand) / len(hand)
    

    if media == card_average or carta_do_meio == card_average:
        return True
    else:
        return False
    
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    lista_par = []
    lista_impar = []
    
    for index, valor in enumerate(hand):
        if index % 2 == 0:
            lista_par.append(valor)
        else:
            lista_impar.append(valor)

    media_par = sum(lista_par) / len(lista_par)
    media_impar = sum(lista_impar) / len(lista_impar)
    
    if media_par == media_impar:
        return True
    else:
        return False
    