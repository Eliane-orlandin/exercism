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
