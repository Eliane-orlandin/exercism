"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    nova_lista = []
    for item in student_scores:
        conversor = round(item)
        nova_lista.append(conversor)
    return nova_lista

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    contador = 0
    for item in student_scores:
        if item <= 40:
            contador += 1
    return contador

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.
    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    lista_aprovados = []
    for nota in student_scores:
        if nota >= threshold:
            lista_aprovados.append(nota)
    return lista_aprovados

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.
    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    diferenca = highest - 40
    limite = round(diferenca / 4)

    lista = list()

    for index, item in enumerate(range(4)):
        lista.append(41 + (limite * index))
    return lista

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.
    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    lista = []
    for index, (score, nome) in enumerate(zip(student_scores, student_names), start=1):
        classificacao = (f"{index}. {nome}: {score}")
        lista.append(classificacao)
    return lista
