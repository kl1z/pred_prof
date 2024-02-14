file = open('products.csv', encoding='utf-8') # Открытие файла(таблицы) с продуктами на чтение

products = [x.split(';') for x in file] # Обработка таблицы для удобной работы с её данными
for i in range(1, len(products)):
    products[i][4] = str(float(products[i][4]))

file.close() # Закрытие файла

new_file = open('products_new.csv', 'w', encoding='utf-8') # Открытие и создание файла(таблицы) на запись
new_file.writelines(';'.join(products[0]).rstrip() +';total\n') # Добавление первой строки в таблицу, добавив при этом новый столбец total

final_ammount = 0 # Создание переменной для хранения итоговой суммы для продуктов категории "Закуски"

for product in products[1:]: # Добавление остальных строк и параллельный подсчет итоговой суммы
    ammount = float(product[3])*float(product[4])

    new_row = ';'.join(product) + ';' + str(ammount) + '\n'
    new_file.writelines(new_row)

    if product[0] == 'Закуски':
        final_ammount += ammount

new_file.close() # Закрытие файла

print(final_ammount) # Вывод суммы в консоль
