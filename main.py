# Импортируем библиотеку json для работы с JSON данными
import json

# Открываем файл cars.json в режиме чтения с кодировкой utf-8
with open("cars.json", 'r', encoding='utf-8') as file:
    # Загружаем данные из файла в переменную data
    data = json.load(file)

# Инициализируем счетчик всех операций
count = 0

# Список доступных действий
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]

# Словарь для подсчета количества каждой операции
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}

# Бесконечный цикл, который прерывается только при выборе пользователем пункта 5
while True:
    # Вывод меню с доступными действиями
    print(
        """
        1) Вывести все записи 
        2) Вывести запись по полю 
        3) Добавить запись 
        4) Удалить запись по полю 
        5) Выйти из программы
        """
    )

    # Получаем номер выбранного пункта меню от пользователя и преобразуем его в целое число
    num = int(input("Введите номер пункта: "))

    # Обработка выбора пункта меню
    if num == 1:
        # Цикл для вывода всех записей из списка data
        for car in data:
            # Вывод информации о машине в формате, удобном для чтения
            print(f"""
             Номер записи: {car["id"]},
             Название модели: {car["name"]},
             Название производителя: {car["manufacturer"]},
             Заправляется бензином: {"да" if car["is_petrol"] == True else "нет"},
             Объем бака: {car["tank_volume"]}
            """)
        # Увеличиваем счетчик общих операций и счетчик операций "Вывести все записи"
        count += 1
        actions_count[1] += 1

    # Вывод записи по ID
    elif num == 2:
        # Флаг для отслеживания успешности поиска записи
        find = False

        # Получаем ID записи от пользователя
        id = input("Введите номер записи машины: ").strip()
        while not id.isdigit():
            print("Неверное значение. Введите id корректно!")
            print()
            id = input("Введите номер записи машины: ").strip()

        # Цикл для поиска записи по ID
        for car in data:

            # Если ID совпадает, выводим информацию о машине и устанавливаем флаг find в True

            if id == car.get("id", 0):
                print(f"""
                Номер записи: {car["id"]},
                Название модели: {car["name"]},
                Название производителя: {car["manufacturer"]},
                Заправляется бензином: {"да" if car["is_petrol"] == True else "нет"},
                Объем бака: {car["tank_volume"]}
                """)
                find = True
                # Прерываем цикл, так как запись найдена
                break

        # Увеличиваем счетчик общих операций и счетчик операций "Вывести запись по полю"
        count += 1
        actions_count[2] += 1
        if not find:
            # Выводим сообщение о том, что запись не найдена, если find остаётся False
            print("Запись не найдена.")

    # Добавление новой записи
    elif num == 3:
        # Флаг для отслеживания успешности поиска записи
        find = False

        # Получение ID новой машины от пользователя
        id = input("Введите номер записи машины: ").strip()
        while not id.isdigit():
            print("Неверное значение. Введите id корректно!")
            print()
            id = input("Введите номер записи машины: ").strip()

        # Проверка на существование ID
        for car in data:
            if car.get("id", 0) == id:
                find = True
                break

        # Вывод сообщения об ошибке, если ID уже существует
        if find:
            print("Такой номер уже существует.")
        # Ввод данных о новой машине и создание словаря
        else:
            new_name = input("Введите название модели: ")
            new_manufacturer = input("Введите производителя: ")
            new_is_petrol = input("Машина заправляется бензином (да/нет): ").strip()

            flag = False
            if new_is_petrol.isdigit():
                flag = True
            
            while (new_is_petrol not in ["да", "нет"]) or flag:
                print("Неверное значение. Введите ответ корректно!")
                print()
                new_is_petrol = input("Машина заправляется бензином (да/нет): ")
                if new_is_petrol.isdigit():
                  flag = True
                  continue
                new_is_petrol = new_is_petrol.lower().strip()
                flag = False

            new_tank_volume = input("Введите объём бака: ")
            if not new_tank_volume.isdigit():
              while not new_tank_volume.isdigit():
                  print("Неверное значение. Введите ответ корректно!")
                  print()
                  new_tank_volume = input("Введите объём бака: ")
            new_tank_volume = float(new_tank_volume)
          
                    

            new_car = {
                "id": id,
                "name": new_name,
                "manufacturer": new_manufacturer,
                "is_petrol": True if new_is_petrol.lower() == "да" else False,
                "tank_volume": new_tank_volume
            }

            # Добавление новой машины в список data
            data.append(new_car)
            # Открытие файла для записи, сохранение обновленного списка
            with open("cars.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)

            print("\nМашина успешно добавлена.")

        # Увеличиваем счетчик общих операций и счетчик операций "Добавить запись"
        count += 1
        actions_count[3] += 1

    # Удаление записи
    elif num == 4:
        # Получение ID записи для удаления
        id = input("Введите номер записи машины: ").strip()
        while not id.isdigit():
            print("Неверное значение. Введите id корректно!")
            print()
            id = input("Введите номер записи машины: ").strip()
        find = False

        # Цикл для поиска записи по ID
        for car in data:
            # Если ID совпадает, удаляем запись и устанавливаем флаг find в True
            if id == car.get("id", 0):
                data.remove(car)
                find = True
                break
        if not find:
            # Выводим сообщение о том, что запись не найдена, если find остаётся False
            print("Запись не найдена.")

        # Сохраняем изменения в файл, если запись была найдена и удалена
        with open("cars.json", 'w', encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print("\nЗапись успешно удалена.")
        # Увеличиваем счетчик общих операций и счетчик операций "Удалить запись по полю"
        count += 1
        actions_count[4] += 1

    # Выход из программы
    elif num == 5:
        # Увеличиваем счетчик операций "Выйти из программы"
        actions_count[5] += 1
        # Выводим сообщение о завершении программы и количество выполненных операций
        print(f"""
           Программа завершена.
           Кол-во операций: {count}\n
           """)

        # Выводим сводку по количеству каждой операции
        count = 1
        print("Количество выполненных операций: ")
        for act in actions_list:
            print(f"""
             {act} : {actions_count[count]}
             """)
            count += 1
        # Прерываем цикл while True
        break

    # Обработка некорректного ввода
    else:
        print("Такого номера нет.")
