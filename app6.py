from typing import Any

def my_sum(sec: list|tuple) -> list|tuple|None:
    """
    Это функция для того-то
    :param sec: Ожидается список чего-то
    :return: Что-то
    """

    if isinstance(sec, list|tuple):
        return sec
    return {}

print(my_sum({}))