def func_lab2(number_task):
    if number_task == 1:
        print(
            f'Ты выбрал задание № 1, вариант - 9:\n'
            f'"Написать программу вычисления стоимости покупки с учетом скидки.\n'
            f'Скидка в 3% предоставляется, если сумма покупки больше 500 руб, в 5% – если сумма больше 1000 руб."')
        price = float(input("Введите сумму покупки: "))

        def task_calculate_cost(price):
            discount = 0
            if price > 1000:
                discount = 0.05
            elif price > 500:
                discount = 0.03
            total_cost = price - price * discount
            return total_cost

        total_cost = task_calculate_cost(price)
        print(f"Итоговая стоимость покупки с учетом скидки: {total_cost} руб")
    else:
        if number_task == 2:
            print(
                f'Ты выбрал задание № 2, вариант - 9:\n'
                f'"Напишите программу, которая определяет, принадлежит ли точка с координатами (x; y) заштрихованной области."')
            x = float(input(f'Введите значения X:\n'))
            y = float(input(f'Введите значения Y:\n'))

            def task__dotxy(x, y):
                if y >= 0:
                    if x <= 1.5:
                        if y <= x * x:
                            count = 'принадлежит'
                        else:
                            count = 'не принадлежит'
                    else:
                        count = 'не принадлежит'
                else:
                    count = 'не принадлежит'
                return count

            print(f'Точка с координатами [{x}, {y}] {task__dotxy(x, y)} закрашенной области')
        else:
            if number_task == 3:
                print(
                    f'Ты выбрал задание № 3, вариант - 9:\n'
                    f'"На шахматной доске стоят черный король и белые ладья и слон\n'
                    f'(ладья бьет по горизонтали и вертикали, слон – по диагоналям).\n'
                    f'Проверить, есть ли угроза королю и если есть, то от кого именно.\n'
                    f'Учесть возможность защиты (например, ладья не бьет через слона)."')
                king_x, king_y = map(int, input(f'Введи X и Y позиции короля: ').split())
                rook_x, rook_y = map(int, input(f'Введи X и Y позиции ладьи: ').split())
                bishop_x, bishop_y = map(int, input(f'Введи X и Y позиции слона: ').split())

                def task_check(king_x, king_y, rook_x, rook_y, bishop_x, bishop_y):
                    # Проверяем угрожают ли королю ладья и слон
                    if king_x == rook_x or king_y == rook_y or abs(king_x - bishop_x) == abs(king_y - bishop_y):
                        # Проверяем есть ли защита от угрозы ладьи через слона
                        if (king_x == bishop_x and abs(king_y - bishop_y) <= 1) or (
                                king_y == bishop_y and abs(king_x - bishop_x) <= 1):
                            count = "Слон защищает короля от угрозы ладьи"
                        else:
                            count = "Ладья или слон угрожают королю"
                    else:
                        count = "Нет угрозы для короля"
                    return count

                result = task_check(king_x, king_y, rook_x, rook_y, bishop_x, bishop_y)
                print(f'{result}')
            else:
                print(f'Некорректный номер задания!')