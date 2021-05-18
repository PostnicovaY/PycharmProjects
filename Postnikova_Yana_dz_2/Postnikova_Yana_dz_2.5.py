commodity_prices = [20.5, 56.23, 380.2, 4567.3, 567.28, 2347, 2, 234.45, 35, 299.99, 15725.99, 26.4]

def two_digit(el):
    while len(el) < 2:
        el = '0' + el
    return el

def cm_prices(prices):
    new_cm_prices = []
    import re
    for el in prices:
        if type(el) == int:
            el = str(el)
            el = re.sub(r'.{3}', r'\g<0> ', el[::-1])[::-1]
            new_cm_prices.append(el + ' руб')
        else:
            el = str(el)
            el = el.split('.')
            if len(el[0]) > 3:
                el[0] = re.sub(r'.{3}', r'\g<0> ', el[0][::-1])[::-1]
            new_cm_prices.append(el[0] + ' руб ' + two_digit(el[1]) + ' коп')
    text = ', '.join(new_cm_prices)
    return text

print(cm_prices(commodity_prices)) #Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
print(id(commodity_prices))
commodity_prices.sort()
print(cm_prices(commodity_prices)) #Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print(id(commodity_prices))
commodity_prices.sort(reverse = True)
print(cm_prices(commodity_prices)) #Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print(cm_prices(commodity_prices[:5])) #Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


