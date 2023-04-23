﻿#Реализовать консольное приложение заметки, с сохранением, чтением,
#добавлением, редактированием и удалением заметок. Заметка должна
#содержать идентификатор, заголовок, тело заметки и дату/время создания
#или последнего изменения заметки. Сохранение заметок необходимо сделать
#в формате json или csv формат (разделение полей рекомендуется делать через
#точку с запятой). Реализацию пользовательского интерфейса студент может
#делать как ему удобнее, можно делать как параметры запуска программы
#(команда, данные), можно делать как запрос команды с консоли и
#последующим вводом данных, как-то ещё, на усмотрение студента

from Core.Model.presenter import presenter

pres = presenter()

control_num = "-"
print("Для завершения работы нажмите '-'")

while(control_num != "-"):
    print("Список команд:\n0 - Вывести все заметки\n1 - Создать заметку\n2 - изменить заголовок заметки\n3 - изменить заметку\n4 - удалить заметку")
