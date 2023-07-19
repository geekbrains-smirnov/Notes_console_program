def loger(dir):
    with open('notes.csv', 'a', encoding='utf-8') as data:
        for title, values in dir.items():
            message, date = values
            record = f"{title};{message};{date}\n"
            data.write(record)

