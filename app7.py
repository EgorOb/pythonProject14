data_f = None

while True:
    data = input("Введи вещественное число с десятичным разделителем: ")

    try:
        data_f = float(data)
        print('Все нормально')
    except TypeError:
        print('Случилась TypeError')
        continue
    except ValueError:
        print('Случилась ValueError ошибка, не могу привести к float')
        continue
    break

print(data_f)
print('End')