my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def two_digit(el):
    while len(el) < 2:
        el = '0' + el
    return el

i = 0
while i < len(my_list):
    if my_list[i].isdigit():
        my_list.insert(i, '"')
        my_list[i + 1] = two_digit(my_list[i + 1])
        my_list.insert(i + 2, '"')
        i = i + 3
    elif my_list[i][0] == '+':
        my_list.insert(i, '"')
        my_list[i + 1] = '+' + two_digit(my_list[i + 1][1:])
        my_list.insert(i + 2, '"')
        i = i + 3
    else:
        i = i + 1


print(my_list)

i = 0
s = ''
while i < len(my_list):
    if my_list[i] == '"':
        s = s + f'"{my_list[i+1]}" '
        i = i + 3
    else:
        s = s + f'{my_list[i]} '
        i = i + 1

print(s)