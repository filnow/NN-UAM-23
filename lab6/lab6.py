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
    x = [[f(sum([w[i][j]*u[p][j] for j in range(3)])) for i in range(2)] + [1.0] for p in range(4)]
    y = [f(sum([s[i]*x[p][i] for i in range(3)])) for p in range(4)]
    return x, y

def calculate_s(s: List[float], 
                w: List[List[float]], 
                u: List[List[float]], 
                z: List[float], 
                i: int):
    x, y = calculate_xy(w, u, s)
    p = random.randint(0, 3)
    return (y[p] - z[p]) * d_f(sum([s[j]*x[p][j] for j in range(3)])) * x[p][i] 

def calculate_w(s: List[float], 
                w: List[List[float]], 
                u: List[List[float]], 
                z: List[float], 
                i: int ,
                j: int):
    _, y = calculate_xy(w, u, s)
    p = random.randint(0, 3)
    return (y[p] - z[p]) * d_f(y[p]) * s[i] * d_f(sum([w[i][k] * u[p][k] for k in range(3)])) * u[p][j] 

def calculate_max(w_old, w_new, s_old, s_new):
    return max(max([abs(s_new[i] - s_old[i]) for i in range(3)]), 
               max([abs(w_new[i][j] - w_old[i][j]) for i in range(2) for j in range(3)]))

def main():
    C: float = 0.5
    EPS: float = 0.0001

    z = [0.0, 1.0, 1.0, 0.0]
    u = [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
    w_old = [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]
    s_old = [0.0, 1.0, 2.0]

    s_new = [s_old[i] - C * calculate_s(s_old, w_old, u, z, i) for i in range(3)]
    w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, z, i, j) for j in range(3)] for i in range(2)]

    while calculate_max(w_old, w_new, s_old, s_new) > EPS:
        s_old = s_new.copy()
        w_old = w_new.copy()

        s_new = [s_old[i] - C * calculate_s(s_old, w_old, u, z, i) for i in range(3)]
        w_new = [[w_old[i][j] - C * calculate_w(s_old, w_old, u, z, i, j) for j in range(3)] for i in range(2)]

    _, y = calculate_xy(w_new, u, s_new)

    print(f'Wagi w: {w_old} \n')
    print(f'Wagi s: {s_old} \n')
    print("Wartości XOR'a: \n")
    for xor, y_pred in zip(u, y):
        print(f'{xor} -> {y_pred:.3f}')


if __name__ == "__main__":
    main()