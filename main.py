text_list = []

with open('1.txt', 'r') as text:
    text_count_lines = 0
    text = text.read()
    for string in text.split('\n'):
        text_count_lines += 1

    text_dict = {'name': '1.txt', 'lines': str(text_count_lines), 'value': text}
    text_list.append(text_dict)


with open('2.txt', 'r') as text:
    text_count_lines = 0
    text = text.read()
    for string in text.split('\n'):
        text_count_lines += 1

    text_dict = {'name': '2.txt', 'lines': str(text_count_lines), 'value': text}
    text_list.append(text_dict)


with open('3.txt', 'r') as text:
    text_count_lines = 0
    text = text.read()
    for string in text.split('\n'):
        text_count_lines += 1

    text_dict = {'name': '3.txt', 'lines': str(text_count_lines), 'value': text}
    text_list.append(text_dict)

text_list = sorted(text_list, key=lambda k: k['lines'])

with open('result_file.txt', 'w', encoding='utf-8') as file:
    for text in text_list:
        for i in text.values():
            file.write(i + '\n')


