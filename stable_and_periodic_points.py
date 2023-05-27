from numpy import *
from sympy import *


def stable_point_logistic(rr):
    init_printing()
    a, r, x, x1, x2 = symbols('a r x x1 x2')  # обозначили параметры отображений и переменную за символы

    def system_1(r):  # объявляем первое логистическое отображение
        return r * x * (1 - x)

    # НЕПОДВИЖНЫЕ ТОЧКИ И ИХ УСТОЙЧИВОСТЬ
    solution_1 = solve(system_1(r) - x,
                       x)  # решаем уравнение для нахождения неподвижных точек, на выходе получаем список [0,(r-1)/r]
    stationary_point_1_2 = [solution_1[i].replace(r, rr) if i == 1 else solution_1[i] for i in range(len(solution_1))]
    # подставляем значение параметра r=rr в x0_2(r)
    multiplier_1 = diff(system_1(r),
                        x)  # берем производную, чтобы рассматривать зависимость мультипликатора от значения параметра
    value_of_multiplier_1_1 = multiplier_1.replace(x, solution_1[0])  # подставляем x0_1(r) = 0 в мультипликатор
    value_of_multiplier_1_2 = multiplier_1.replace(x, solution_1[1])  # подставляем x0_2(r) в мультипликатор
    stable_1 = (solve(abs(value_of_multiplier_1_1) < 1,
                      r))  # находим значения параметра, при которых неподвжиная точка x0_1 устойчива
    stable_2 = (solve(abs(value_of_multiplier_1_2) < 1,
                      r))  # находим значения параметра, при которых неподвжиная точка x0_2 устойчива
    stablic_1 = abs(value_of_multiplier_1_1.subs(r, rr)) < 1
    stablic_2 = abs(value_of_multiplier_1_2.subs(r, rr)) < 1
    return stationary_point_1_2, [stablic_1, stablic_2]


# ТОЧКИ 2-ПЕРИОДА ЛОГИСТИЧЕСКОГО ОТОБРАЖЕНИЯ И ИХ УСТОЙЧИВОСТЬ
def period_2_logistic(rr):
    init_printing()
    a, r, x, x1, x2 = symbols('a r x x1 x2')  # обозначили параметры отображений и переменную за символы

    def system_1(r):  # объявляем первое логистическое отображение
        return r * x * (1 - x)

    # НЕПОДВИЖНЫЕ ТОЧКИ И ИХ УСТОЙЧИВОСТЬ
    solution_1 = solve(system_1(r) - x,
                       x)  # решаем уравнение для нахождения неподвижных точек, на выходе получаем список [0,(r-1)/r]
    stationary_point_1_2 = [solution_1[i].replace(r, rr) for i in range(len(solution_1)) if i == 1]
    # подставляем значение параметра r=rr в x0_2(r)
    multiplier_1 = diff(system_1(r),
                        x)  # берем производную, чтобы рассматривать зависимость мультипликатора от значения параметра
    value_of_multiplier_1_1 = multiplier_1.replace(x, solution_1[0])  # подставляем x0_1(r) = 0 в мультипликатор
    value_of_multiplier_1_2 = multiplier_1.replace(x, solution_1[1])  # подставляем x0_2(r) в мультипликатор
    stable_1 = solve(abs(value_of_multiplier_1_1) < 1,
                     r)  # находим значения параметра, при которых неподвжиная точка x0_1 устойчива
    stable_2 = solve(abs(value_of_multiplier_1_2) < 1,
                     r)  # находим значения параметра, при которых неподвжиная точка x0_2 устойчива

    def system_period_1(x):  # объявляем первое логистическое отображение
        return r * x * (1 - x)

    period_2_points_1 = solve(system_period_1(system_period_1(x)) - x,
                              x)  # выводит и неподвижные точки, и точки периода 2
    del period_2_points_1[0:2]  # убираем неподвижные точки
    value_of_multiplier_1_3 = multiplier_1.replace(x, period_2_points_1[0])  # подставляем x_1(r) в мультипликатор
    value_of_multiplier_1_4 = multiplier_1.replace(x, period_2_points_1[1])  # подставляем x_2(r) в мультипликатор
    multiplier_2 = value_of_multiplier_1_3 * value_of_multiplier_1_4  # мультипликатор для точек периода 2
    (solve(abs(multiplier_2) < 1, r))  # находим значения параметра, при которых точки периода-2 устойчивы
    concrete_period_2_points_1 = [period_2_points_1[i].replace(r, rr) for i in range(len(period_2_points_1))]
    return period_2_points_1, concrete_period_2_points_1, abs((multiplier_2).replace(r, rr)) < 1


