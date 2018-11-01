# Liza
# Создание проекта на github, анализа текста на кол-во предложений, слов и слогов.
vowel = 'аоиеёэыуюя'
text = input()
count = 0

sentences = text.count('.')
words = text.count(' ') + 1
for i in range(0, len(text)):
    if vowel.find(text[i]) != -1:
        count += 1

print('{} {}'.format('Предложений:', sentences))
print('{} {}'.format('Слов:', words))
print('{} {}'.format('Слогов:', count))

# Alina
# Средняя дина предложения в словах, длина слова в слогах, индекс удобочитаемости Флеша, pep8.

# Aygerim
# Анализ индекса Флеша и вывод, гu_local.
