import math
def func_lab4(number_task):
    if number_task == 1:
        print(
            f'Ты выбрал задание № 1, вариант - 9:\n'
            f'"Реализуйте функцию для нахождения корней квадратного уравнения."')
        a = float(input("Введи коэффициент a: "))
        b = float(input("Введи коэффициент b: "))
        c = float(input("Введи коэффициент c: "))

        def task_quadratic(a, b, c):
            discriminant = b ** 2 - 4 * a * c
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                return x1, x2
            elif discriminant == 0:
                x = -b / (2 * a)
                return x
            else:
                return "Корни не являются действительными числами"

        result = task_quadratic(a, b, c)
        print(f"Корни квадратного уравнения: {result}")
    else:
        if number_task == 2:
            print(
                f'Ты выбрал задание № 2:\n'
                f'"Напишите функцию, которая будет принимать в качестве параметров строку s,\n'
                f'а также ширину окна в символах – w. Возвращать функция должна новую строку,\n'
                f'в которой в начале добавлено необходимое количество пробелов,\n'
                f'чтобы первоначальная строка оказалась размещена по центру заданного окна.\n'
                f'Новая строка должна формироваться по следующему принципу:\n'
                f'– если длина исходной строки s больше или равна ширине заданного окна,\n'
                f'возвращаем ее в неизменном виде; в противном случае должна быть\n'
                f'возвращена строка s с ведущими пробелами в количестве (len(s) – w) // 2 штук.\n'
                f'В вашей основной программе должен осуществляться\n'
                f'пример вывода нескольких строк в окнах разной ширины."')
            user_string = input("Введите строку: ")
            window_widths = [30, 60, 90]

            def center_string(s, w):
                if len(s) >= w:
                    return s
                else:
                    leading_spaces = (w - len(s)) // 2
                    return " " * leading_spaces + s

            def display_centered_string(s, widths):
                for width in widths:
                    centered_str = center_string(s, width)
                    print(f"|{centered_str}|")
            for width in window_widths:
                display_centered_string(user_string, window_widths)
        else:
            if number_task == 3:
                print(
                    f'Ты выбрал задание № 3, вариант - 9:\n'
                    f'"Представьте, что сумма за пользование услугами такси \n'
                    f'складывается из базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.\n'
                    f'Напишите функцию, принимающую в качестве единственного параметра расстояние\n'
                    f' поездки в километрах умноженное на номер вашего варианта и возвращающую итоговую\n'
                    f'сумму оплаты такси. В основной программе должен демонстрироваться результат вызова функции.\n'
                    f'Подсказка. Цены на такси могут меняться со временем. Используйте константы для представления\n'
                    f'базового тарифа и плавающей ставки, чтобы программу можно было легко обновлять при изменении цен."')
                distance_km = float(input("Введи расстояние поездки в км: "))
                BASE_TARIFF = 4.00
                RATE_PER_KM = 0.25 / 140

                def task_taxi_fare(distance_in_km):
                    M = 1000
                    V = 9
                    fare = BASE_TARIFF + distance_in_km * M * V * RATE_PER_KM
                    return fare

                total_fare = round(task_taxi_fare(distance_km), 2)
                print(f"Итоговая сумма оплаты такси: ${total_fare}")
            else:
                print(f'Некорректный номер задания!')

