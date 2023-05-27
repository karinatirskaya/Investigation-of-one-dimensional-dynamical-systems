from numpy import *
from sympy import *
import matplotlib.pyplot as plt
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
print("Выберите отображение, которое будете исследовать:")

reflection_type = int(input("1 - Логистическое отображение rx(1-x)\n2 - Отображение параболы 1-ay^2\n"))

if reflection_type == 1:
    # logistic
    while True:
        operation = int(input("\n1 - Неподвижные точки и их устойчивость,\n"
                              "2 - Точки периода 2 и их устойчивость,\n" 
                              "3 - Итерационная диаграмма,\n"
                              "4 - Бифуркационная диаграмма,\n"
                              "5 - Показатель Ляпунова и фазовый портрет\n"
                              "0 - Выход из программы\n"))
        if operation == 1:
            from stable_and_periodic_points import stable_point_logistic
            rr = float(input("Введите параметр r: "))
            for i in range(len(stable_point_logistic(rr))):
                if stable_point_logistic(rr)[1][i]:
                    print(f"Неподвижная точка: {stable_point_logistic(rr)[0][i]} - устойчива")
                else:
                    print(f"Неподвижная точка: {stable_point_logistic(rr)[0][i]} - неустойчива")
        if operation == 2:
            from stable_and_periodic_points import period_2_logistic
            rr = float(input("Введите параметр r: "))
            output = period_2_logistic(rr)
            for i in range(len(output[0])):
                print(f"Общий закон {[i+1]}: {output[0][i]}")
            if rr >= 3:
                for i in range(len(output[1])):
                    if output[2]:
                        print(f"Точка периода два: {output[1][i]} - устойчива")
                    else:
                        print(f"Точка периода два: {output[1][i]} - неустойчива")
            else:
                print('Точек периода 2 при заданном значении параметра не существует')
        if operation == 3:
            rr = float(input("Введите параметр r: "))
            print("Итерационная диаграмма выведена в отдельном окне.\nВ построенной диаграмме рекомендуется увеличить масштаб.")
            from iterative_diagram_for_logistic import iter_diagram_logistic
            iter_diagram_logistic(rr)
        if operation == 4:
            from bifurcation_tree_logistic import bifur_logistic
            print("Бифуркационное дерево строится достаточно долго, скорость загрузки зависит от мощности вашего компьютера.\n "
                  "Подождите, пожалуйста, некоторое время и ни в коем случае не закрывйте окно программы!")
            bifur_logistic()
        if operation == 5:
            r = float(input('Введите параметр r: '))
            from indicator_of_Lyapunov_logistic import lyapunov_logistic
            print("")
            print(lyapunov_logistic(r))
        if operation == 0:
            break


elif reflection_type == 2:
    while True:
        operation = int(input("1 - Неподвижные точки и их устойчивость,\n"
                              "2 - Точки периода 2 и их устойчивость,\n"
                              "3 - Итерационная диаграмма,\n"
                              "4 - Бифуркационная диаграмма,\n"
                              "5 - Показатель Ляпунова и фазовый портрет\n"
                              "0 - Выход из программы\n"))

        if operation == 1:
            from stable_and_periodic_points import stable_point_parabolic
            rr = float(input("Введите параметр a: "))
            for i in range(len(stable_point_parabolic(rr))):
                if stable_point_parabolic(rr)[1][i]:
                    print(f"Неподвижная точка: {stable_point_parabolic(rr)[0][i]} - устойчива")
                else:
                    print(f"Неподвижная точка: {stable_point_parabolic(rr)[0][i]} - неустойчива")
        if operation == 2:
            from stable_and_periodic_points import period_2_parabolic
            rr = float(input("Введите параметр a: "))
            output = period_2_parabolic(rr)
            for i in range(len(output[0])):
                print(f"Общий закон {[i+1]}: {output[0][i]}")
            if rr >= 0.75:
                for i in range(len(output[1])):
                    if output[2]:
                        print(f"Точка периода два: {output[1][i]} - устойчива")
                    else:
                        print(f"Точка периода два: {output[1][i]} - неустойчива")
            else:
                print('Точек периода 2 при заданном значении параметра не существует')
        if operation == 3:
            rr = float(input("Введите параметр a: "))
            print("Итерационная диаграмма выведена в отдельном окне.\nВ построенной диаграмме рекомендуется увеличить масштаб.")
            from iterative_diagram_for_parabolic import iter_diagram_parabolic
            iter_diagram_parabolic(rr)
        if operation == 4:
            from bifurcation_tree_parabolic import bifur_parabolic
            print("Бифуркационное дерево строится достаточно долго, скорость загрузки зависит от мощности вашего компьютера.\n",
                  "Подождите, пожалуйста, некоторое время и ни в коем случае не закрывйте окно программы!")
            bifur_parabolic()
        if operation == 5:
            r = float(input("Введите параметр a: "))
            from indicator_of_Lyapunov_parabolic import lyapunov_parabolic
            print(lyapunov_parabolic(r))
        if operation == 0:
            break