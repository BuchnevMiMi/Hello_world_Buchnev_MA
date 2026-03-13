capsules = int(input('Число капсул'))
capacity = int(input('Вместимость упаковки'))
packages = capsules // capacity
extra = capsules % capacity

print('---Отчет фасовочного цеха---')
print(f'Число полных упаковок{packages}')
print(f'Число оставшихся капсул{extra}')