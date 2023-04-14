import random


N = 50
EPSILON = 0.00001

def ex1(n: int, C: float):
    F = lambda x: 2*x[0]**2 + 2*x[1]**2 + x[2]**2 - 2*x[0]*x[1] - 2*x[1]*x[2] - 2*x[1] + 3
    DF = lambda x: [4*x[0] - 2*x[1] - 2, 4*x[1] - 2*x[0] - 2*x[2], 2*x[2] - 2*x[1]]
    
    x_old = [(random.uniform(-N, N)/N - 0.5)*2*N for _ in range(n)]
    x_new = [x_old[i] - C*DF(x_old)[i] for i in range(n)]

    print(f'Values of x_old for the start {x_old}')

    while abs(F(x_new) - F(x_old)) > EPSILON:
        x_old = x_new.copy()
        x_new = [x_old[i] - C*DF(x_old)[i] for i in range(n)]

    print(f'Values of x_new at the end {x_new}\nMinimum of function {F(x_new):.3f}\n')

def ex2(n: int, C: float):
    F = lambda x: 3*x[0]**4 + 4*x[0]**3 - 12*x[0]**2 + 12*x[1]**2 - 24*x[1]
    DF = lambda x: [12*x[0]**3 + 12*x[0]**2 - 24*x[0], 24*x[1] - 24]
    
    x_old = [(random.uniform(-N, N)/N*0.5 - 0.5)*2*N for _ in range(n)]
    x_new = [x_old[i] - C*DF(x_old)[i] for i in range(n)]
    
    print(f'Values of x_old for the start {x_old}')

    while abs(F(x_new) - F(x_old)) > EPSILON:
        x_old = x_new.copy()
        x_new = [x_old[i] - C*DF(x_old)[i] for i in range(n)]
    
    print(f'Values of x_new at the end {x_new}\nMinimum of function {F(x_new):.3f}\n')


if __name__ == '__main__':
    print('########Exercise 1########')
    ex1(n=3, C=0.01)
    print('########Exercise 2########')
    ex2(n=2, C=0.00001)



