EXPECTED_BAKE_TIME = 40
    
def bake_time_remaining(current_time):
    """
    Calculate the remaining time.
    """
    result = EXPECTED_BAKE_TIME - current_time 
    return result

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the prep time multiplied by the number of layers.
    """
    result = number_of_layers * 2
    return result

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    result = number_of_layers * 2 + elapsed_bake_time
    return result