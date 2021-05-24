#i - счетчик
list = [i ** 3 for i in range(1, 1000, 2)]

def sum_odds(odd_number):
    sum = 0
    while (odd_number > 0):
        sum += odd_number % 10
        odd_number //= 10
    return sum

sum = 0
for number in list:
    if sum_odds(number) % 7 == 0:
        sum += number


print(sum)

for number in list:
    number += 17
    if sum_odds(number) % 7 == 0:
        sum += number

print(sum)
