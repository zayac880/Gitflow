def str_func(value):
    """
    Принимает на вход строку и возвращает ее со всеми заглавными буквами.
    """
    return value.upper()


def word_func(value):
    """
    Принимает на вход слово и возвращает его с заглавной буквы.
    """
    return ' '.join(word.capitalize() for word in value.split())
