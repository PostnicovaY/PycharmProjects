number_translator = [
    ["ноль", "zero"],
    ["один", "one"],
    ["два", "two"],
    ["три", "three"],
    ["четыре", "four"],
    ["пять", "five"],
    ["щесть", "six"],
    ["семь", "seven"],
    ["восемь", "eight"],
    ["девять", "nine"],
    ["десять", "ten"]
]

def num_translate(numbers):
    numbers = numbers.lower()
    for el in number_translator:
        if el[1] == numbers:
            return (f'"{el[0]}"')
    return None


#Пример использования
# 1
print(num_translate("One"))
# 2

user_option = input("Вас приветствует переводчик чисел от 0 до 10 c английского на русский язык! Какое число вам перевести?\n")
while True:
    answer = num_translate(user_option)
    if not (answer is None):
        print(f'Певевод числа "{user_option}" - {answer}')
        break
    print("Ошибка ввода!")
    user_option = input("Попробуйте ввести число на английском языке еще раз:\n")