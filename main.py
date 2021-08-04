text_list = []

with open('1.txt', 'r') as text_1:
    text_1_count_lines = 0
    text_1 = text_1.read()
    for string in text_1.split('\n'):
        text_1_count_lines += 1

    text_1_string_counted = f'1.txt\n{text_1_count_lines}\n{text_1}'
    text_list.append(text_1_string_counted)


with open('2.txt', 'r') as text_2:
    text_2_count_lines = 0
    text_2 = text_2.read()
    for string in text_2.split('\n'):
        text_2_count_lines += 1

    text_2_string_counted = f'1.txt\n{text_2_count_lines}\n{text_2}'
    text_list.append(text_2_string_counted)

with open('3.txt', 'r') as text_3:
    text_3_count_lines = 0
    text_3 = text_3.read()
    for string in text_3.split('\n'):
        text_3_count_lines += 1

    text_3_string_counted = f'1.txt\n{text_3_count_lines}\n{text_3}'
    text_list.append(text_3_string_counted)

print(text_list)

