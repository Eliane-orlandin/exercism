#def trocar_dinheiro(orçamento, taxa de câmbio)
def exchange_money(budget, exchange_rate): 
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchange_amount = budget / exchange_rate
    return exchange_amount
    
#def conseguir_troco(orçamento, valor_troca)
def get_change(budget, exchanging_value):
    """:param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    remaning_budget = budget - exchanging_value
    return remaning_budget

#def obter_valor_das_contas(denominação, número_de_notas)
def get_value_of_bills(denomination, number_of_bills):
    """:param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total_accounts = denomination * number_of_bills
    return total_accounts
 
#def obter_número_de_contas(orçamento, denominação)
def get_number_of_bills(budget, denomination):
    """:param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    whole_cells = budget // denomination
    return int(whole_cells)
    
def get_leftover_of_bills(budget, denomination):
    """:param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    remaining_value = budget % denomination
    return float(remaining_value)
    
#def valor_de_troca (orçamento, câmbio_taxa, spread, denominação):
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """:param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # converter spread em decimal divindo por 100
    add_spread = spread / 100
    
    # adicionar o spread a taxa de cambio
    real_exchange_rate = (exchange_rate * add_spread) + exchange_rate

    # calcular o valor maximo moeda calculando a taxa spread
    exchanged_value = budget / real_exchange_rate

    # calcular o valor maximo na moeda estrangeira considerando denominacao da moeda.
    value_denomination = exchanged_value // denomination
    return value_denomination * denomination