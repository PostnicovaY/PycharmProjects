def thesaurus(*names):
    dictionary = {el[0]: [] for el in names}
    for el in names:
        dictionary[el[0]].append(el)
    return dictionary

#Пример использования

print(thesaurus("Иван", "Мария", "Петр", "Илья"))


