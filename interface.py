from write_notes import str_parse
import log
import change_notes as r
import output as o


def button_click():
    print('Для создания заметки введите "1": ')
    print('Для поиска по ключевым значениям введите "2": ')
    print('Для чтения файла введите "3": ')
    print('Для редактирования файла введите "4": ')
    print('Для удаления записи введите "5": ')
    print('Для завершения программы введите "0": ')

    start = int(input())
    if start == 1:
        dir = str_parse()
        log.loger(dir)
    if start == 2:
        o.write_file()
    if start == 3:
        r.print_notes()
    if start == 4:
        r.edit_notes()
    if start == 5:
        r.delete_notes()
    if start == 0:
        print('Программа завершилась удачно, спасибо!')
    else: print("Нет такой команды, поробуйте заново!")


