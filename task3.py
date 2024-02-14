file = open('products_new.csv', encoding='utf-8') # Открытие файла(таблицы) с продуктами на чтение

products = [x.split(';') for x in file] # Обработка таблицы для удобной работы с её данными
for i in range(1, len(products)):
    products[i][4] = str(float(products[i][4]))
    products[i][5] = str(float(products[i][5]))

file.close() # Закрытие файла

first_line = products[0] # Для более удобной работы с данными из таблицы первая строка хранится отдельно
products = products[1:]

products.sort(key=lambda x: x[0]) # Сортировка по категории

min_product_count = {} # Создание словаря для хранения цены по категориям 
categories = [  # Список категорий
    'Масло', 'Фрукты и овощи', 'Пищевые злаки', 'Хлебобулочные изделия', 'Злаки',
    'Зерновые продукты', 'Снеки', 'Закуски', 'Яйца, мясо и рыба', 'Напитки', 'Выпечка'
]
for c in categories: # Первичное заполнение словаря
    min_product_count[c] = []

for product in products: # Заполнение словаря списком кортежей типа: (количество, название продукта)
    min_product_count[product[0]].append((float(product[4]), product[1]))

for category in categories: # Финальное заполение словаря кортежем типа: (минимальное количество, название продукта)
    min_count = 100000
    min_count_product = ''
    for count in min_product_count[category]:
        if count[0] < min_count:
            min_count = count[0]
            min_count_product = count[1]
    min_product_count[category] = (min_count, min_count_product)

        

category = input() # Ввод категории
while category != 'молоко': # Цикл, который заканчивается, если ввести категорию 'молоко'
    try:
        print(f"В категории: '{category}' товар: '{min_product_count[category][1]}' был куплен {min_product_count[category][0]} раз")
    except:
        print("Такой категории не существует в нашей БД")
    category = input() # Ввод новой категории