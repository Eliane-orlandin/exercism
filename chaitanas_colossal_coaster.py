def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.
    (Adicione uma pessoa à fila 'expresso' ou 'normal' dependendo do número do bilhete.)
    :param express_queue: list - names in the Fast-track queue.(nomes na fila Fast-track.)
    :param normal_queue: list - names in the normal queue.(nomes na fila normal.)
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.(tipo de bilhete. 1 = expresso, 0 = normal.)
    :param person_name: str - name of person to add to a queue.(nome da pessoa a ser adicionada a uma fila.)
    :return: list - the (updated) queue the name was added to.(a fila (atualizada) à qual o nome foi adicionado.)
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue

