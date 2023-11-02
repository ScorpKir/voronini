""" Модули парсинга функций и неравенств """

import sympy as sp


def get_expression_coefficients(expression: str) -> list[float]:
    """
    Преобразует выражение от x и y в виде строки
    в массив коэффициентов при x и y

    :param expression: Функция, записанная в виде строки
    :type expression: str
    :return: Исполняемая функция python
    :rtype: list[float]
    """
    # Создаем символьные переменные
    x, y = sp.symbols('x y')
    # Превращаем строку expression в символьное выражение
    expr = sp.sympify(expression)
    # Получаем коэффициенты при x и y
    return [expr.coeff(x), expr.coeff(y)]


def get_condition_coefficients(condition: str) -> list[float|str]:
    """
    Извлекает коэффициенты a, b и c их выражений вида
    
    a*x + b*y < c или a*x - b*y < c
     
    :param condition: Выражение
    :type condition: str
    :return: Список коэффициентов и какая именно операция
             применяется
    :rtype: list[float|str]
    """
    # Разбиваем строку на части
    parts = condition.split()
    c = float(parts[-1])
    action = parts[3]
    expression = ''.join(parts[0:3])
    a, b = get_expression_coefficients(expression)
    return [a, b, action, c]


def parse_condition(condition: str) -> bool:
    """
    Проверяет корректность граничного условия

    :param condition: Граничное условие для проверки
    :type condition: str
    :return: True - если выражение корректно, иначе - False
    :rtype: bool
    """
    parts = condition.split()
    try:
        c = float(parts[-1])
        sign = parts[3]
        if sign not in ('<', '<=', '>', '>=', '='):
            return False
        expression = ''.join(parts[0:3])
        x, y = sp.symbols('x y')
        expr = sp.sympify(expression)
    except Exception:
        return False
    return True


def parse_expression(expression: str) -> bool:
    """
    Проверяет корректность функции

    :param condition: Функция
    :type condition: str
    :return: True - если функция корректна, иначе - False
    :rtype: bool
    """
    parts = expression.split()
    if parts[0][-1] in ("x", "y") and parts[2][-1] in ("x", "y"):
        return True
    return False     
