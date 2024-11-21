# Импортируем библиотеку json для работы с JSON-данными.
import json


# Функция вывода меню на экран.
def showMenu():
  print()
    # Вывод меню пользователю с описанием доступных действий.
  return ("""
          1) Вывести все записи 
          2) Вывести запись по полю 
          3) Добавить запись 
          4) Удалить запись по полю 
          5) Выйти из программы
        """)


# Функция вывода информации об автомобиле.
def showVehicleInfo(data):
    # Цикл перебора всех автомобилей в списке data.
    for car in data:
        # Вывод информации об автомобиле в удобном формате.
        print(f"""
            Номер записи: {car["id"]},
            Название модели: {car["name"]},
            Название производителя: {car["manufacturer"]},
            Заправляется бензином: {car["is_petrol"]},
            Объем бака: {car["tank_volume"]}
           """)


# Функция ввода информации о новом автомобиле.
def inputAndCheckNewCarInfo():

  #создание функции для вывода ошибки
  def errorMassage(value):
    print(f"""
      Недопустимое значение {value},
      Повторите ввод корректно:""")
    print()
    
  # создание функции для проверки аргумента на строковой тип данных
  def is_string(input_str):
    if isinstance(input_str, str) and (not input_str.isdigit()):
      return
    errorMassage(input_str)

    return inputAndCheckNewCarInfo()

  # создание функции для проверки корректного ввода ответа 
  def checkAnswer(answer):
    is_string(answer)
    if (answer.lower() == "да") or (answer.lower() == "нет"):
      return
    errorMassage(answer)

  # создание функции для преобразования значения в float тип
  def toFloat(input_num):
    try:
      return float(input_num)
    except (ValueError, TypeError):
      errorMassage(input_num)



  # Запрос данных о новом автомобиле у пользователя.
  new_name = input("Введите название модели: ")
  is_string(new_name)

  new_manufacturer = input("Введите производителя: ")
  is_string(new_manufacturer)

  new_is_petrol = input("Машина заправляется бензиноом (да/нет): ")
  checkAnswer(new_is_petrol)

  new_tank_volume = toFloat(input("Введите объём бака: "))
  # Возвращает список с данными о новом автомобиле.
  return [new_name, new_manufacturer, new_is_petrol, new_tank_volume]


# Функция создания словаря с информацией о новом автомобиле.
def createNewCar(id, name, manufacturer, petrol, tank_volume):
    # Создание словаря с данными о новом автомобиле.
    new_car = {
        "id": id,
        "name": name,
        "manufacturer": manufacturer,
        "is_petrol": True if petrol.lower() == "да" else False,
        "tank_volume": tank_volume
    }
    # Возвращает словарь с данными о новом автомобиле.
    return new_car


# Функция добавления нового автомобиля в список.
def addNewCar(data, new_car):
    # Добавление нового автомобиля в список data.
    data.append(new_car)


# Функция удаления автомобиля из списка.
def deleteCar(data, id, flag):
    # Цикл перебора всех автомобилей в списке data.
    for car in data:
        # Если ID совпадает, удаляем автомобиль из списка и устанавливаем флаг find в True.
        if id == car["id"]:
            data.remove(car)
            flag = True
            break


# Функция вывода информации о завершении программы и количестве выполненных операций.
def output(count, actions_list, actions_count):
    # Вывод информации о завершении программы и количестве выполненных операций.
    print(f"""     Программа завершена.
        Кол-во операций: {count}\n
       """)

    # Вывод статистики по каждой операции
    count = 1
    print("Количество выполненных операций: ")
    for act in actions_list:
        print(f"""
            {act} : {actions_count[count]}
           """)
        count += 1
    # Возвращает None, чтобы не выводить лишний None в консоль
    return None


  

# Открытие файла cars.json в режиме чтения с кодировкой utf-8.
with open("cars.json", 'r', encoding='utf-8') as file:
    # Загрузка данных из файла в переменную data.
    data = json.load(file)

# Инициализация счетчика выполненных операций.
count = 0

# Список доступных действий.
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]

# Словарь для подсчета количества каждой операции.
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}

# Бесконечный цикл меню.
while True:
    # Вывод меню на экран.
    print(showMenu())

    # Получение номера действия от пользователя.
    num = int(input("Введите номер пункта: "))
    find = False

    # Обработка выбора пункта меню.
    if num == 1:
        # Вывод информации обо всех автомобилях.
        showVehicleInfo(data)
        # Увеличение счетчиков.
        count += 1
        actions_count[1] += 1

    elif num == 2:
        # Получение ID автомобиля от пользователя.
        id = int(input("Введите номер записи машины: "))

        # Поиск автомобиля по ID.
        for car in data:
            if id == car["id"]:
                # Вывод информации об автомобиле.
                showVehicleInfo(data)
                find = True
                break

        # Увеличение счетчиков.
        count += 1
        actions_count[2] += 1

        # Вывод сообщения, если автомобиль не найден.
        if not find:
            print("Запись не найдена.")

    elif num == 3:
        # Получение ID нового автомобиля от пользователя.
        id = int(input("Введите номер машины: "))

        # Проверка на существование ID.
        for car in data:
            if car["id"] == id:
                find = True
                break

        # Вывод сообщения об ошибке, если ID уже существует.
        if find:
            print("Такой номер уже существует.")
        # Ввод информации о новом автомобиле и добавление его в список.
        else:
            new_name, new_manufacturer, new_is_petrol, new_tank_volume = inputAndCheckNewCarInfo()
            # Создание нового автомобиля и добавление его в список.
            new_car = createNewCar(
                id, new_name, new_manufacturer, new_is_petrol, new_tank_volume)
            addNewCar(data, new_car)
            # Сохранение изменений в файл.
            with open("cars.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Машина успешно добавлена.")

        # Увеличение счетчиков.
        count += 1
        actions_count[3] += 1

    elif num == 4:
        # Получение ID автомобиля для удаления.
        id = int(input("Введите номер записи: "))
        find = False

        # Удаление автомобиля из списка.
        deleteCar(data, id, find)
        # Вывод сообщения, если автомобиль не найден.
        if not find:
            print("Запись не найдена.")
        else:
            # Сохранение изменений в файл.
            with open("cars.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно удалена.")
        # Увеличение счетчиков.
        count += 1
        actions_count[4] += 1

    elif num == 5:
        # Увеличение счетчика.
        actions_count[5] += 1
        # Вывод статистики и завершение программы.
        output(count, actions_list, actions_count)
        break

    # Обработка некорректного ввода.
    else:
        print("Такого номера нет.")