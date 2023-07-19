import write_notes

def read_notes():
    with open('notes.csv', 'r', encoding='utf-8') as data:
        notes = []
        for line in data:
            title, message, date = line.strip().split(';')
            notes.append({'title': title, 'message': message, 'date': date})
    return notes


def print_notes():
    all_notes = read_notes()
    for note in all_notes:
        print('Заголовок:', note['title'])
        print('Сообщение:', note['message'])
        print('Дата:', note['date'])
        print('-' * 30)


def edit_notes():
    all_notes = read_notes()
    title_to_edit = input('Введите заголовок заметки, которую хотите отредактировать: ').lower()
    for note in all_notes:
        if note['title'] == title_to_edit:
            new_message = input('Введите новое тело заметки: ')
            note['message'] = new_message
            print('Заметка успешно отредактирована!')
            with open('notes.csv', 'w', encoding='utf-8') as data:
                for note in all_notes:
                    title = note['title']
                    message = note['message']
                    date = note['date']
                    record = f"{title};{message};{date}\n"
                    data.write(record)
            return

    print('Заметка с таким заголовком не найдена.')


def delete_notes():
    all_notes = read_notes()
    title_to_delete = input('Введите заголовок заметки, которую хотите удалить: ').lower()
    for note in all_notes:
        if note['title'] == title_to_delete:
            all_notes.remove(note)
            print('Заметка успешно удалена!')
            with open('notes.csv', 'w', encoding='utf-8') as data:
                for note in all_notes:
                    title = note['title']
                    message = note['message']
                    date = note['date']
                    record = f"{title};{message};{date}\n"
                    data.write(record)
            return

    print('Заметка с таким заголовком не найдена.')
