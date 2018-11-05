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

print('{} {}'.format(COUNT_SENTENS, sentences))
print('{} {}'.format(COUNT_WORDS, words))
print('{} {}'.format(COUNT_SYLLABLES, count))

# Alina
# Средняя дина предложения в словах, длина слова в слогах, индекс удобочитаемости Флеша, pep8.
asl = words/sentences
asw = count/words

print('{} {}'.format(ASL, asl))
print('{} {}'.format(ASW, asw))

# Aigerim
# Анализ индекса Флеша и вывод, гu_local.
if FRE >= 80:
    print('{}'.format(VERY_EASY_TO_READ))
elif FRE >= 50:
    print('{}'.format(EASY_TEXT))
elif FRE >= 25:
    print('{}'.format(LITTLE_HARD_TO_READ))
else:
    print('{}'.format(HARD_TO_READ))