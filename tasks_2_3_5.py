
# Задание 2. Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т. е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

uniq_users = list()
values_ids = list(ids.values())
for user in values_ids:
    uniq_users.extend(user)

print(set(uniq_users))
print()

# Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них.
# Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]


def words_count(list_of_words):
    all_words = len(list_of_words)
    count_dict = {}
    for q in list_of_words:
        key = (len(q.split()))
        count_dict[key] = 0
    for q in queries:
        if len(q.split()) in count_dict.keys():
            count_dict[len(q.split())] += 1
    for key, value in count_dict.items():
        print(f'Количество запросов из {key} слов:\n  {"{:.2f}".format((value / all_words) * 100)} %')


words_count(queries)
print()

# Задание 5. *(Необязательное) Напишите код для преобразования произвольного списка вида
# ['2018-01-01', 'yandex', 'cpc', 100]  (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

a = ['2018-01-01', 'yandex', 'cpc', 100]


def list_to_dict(some_list):
    x = 1
    f_dict = dict()
    some_dict = dict()
    b = list(reversed(some_list))
    some_dict[b[1]] = b[0]
    while x < (len(b)-1):
        x += 1
        f_dict[b[x]] = some_dict.copy()
        some_dict = f_dict.copy()
        f_dict.pop(b[x])
    return some_dict


print(list_to_dict(a))
