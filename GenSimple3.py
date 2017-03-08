# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:41:36 2017

@author: Р.В. Шамин
"""

import math

import matplotlib.pyplot as plt

import random as rnd

# количество генов
N = 5

# функция, которую будем минимизировать
def F(x, y, z):
    return x*x*(1+math.sin(100*x)) + y*y*(1+math.sin(100*y)) + z*z*(1+math.sin(100*z))

# вычислить значение гена
def calc_gen(Gen):
    return F(Gen[0], Gen[1], Gen[2])

# получить результаты всех генов
def calc_gens(Gens):
    res = list()
    for gen in Gens:
        res.append(calc_gen(gen))
    return res

# найти номер с минимальным значением
def get_min(Res):
    i_min = 0
    min_res = Res[i_min]
    i = 0
    for r in Res:
        if r < min_res:
            i_min = i
            min_res = r
        i = i + 1
    return i_min
    
# сгенерировать новое поколение генов
def Generate(Gens, Res):
    New_Gens = list()
    
    for i in range(N):
        New_Gens.append([0, 0, 0])
        
    # ищем первый оптимальный        
    i_min = get_min(Res)
    Res[i_min] = 1000 # исключить этот номер из дальнейшего выбора
    
    # размножаем хромосомы из первого гена
    New_Gens[0][0] = Gens[i_min][0]
    New_Gens[0][1] = Gens[i_min][1]
    New_Gens[1][1] = Gens[i_min][1]
    New_Gens[1][2] = Gens[i_min][2]
    New_Gens[2][0] = Gens[i_min][0]
    New_Gens[2][2] = Gens[i_min][2]
    New_Gens[3][1] = Gens[i_min][1]
    New_Gens[4][2] = Gens[i_min][2]
    

    # ищем второй оптимальный
    i_min = get_min(Res)
    Res[i_min] = 1000 # ищем первый оптимальный

    # размножаем хромосомы из второго гена
    New_Gens[0][2] = Gens[i_min][2]
    New_Gens[1][0] = Gens[i_min][0]
    New_Gens[2][0] = Gens[i_min][0]
    New_Gens[2][2] = Gens[i_min][2]
    New_Gens[3][2] = Gens[i_min][2]
    New_Gens[4][0] = Gens[i_min][0]
    

    # ищем третий оптимальный
    i_min = get_min(Res)
    
    # размножаем хромосомы из третьего гена
    New_Gens[3][0] = Gens[i_min][0]
    New_Gens[4][2] = Gens[i_min][2]

    # деламем мутацию для трех последних генов
    New_Gens[2][0] = New_Gens[2][0] + 0.01 * (0.5 - rnd.random())
    New_Gens[2][1] = New_Gens[2][1] + 0.01 * (0.5 - rnd.random())
    New_Gens[2][2] = New_Gens[2][2] + 0.01 * (0.5 - rnd.random())

    New_Gens[3][0] = New_Gens[3][0] + 0.2 * (0.5 - rnd.random())
    New_Gens[3][1] = New_Gens[3][1] + 0.2 * (0.5 - rnd.random())
    New_Gens[3][2] = New_Gens[3][2] + 0.2 * (0.5 - rnd.random())

    New_Gens[4][0] = New_Gens[4][0] + 0.3 * (0.5 - rnd.random())
    New_Gens[4][1] = New_Gens[4][1] + 0.3 * (0.5 - rnd.random())
    New_Gens[4][2] = New_Gens[4][2] + 0.3 * (0.5 - rnd.random())

    return New_Gens


# инициализируем генератор случайных чисел
rnd.seed() 

# создаем начальную популяцию
Gens = list()
Gens.append([1, 2, 3])
Gens.append([-0.5, 1, -4])
Gens.append([0.5, 1.5, -1])
Gens.append([2, 0.1, -1.5])
Gens.append([2, 1.1, -0.05])

# вычисляем первоначальные реузльтаты
Res = calc_gens(Gens)

# создаем списки для хранения результатов
Sol = list()
Sollog = list()

# главный цикл вычислений
for i in range(100):
    Gens = Generate(Gens, Res) # порождаем новое поколение
    Res = calc_gens(Gens) # вычисляем результаты
    
    # печать лучшего решения
    i_min = get_min(Res)
    print(Res[i_min])
    x = Res[i_min]
    Sol.append(x) 
    Sollog.append(math.log10(abs(x)))

# рисуем графики 
plt.figure(1)
plt.plot(Sol)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Solution")
plt.show()

plt.figure(2)
plt.plot(Sollog)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Solution")
plt.show()
