﻿from ..Service.data_manager import data_manager

class presenter:

    def __init__(self):
        self.manager = data_manager()

    def print_notes(self):
        notes = self.manager.notes
        for x in notes:
            print(x)

    def create_note(self):
        input_head = input("Введите название заметки: ")
        input_body = input("Введите заметку: ")
        print(f"\nСОЗДАНА НОВАЯ ЗАМЕТКА\n{self.manager.create_note(input_head, input_body)}")

    def change_head_note(self):
        self.print_notes()
        number = int(input("Введите номер заметки для изменения: "))
        note = [number == x.ID for x in self.manager.notes]
        if note != "":
            self.manager.chage_note(note, input("Введите новое название: "), 0)
        else:
            print("Заметка не найдена")

    def change_body_note(self):
        self.print_notes()
        try:
             number = input("Введите номер заметки для изменения: ")
             for x in self.manager.notes:
                 if x.ID == number:
                     print(x)
                     self.manager.chage_note(x, input("Введите новый текст: "), 1)
        except:
             print("Ошибка ввода номера")
    def del_note(self):
        self.print_notes()
        pass