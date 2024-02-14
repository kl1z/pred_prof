file = open('products.csv', encoding='utf-8')


products = [x.split(';') for x in file]
for i in range(1, len(products)):
    products[i][4] = str(float(products[i][4]))

file.close()

new_file = open('products_new.csv', 'w', encoding='utf-8')
new_file.writelines(';'.join(products[0]).rstrip() +';total\n')

final_ammount = 0

for product in products[1:]:
    ammount = float(product[3])*float(product[4])
    new_row = ';'.join(product) + ';' + str(ammount) + '\n'
    new_file.writelines(new_row)
    if product[0] == 'Закуски':
        final_ammount += ammount

new_file.close()

print(final_ammount)
