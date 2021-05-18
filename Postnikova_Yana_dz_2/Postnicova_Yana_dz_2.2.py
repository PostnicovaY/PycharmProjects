my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []

def two_digit(el):
    while len(el) < 2:
        el = '0' + el
    return el


for el in my_list:
    if el.isdigit():
        new_list.append('"')
        new_list.append(two_digit(el))
        new_list.append('"')
    elif el[0] == '+':
        new_list.append('"')
        new_list.append('+' + two_digit(el[1:]))
        new_list.append('"')
    else:
        new_list.append(el)


print(new_list)

i = 0
s = ''
while i < len(new_list):
    if new_list[i] == '"':
        s = s + f'"{new_list[i+1]}" '
        i = i + 3
    else:
        s = s + f'{new_list[i]} '
        i = i + 1

print(s)