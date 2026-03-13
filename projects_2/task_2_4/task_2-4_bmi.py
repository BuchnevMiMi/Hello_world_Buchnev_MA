weight = float(input('Введите ваш вес в кг: '))
height = float(input('Введите ваш рост в см: '))
calculate_height = float(height / 100)
imt = weight / calculate_height**2
print(f'Рост\t{height}\nВес\t{weight}\nИМТ\t{imt}')