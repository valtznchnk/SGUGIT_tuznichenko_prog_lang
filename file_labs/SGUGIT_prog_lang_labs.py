import file_labs.file_lab1
import file_labs.file_lab2
import file_labs.file_lab3
import file_labs.file_lab4


def SGUGIT_prog_lang_labs():
    print(
        f'Привет, какая лабораторная работа тебя интересует?\n'
        f'Будь внимателен, их всего 4!')
    number_lab = int(input())
    if number_lab == 1:
        print(
            f'Ты попал в лабораторную работу № 1!\n'
            f'Какое задание тебя интересует здесь?\n'
            f'Будь внимателен, их всего 3')
        number_task = int(input())
        file_labs.file_lab1.func_lab1(number_task)
    else:
        if number_lab == 2:
            print(
                f'Ты попал в лабораторную работу № 2!\n'
                f'Какое задание тебя интересует здесь?\n'
                f'Будь внимателен, их всего 3')
            number_task = int(input())
            file_labs.file_lab2.func_lab2(number_task)
        else:
            if number_lab == 3:
                print(
                    f'Ты попал в лабораторную работу № 3!\n'
                    f'Какое задание тебя интересует здесь?\n'
                    f'Будь внимателен, их всего 3')
                number_task = int(input())
                file_labs.file_lab3.func_lab3(number_task)
            else:
                if number_lab == 4:
                    print(
                        f'Ты попал в лабораторную работу № 4!\n'
                        f'Какое задание тебя интересует здесь?\n'
                        f'Будь внимателен, их всего 3')
                    number_task = int(input())
                    file_labs.file_lab4.func_lab4(number_task)
                else:
                    print(f'Некорректный номер лабораторной!')

SGUGIT_prog_lang_labs()
