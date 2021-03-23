import re

# Масив можливих співпадінь
names = ['вулиця', 'вул', 'провулок', 'бульвар', 'проспект']


# функція перевірки
def check_postal_address(line):
    # перетворення стрічки до нижнього регістру
    lower_string = line.lower()
    # цикл, який проходить по усіх можливих співпадіннях
    for name in names:
        # пошук співпадіння
        if re.search(f'\\b{name}\\b', lower_string) is not None:
            # співпадіння знайдено
            print(line + ' is postal address!')
            return
    # співпадіння не знайдено
    print(line + ' is NOT postal address!')


# тестування функції перевірки
check_postal_address('м. Київ вулИЦЯ Шевченка')
check_postal_address('м. Чернігів магазин прод_товарів')
check_postal_address('Луцьк вул Гагаріна')
check_postal_address('Вінниця бульвАр Коперника')
check_postal_address('Вечірній прогноз погоди')
check_postal_address('Львів ПросПект Свободи')
