def func_lab1(number_task):
    if number_task == 1:
        print(f'Ты выбрал задание № 1, вариант - 9:\n'
              f'"Напишите программу, которая приветствует пользователя, выводя слово «Hello»,\n'
              f'введенное имя и знаки препинания по образцу: «Hello, USER!»"')
        print(f'Как тебя зовут?')
        name = input()

        def task_print(name):
            print(f"Hello, {name}!")

        task_print(name)
    else:
        if number_task == 2:
            print(f'Ты выбрал задание № 2, вариант - 9:\n'
                  f'"Дана строка. Посчитайте в этой строке количество всех букв «h»,\n'
                  f'кроме первого и последнего вхождения."')
            print(f'Введи предложение:')
            input_string = input()

            def task_count(input_string):
                first_h = input_string.find('h')
                last_h = input_string.rfind('h')
                if first_h != -1 and last_h != -1:
                    count = input_string.count('h', first_h + 1, last_h)
                    return count

            print(f'Количество букв "h" в введенной строке: {task_count(input_string)}')
        else:
            if number_task == 3:
                print('Ты выбрал задание № 3, вариант - 9:\n'
                      '"С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).\n'
                      'По данным числам H, M, S определите угол (в градусах),\n'
                      'на который повернулась часовая стрелка с начала суток,\n'
                      'и выведите его в виде действительного числа."')
                print(f'Введите значения H часов M минут S секунд:')
                H, M, S = map(int, input().split())

                def task_calculate_angle(H, M, S):
                    if 0 <= H < 12 and 0 <= M < 60 and 0 <= S < 60:
                        total_seconds = (H * 3600 + M * 60 + S)  # Общее количество секунд с начала суток
                        total_seconds %= 43200  # Переводим в промежуток 12 часов
                        angle = str(round(total_seconds / 43200 * 360, 2))  # Угол поворота часовой стрелки
                        out_str = 'Угол, на который повернулась часовая стрелка с начала суток: ' + angle
                        return out_str
                    else:
                        error_str = "Некорректные данные времени"
                        return error_str

                angle = task_calculate_angle(H, M, S)
                print(f'{angle}')
            else:
                print(f'Некорректный номер задания!')


