def func_lab3(number_task):
    if number_task == 1:
        print(
            f'Ты выбрал задание № 1, вариант - 9:\n'
            f'"Напишите программу, которая проверяет, является ли введенное\n'
            f'пользователем число числом Фибоначчи с использованием цикла while."')
        userinput = int(input("Введи число: "))

        def isfibonacci(num):
            a, b = 0, 1
            while b < num:
                a, b = b, a + b
            if b == num:
                return True
            else:
                return False

        if isfibonacci(userinput):
            print(f"Число является числом Фибоначчи.")
        else:
            print(f"Число не является числом Фибоначчи.")
    else:
        if number_task == 2:
            print(
                f'Ты выбрал задание № 2, вариант - 9:\n'
                f'"Напишите программу для вычисления значения выражения (1+x)^n\n'
                f'с использованием биномиальной формулы."')
            x = int(input("Введи значение x: "))
            n = int(input("Введи значение n: "))

            def task_binomialformula(x, n):
                result = 0
                for k in range(n + 1):
                    result += math.comb(n, k) * (x ** k) * (1 ** (n - k))
                return result

            result = task_binomialformula(x, n)
            print(f"Результат выражения (1+{x})^{n} равен {result}")
        else:
            if number_task == 3:
                print(
                    f'Ты выбрал задание № 3, вариант - 9:\n'
                    f'"Напишите программу, которая находит количество различных символов в строке."')
                userinput = input("Введите строку: ")

                def task_countuniquechar(text):
                    uniquechars = set(text)
                    return len(uniquechars)

                result = task_countuniquechar(userinput)
                print(f"Количество различных символов в строке: {result}")
            else:
                print(f'Некорректный номер задания!')