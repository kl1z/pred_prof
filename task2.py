file = open('products_new.csv', encoding='utf-8') # Открытие файла(таблицы) с продуктами на чтение

products = [x.split(';') for x in file] # Обработка таблицы для удобной работы с её данными
for i in range(1, len(products)):
    products[i][4] = str(float(products[i][4]))
    products[i][5] = str(float(products[i][5]))

file.close() # Закрытие файла

first_line = products[0] # Для более удобной работы с данными из таблицы первая строка хранится отдельно
products = products[1:]

products.sort(key=lambda x: x[0]) # Сортировка по категории
max_product_price = {} # Создание словаря для хранения цены по категориям 
categories = [  # Список категорий
    'Масло', 'Фрукты и овощи', 'Пищевые злаки', 'Хлебобулочные изделия', 'Злаки',
    'Зерновые продукты', 'Снеки', 'Закуски', 'Яйца, мясо и рыба', 'Напитки', 'Выпечка'
]
for c in categories: # Первичное заполнение словаря
    max_product_price[c] = []

for product in products: # Финальное заполнение словаря кортежем типа: (цена, название продукта)
    max_product_price[product[0]].append((float(product[3]), product[1]))

for category in categories: # Обработка словаря и вывод финального ответа
    max_price = 0
    max_price_product = ''
    for price in max_product_price[category]:
        if price[0] > max_price:
            max_price = price[0]
            max_price_product = price[1]
    print(f'В категории: {category} самый дорогой товар: "{max_price_product}" его цена за единицу товара составляет {max_price}' )

