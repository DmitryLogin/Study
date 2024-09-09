def custom_write(file_name, strings):
    file_name = f'{file_name}.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            tell1 = file.tell()
            file.write(f'{i}\n')
            tell2 = file.tell()
            strings_positions = [(tell1, tell2), i]
            print(strings_positions)

    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test', info)
