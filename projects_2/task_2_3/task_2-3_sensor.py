operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")
with open('C:\\info\\task_2_3\\sensor_log.txt', 'a', encoding='utf-8') as sensor:
    sensor.write(f'{operator_name}\t{pressure} (Па)\n')

print('Данные успешно сохранены в sensor_log.txt')