# НЕПОДВИЖНЫЕ ТОЧКИ ОТОБРАЖЕНИЯ ПАРАБОЛЫ И ИХ УСТОЙЧИВОСТЬ
def stable_point_parabolic(rr):
    init_printing()
    a, r, x, x1, x2 = symbols('a r x x1 x2')  # обозначили параметры отображений и переменную за символы

    def system_2(r):  # объявляем отображение параболы
        return 1 - r * x ** 2

    solution_2 = solve(system_2(r) - x,
                       x)  # решаем уравнение для нахождения неподвижных точек, на выходе получаем список [(-sqrt(4*r + 1) - 1)/(2*r), (sqrt(4*r + 1) - 1)/(2*r)]
    stationary_point_2_1 = solution_2[0].replace(r, rr)  # подставляем значение параметра r=rr в x0_1(r)
    stationary_point_2_2 = solution_2[1].replace(r, rr)  # подставляем значение параметра r=rr в x0_2(r)
    multiplier_3 = diff(system_2(r),
                        x)  # берем производную, чтобы рассматривать зависимость мультипликатора от значения параметра
    value_of_multiplier_3_1 = multiplier_3.replace(x, solution_2[
        0])  # подставляем x0_1(r) в мультипликатор - она ВСЕГДА неучтойчива, тк мультипликатор при любом параметре больше 1
    value_of_multiplier_3_2 = multiplier_3.replace(x, solution_2[1])  # подставляем x0_2(r) в мультипликатор
    stablic_1 = abs(value_of_multiplier_3_1.subs(r, rr)) < 1
    stablic_2 = abs(value_of_multiplier_3_2.subs(r, rr)) < 1
    return [stationary_point_2_1, stationary_point_2_2], [stablic_1, stablic_2]


# ТОЧКИ ПЕРИОДА-2 ОТОБРАЖЕНИЯ ПАРАБОЛЫ
def period_2_parabolic(rr):
    init_printing()
    a, r, x, x1, x2 = symbols('a r x x1 x2')  # обозначили параметры отображений и переменную за символы

    def system_2(r):  # объявляем отображение параболы
        return 1 - r * x ** 2

    solution_2 = solve(system_2(r) - x,
                       x)  # решаем уравнение для нахождения неподвижных точек, на выходе получаем список [(-sqrt(4*r + 1) - 1)/(2*r), (sqrt(4*r + 1) - 1)/(2*r)]
    stationary_point_2_1 = solution_2[0].replace(r, rr)  # подставляем значение параметра r=rr в x0_1(r)
    stationary_point_2_2 = solution_2[1].replace(r, rr)  # подставляем значение параметра r=rr в x0_2(r)
    multiplier_3 = diff(system_2(r),
                        x)  # берем производную, чтобы рассматривать зависимость мультипликатора от значения параметра
    value_of_multiplier_3_1 = multiplier_3.replace(x, solution_2[
        0])  # подставляем x0_1(r) в мультипликатор - она ВСЕГДА неучтойчива, тк мультипликатор при любом параметре больше 1
    value_of_multiplier_3_2 = multiplier_3.replace(x, solution_2[1])  # подставляем x0_2(r) в мультипликатор
    stablic_1 = abs(value_of_multiplier_3_1.subs(r, rr)) < 1
    stablic_2 = abs(value_of_multiplier_3_2.subs(r, rr)) < 1

    def system_period_2(x):  # объявляем первое логистическое отображение
        return 1 - r * x ** 2
    period_2_points_2 = solve(system_period_2(system_period_2(x)) - x, x)  # выводит и неподвижные точки, и точки периода 2
    del period_2_points_2[2:]
    value_of_multiplier_3_3 = multiplier_3.replace(x, period_2_points_2[0])  # подставляем x_1(r) в мультипликатор
    value_of_multiplier_3_4 = multiplier_3.replace(x, period_2_points_2[1])  # подставляем x_2(r) в мультипликатор
    multiplier_4 = value_of_multiplier_3_3 * value_of_multiplier_3_4

    concrete_period_2_points_2 = [period_2_points_2[i].replace(r, rr) for i in range(len(period_2_points_2))]
    return period_2_points_2, concrete_period_2_points_2, abs((multiplier_4).replace(r, rr)) < 1

