""" Реализация основного GUI """

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from .frames.scrollable_frame import ScrollableLabelFrame
from parsing.parsing import get_expression_coefficients, get_condition_coefficients, parse_expression
from minimize.minimize import minimize



class App(ctk.CTk):
    """ Основное GUI """
    
    
    # Размеры окна по умолчанию
    LENGTH = 500
    WIDTH = 400
    
    
    def __init__(self):
        super().__init__()
        self.function = tk.StringVar()
        
        # Настраиваем окно
        self.title("Моя программа")
        self.geometry(f"{App.LENGTH}x{App.WIDTH}")
        
        # Настраиваем сетку окна
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Добавляем виджеты
        self.conditions = ScrollableLabelFrame(self, [])
        self.entry = ctk.CTkEntry(self, textvariable=self.function)
        self.add_button = ctk.CTkButton(self, text="+", command=lambda: self.conditions.add_item(self.function.get()))
        self.optimize_button = ctk.CTkButton(self, text="Минимизировать", command=lambda: self.minimize())
        self.remove_button = ctk.CTkButton(self, text="-", command=lambda: self.conditions.remove_item(self.function.get()))
        
        # Размещаем виджеты
        self.conditions.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.entry.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.add_button.grid(row=3, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.optimize_button.grid(row=3, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.remove_button.grid(row=3, column=2, sticky="nsew", padx=(10, 10), pady=(10, 10))
        
        
    def get_minimization_task(self) -> tuple[list[int], list[list[int]]]:
        """
        Возвращает условия для задачи минимизации

        :return: Возвращает коэффициенты при x и y для главной функции
                 и для граничных условий
        :rtype: tuple[list[int], list[list[int]]]
        """
        function_coef = get_expression_coefficients(self.function.get())
        conditions = self.conditions.get_list_items()
        conditions_coef = []
        for item in conditions:
            conditions_coef.append(get_condition_coefficients(item))
        return (function_coef, conditions_coef)
    
    
    def minimize(self) -> None:
        """ Запускает задачу минимизации """
        if parse_expression(self.function.get()):
            function_, conditions = self.get_minimization_task()
            result = minimize(function_, conditions)
            messagebox.showinfo("Результат", str(result))
        else:
            messagebox.showerror("ERROR!!!", "Неверно задан формат функции для минимизации!")
            