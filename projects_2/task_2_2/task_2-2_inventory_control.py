reagent = input('Введите название нового реагента: ')
our_reagent = reagent.upper()
quantity_of_reagent = input('Введите количество реагента: ')
result = (f'Уолтер, реактив {our_reagent} поступил на склад в количестве {quantity_of_reagent} шт.')

print(result)

f = open("C:\\info\\task_2_2\\inventory.txt", 'w', encoding="utf-8")
print(result, file=f)
f.close()