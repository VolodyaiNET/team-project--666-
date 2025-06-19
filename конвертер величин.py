def unit_converter():
    print("Конвертер величин")
    print("Доступные категории: длина, масса, объем, температура")
    print("Для выхода введите 'q'")

    # Коэффициенты преобразования (к базовым единицам)
    conversions = {
        "длина": {
            "м": 1,
            "км": 1000,
            "см": 0.01,
            "мм": 0.001,
            "миля": 1609.34,
            "ярд": 0.9144,
            "фут": 0.3048,
            "дюйм": 0.0254
        },
        "масса": {
            "кг": 1,
            "г": 0.001,
            "мг": 0.000001,
            "т": 1000,
            "фунт": 0.453592,
            "унция": 0.0283495
        },
        "объем": {
            "л": 1,
            "мл": 0.001,
            "м³": 1000,
            "галлон": 3.78541,
            "пинта": 0.473176,
            "кварта": 0.946353
        }
    }

    while True:
        # Выбор категории
        category = input("\nВыберите категорию (длина/масса/объем/температура): ").strip().lower()
        
        if category == 'q':
            print("Выход из конвертера")
            break
        
        if category not in conversions and category != "температура":
            print("Ошибка: неверная категория")
            continue
        
        # Конвертация температуры (особый случай)
        if category == "температура":
            try:
                value = float(input("Введите значение температуры: "))
                source_unit = input("Из (C/F/K): ").upper()
                target_unit = input("В (C/F/K): ").upper()
                
                # Конвертация через Цельсии
                if source_unit == "C":
                    celsius = value
                elif source_unit == "F":
                    celsius = (value - 32) * 5/9
                elif source_unit == "K":
                    celsius = value - 273.15
                else:
                    print("Ошибка: неверная единица измерения")
                    continue
                
                # Конвертация в целевую единицу
                if target_unit == "C":
                    result = celsius
                elif target_unit == "F":
                    result = celsius * 9/5 + 32
                elif target_unit == "K":
                    result = celsius + 273.15
                else:
                    print("Ошибка: неверная единица измерения")
                    continue
                    
                print(f"Результат: {result:.2f} {target_unit}")
            except ValueError:
                print("Ошибка: введите числовое значение")
            continue
        
        # Вывод доступных единиц для категории
        print(f"Доступные единицы: {', '.join(conversions[category].keys())}")
        
        # Ввод данных
        try:
            value = float(input("Введите значение: "))
            source_unit = input("Из: ").strip()
            target_unit = input("В: ").strip()
        except ValueError:
            print("Ошибка: введите числовое значение")
            continue
        
        # Проверка единиц измерения
        if source_unit not in conversions[category] or target_unit not in conversions[category]:
            print("Ошибка: неверная единица измерения")
            continue
        
        # Конвертация через базовую единицу
        in_base = value * conversions[category][source_unit]
        result = in_base / conversions[category][target_unit]
        
        print(f"Результат: {result:.6f} {target_unit}")

if __name__ == "__main__":
    unit_converter()