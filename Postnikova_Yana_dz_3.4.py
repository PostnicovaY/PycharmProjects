def thesaurus(names):
    dictionary = {el[0]: [] for el in names}
    for el in names:
        dictionary[el[0]].append(el)
    return dictionary

def thesaurus_adv(*names):
    names = sorted(names, key=lambda name: name.split(" ")[1])
    dictionary_surnames = {el.split(" ")[1][0]: [] for el in names}
    for el in names:
        dictionary_surnames[el.split(" ")[1][0]].append(el)
    for el in dictionary_surnames:
        dictionary_surnames.update({el : thesaurus(sorted(dictionary_surnames[el], key=lambda name:name.split(" ")[0]))})
    return dictionary_surnames

#Пример использования

print(thesaurus_adv("Инна Серова", "Иван Сергеев", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
