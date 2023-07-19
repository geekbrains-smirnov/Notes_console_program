import datetime
import main as m


def in_data():
    notes = {}
    while True:  # Infinite loop until the user decides to stop
        command = input('Для добавления новой заметки, введите "Добавить", для выхода введите "Меню": ').lower()
        if command == 'добавить':
            title = input('Введите заголовок заметки: ')
            msg = input('Введите тело заметки: ')
            date = str(datetime.datetime.now())
            notes[title] = [msg, date]


        elif command == 'меню':
            m.main()

        else:
            print('Вы ввели неправильную команду!')
