class Text:
    text = ''
    size = 0
    name = ''

    def rate(self, size_l):
        for i in size_l:
            if self.size == i:
                return size_list.index(i) + 1

    def add_new_file(self):
        result_text.insert(self.rate(size_list) - 1, f'{self.name}\n{self.size}\n{"".join(self.text)}\n')


text_1 = Text()
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1.text = file_1.readlines()
    text_1.size = len(text_1.text)

text_2 = Text()
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2.text = file_2.readlines()
    text_2.size = len(text_2.text)

text_3 = Text()
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3.text = file_3.readlines()
    text_3.size = len(text_3.text)


text_1.name = '1.txt'
text_2.name = '2.txt'
text_3.name = '3.txt'

result_text = []

size_list = [text_1.size, text_2.size, text_3.size]
size_list = sorted(size_list)
text_1.rate(size_list)
text_2.rate(size_list)
text_3.rate(size_list)

text_1.add_new_file()
text_2.add_new_file()
text_3.add_new_file()

text = ''.join(result_text)

with open('result_file.txt', 'w', encoding='utf-8') as file:
    file.write(text)

