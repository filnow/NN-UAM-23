import math
import random
from typing import List


def f(x: float, beta: float = 1.0):
    return 1.0 / (1.0 + math.exp(-beta * x))

def d_f(x: float, beta: float = 1.0):
    return (beta * math.exp(-beta * x)) / (math.exp(-beta * x) + 1.0)**2

def calculate_xy(w: List[List[float]], 
                 u: List[List[float]], 
                 s: List[float]):
    x = [[f(sum([w[i][j]*u[p][j] for j in range(10)])) for i in range(2)] + [1.0] for p in range(2)]
    y = [[f(sum([s[i][j]*x[p][i] for i in range(3)])) for j in range(9)] for p in range(2)]
    
    return x, y

def calculate_s(s: List[float], 
                w: List[List[float]], 
                u: List[List[float]], 
                i: int,
                j: int):
    x, y = calculate_xy(w, u, s)
    return sum([(y[p][j] - u[p][j]) * d_f(sum([s[k][j]*x[p][k] for k in range(3)])) * x[p][i] for p in range(2)]) 

def calculate_w(s: List[float], 
                w: List[List[float]], 
                u: List[List[float]], 
                i: int ,
                j: int):
    _, y = calculate_xy(w, u, s)
    suma = 0.0
    for p in range(2):
     suma += sum([(y[p][t] - u[p][t]) * d_f(y[p][t]) * s[i][t] * d_f(sum([w[i][k] * u[p][k] for k in range(10)])) * u[p][j] for t in range(9)])
    return suma

def calculate_max(w_old, w_new, s_old, s_new):
    return max(max([abs(s_new[i][j] - s_old[i][j]) for i in range(3) for j in range(9)]), 
               max([abs(w_new[i][j] - w_old[i][j]) for i in range(2) for j in range(10)]))

def ex1():
    u = [[1.0, 1.0 ,0.0 ,0.0, 1.0 ,0.0, 0.0, 1.0, 0.0, 1.0], 
         [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0]]
    
    w = [[20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10],
         [0.0, 0.0, 20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10]]
    
    s = [[20.0, 20.0, 0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 0.0, 20.0], 
         [0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 20.0], 
         [-10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0]]

    x, y = calculate_xy(w, u, s)
    
    print('###FIRST IMAGE###')
    print(f'x = {x[0]} \n')
    for i in range(0, 9, 3):
        print(f'{y[0][i:i+3]}')
    print('\n')
    print('###SECOND IMAGE###')
    print(f'x = {x[1]} \n')
    for i in range(0, 9, 3):
        print(f'{y[1][i:i+3]}')
    print('\n')

def ex2():
    C: float = 0.5
    EPS: float = 0.0001

    u = [[1.0, 1.0 ,0.0 ,0.0, 1.0 ,0.0, 0.0, 1.0, 0.0, 1.0], 
         [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0]]
    
    w_old = [[20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10],
            [0.0, 0.0, 20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10]]
    
    s_old = [[20.0, 20.0, 0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 0.0, 20.0], 
         [0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 0.0, 0.0, 20.0, 20.0], 
         [-10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0, -10.0]]

    s_new = [[s_old[i][j] - C * calculate_s(s_old, w_old, u, i, j) for j in range(9)] for i in range(3)]
    w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, i, j) for j in range(10)] for i in range(2)]

    while calculate_max(w_old, w_new, s_old, s_new) > EPS:
        s_old = s_new.copy()
        w_old = w_new.copy()

        s_new = [[s_old[i][j] - C * calculate_s(s_old, w_old, u, i, j) for j in range(9)] for i in range(3)]
        w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, i, j) for j in range(10)] for i in range(2)]

    x, y = calculate_xy(w_new, u, s_new)

    print('###FIRST IMAGE###')
    print(f'x = {x[0]} \n')
    for i in range(0, 9, 3):
        print(f'{y[0][i:i+3]}')
    print('\n')
    print('###SECOND IMAGE###')
    print(f'x = {x[1]} \n')
    for i in range(0, 9, 3):
        print(f'{y[1][i:i+3]}')
    print('\n')

def ex3():
    C: float = 0.5
    EPS: float = 0.0001
    N = 0.1

    u = [[1.0, 1.0 ,0.0 ,0.0, 1.0 ,0.0, 0.0, 1.0, 0.0, 1.0], 
         [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0]]
    
    w_old = [[random.uniform(-N, N) for _ in range(10)] for _ in range(2)] 
    s_old = [[random.uniform(-N, N) for _ in range(10)] for _ in range(3)] 

    s_new = [[s_old[i][j] - C * calculate_s(s_old, w_old, u, i, j) for j in range(9)] for i in range(3)]
    w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, i, j) for j in range(10)] for i in range(2)]

    while calculate_max(w_old, w_new, s_old, s_new) > EPS:
        s_old = s_new.copy()
        w_old = w_new.copy()

        s_new = [[s_old[i][j] - C * calculate_s(s_old, w_old, u, i, j) for j in range(9)] for i in range(3)]
        w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, i, j) for j in range(10)] for i in range(2)]

    x, y = calculate_xy(w_new, u, s_new)

    print('###FIRST IMAGE###')
    print(f'x = {x[0]} \n')
    for i in range(0, 9, 3):
        print(f'{y[0][i:i+3]}')
    print('\n')
    print('###SECOND IMAGE###')
    print(f'x = {x[1]} \n')
    for i in range(0, 9, 3):
        print(f'{y[1][i:i+3]}')
    print('\n')


if __name__ == '__main__':
    print('###EXERCISE 1###')
    ex1()
    print('###EXERCISE 2###')
    ex2()
    print('###EXERCISE 3###')
    ex3()