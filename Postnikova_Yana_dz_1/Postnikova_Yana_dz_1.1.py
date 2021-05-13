user_sec = int(input("Введите количество секунд"))

seconds = user_sec % 60
minutes = user_sec // 60
minute = minutes % 60
hours = minutes // 60
hour = hours % 24
days = hours // 24
day = days % 30
months = days // 30
month = months % 12
years = months // 12
year = years % 100
centuries = years // 100

print((f'{centuries}' + " век. " if centuries else "") + (f'{year}' + " год. " if year else "") + (f'{month}' + " мес. " if month else "") + (f'{day}' + " дн. " if day else "") + (f'{hour}' + " час. " if hour else "") + (f'{minute}' + " мин. " if minute else "") + (f'{seconds}' + " сек. " if seconds else ""))

