import random


def calculate_x(i: int, t: int):
    if t == 0:
        xs[i] = random.randint(0, 1)
    else:
        u[i] = sum([w[i][j] * x[j] for j in range(25)]) - theta[i]

        if u[i] > 0: xs[i] = 1
        elif u[i] == 0: calculate_x(i, t-1)
        else: xs[i] = 0
            
x = [0,0,0,0,0,
     0,1,1,0,0,
     0,0,1,0,0,
     0,0,1,0,0,
     0,0,1,0,0]

c = [[(x[i] - 0.5) * (x[j] - 0.5) if j != i else 0 for j in range(25)] for i in range(25)]
theta = [sum(i) for i in c]
w = [[2*c[i][j] for i in range(len(c))] for j in range(len(c))]
u = [0 for _ in range(25)]
xs = [0 for _ in range(25)]


if __name__ == "__main__":
    for t in range(25):
        for i in range(25):
            calculate_x(i, t)
        print(f'\n t = {t} \n')
        print('\n'.join([' '.join(['*' if xs[i*5+j] == 1 else ' ' for j in range(5)]) for i in range(5)]))
        
            