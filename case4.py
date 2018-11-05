from ru_local_4 import *

# Liza
# Создание проекта на github, анализа текста на кол-во предложений, слов и слогов.
vowel = 'аоиеёэыуюя'
text = input(ENTER_THE_TEXT, )
count = 0

sentences = text.count('.')
words = text.count(' ') + 1
for i in range(0, len(text)):
    if vowel.find(text[i].lower()) != -1:
        count += 1

print('{} {}'.format(COUNT_SENTENS, sentences))
print('{} {}'.format(COUNT_WORDS, words))
print('{} {}'.format(COUNT_SYLLABLES, count))

# Alina
# Средняя дина предложения в словах, длина слова в слогах, индекс удобочитаемости Флеша, pep8.
asl = words / sentences
asw = count / words
fre = 206.835 - (1.3 * asl) - (60.1 * asw)

print('{} {}'.format(ASL, asl))
print('{} {}'.format(ASW, asw))
print('{} {}'.format(FRE, fre))

# Aigerim
# Анализ индекса Флеша и вывод, гu_local.
if fre >= 80:
    print('{}'.format(VERY_EASY_TO_READ))
elif fre >= 50:
    print('{}'.format(EASY_TEXT))
elif fre >= 25:
    print('{}'.format(LITTLE_HARD_TO_READ))
else:
    print('{}'.format(HARD_TO_READ))
