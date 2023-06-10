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