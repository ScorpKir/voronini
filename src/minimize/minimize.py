""" Реализация задачи минимизации """


from typing import Any
from scipy.optimize import linprog


def minimize(function: list[float|int], conditions: list[list[float|int]]) -> Any:
    """
    Выполняет задачу минимизации
    
    :param function: Функция для минимизации
    :type function: list[float | int]
    :param conditions: Граничные условия
    :type conditions: list[list[float | int]]
    :return: Результат выполнения задачи
    :rtype: Any
    """
    # Коэффициенты функции для минимизации
    obj = function.copy()
    # Заполняем коэффициенты
    lhs_ineq = []
    rhs_ineq = []
    lhs_eq = []
    rhs_eq = []
    for condition in conditions:
        if condition[2] == "<=":
            lhs_ineq.append(condition[:2])
            rhs_ineq.append(condition[-1])
        elif condition[2] == "=":
            lhs_eq.append(condition[:2])
            rhs_eq.append(condition[-1])  
    # Заполняем границы для x и y
    bnd = [
        (0, float("inf")),
        (0, float("inf"))
    ]
    # Проверяем есть ли у нас условия на равенство
    lhs_eq = None if len(lhs_eq) == 0 else lhs_eq
    rhs_eq = None if len(rhs_eq) == 0 else rhs_eq
    # Получаем результат оптимизации
    opt_result = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)
    return f"Минимум функции: {opt_result.get('fun', 'Не найден')}\n\nТочка минимума: {opt_result.get('x', 'Не найдена')}"
