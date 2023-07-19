def write_file():
    with open('notes.csv', 'r', encoding='utf-8') as data:
        notes = []
        for line in data:
            title, message, date = line.strip().split(';')
            notes.append({'title': title, 'message': message, 'date': date})

    search = input('Введите ключевые слова для поиска: ').lower()
    found_notes = []
    for note in notes:
        if search in note['title'].lower() or search in note['message'].lower() or search in note['date'].lower():
            found_notes.append(note)

    if found_notes:
        for note in found_notes:
            print('Заголовок:', note['title'])
            print('Сообщение:', note['message'])
            print('Дата:', note['date'])
            print('-' * 30)
    else:
        print('Ничего не найдено по заданному ключевому слову.')