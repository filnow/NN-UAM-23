import random


def calculate_c(z):
    c = [[0 for i in range(len(z))] for j in range(len(z))]
    for i in range(len(z)):
        for j in range(len(z)):
            if i != j:
                c[i][j] = (z[i]-0.5)*(z[j]-0.5)
    return c

def calucalte_w(c):
    w = [[2*c[i][j] for i in range(len(c))] for j in range(len(c))]
    theta = [sum(i) for i in c]

    return w, theta

def calculate_u(t, w, theta, i):
    u = 0
    for j in range(len(w)):
        u += w[i][j]*t[j]
    u -= theta[i]
    return u

def calculate_x(t):
    if t == 0:
        return [random.randint(0,1) for _ in range(25)]

N = 25
z = [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]

w, theta = calucalte_w(calculate_c(z))

print(calculate_x(0))


        
