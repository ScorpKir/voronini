""" Реализация области с прокруткой """

import customtkinter as ctk
from tkinter import messagebox
from copy import deepcopy
from parsing.parsing import parse_condition


class ScrollableLabelFrame(ctk.CTkScrollableFrame):
    """
    Класс списка надписей с прокруткой

    :param master: Родительский элемент
    :type master: customtkinter.CTk
    :param item_list: Список элементов области
    :type item_list: list[customtkinter.CTk]
    """
    
    def __init__(self, master: ctk.CTk, item_list: list[ctk.CTk], **kwargs):
        super().__init__(master, **kwargs)
        self.label_list = deepcopy(item_list)


    def add_item(self, item: str) -> None:
        """
        Добавляет элемент в список

        :param item: Текст очередного элемента списка
        :type item: str
        """
        if parse_condition(item):
            label = ctk.CTkLabel(self, text=item)
            label.grid(row=len(self.label_list), column=0, pady=(10, 10), padx=(10, 10))
            self.label_list.append(label)
        else:
            messagebox.showerror("ERROR!!!", "Неверно задан формат выражения!")
            

    def remove_item(self, item: str) -> None:
        """
        Удаляет элемент списка по тексту

        :param item: Текст элемента списка
        :type item: str
        """
        for label in self.label_list:
            if item == label.cget("text"):
                label.destroy()
                self.label_list.remove(label)
                return
            
            
    def get_list_items(self) -> None:
        """ Получаем список элементов """
        return [label.cget("text") for label in self.label_list]
    