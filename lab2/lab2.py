import math


# Define the input values
u = [(0,0,1), (1,0,1), (0,1,1), (1,1,1)]

# Define the weights and biases
w1 = [[2.0, 2.0, -3.0], [2.0, 2.0, -1.0]]
s1 = [-2.0, 2.0, -1.0]

w2 = [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]
s2 = [0.0, 1.0, 2.0]

def f(x, beta): return 1.0 / (1.0 + math.exp(-beta*x))

def dnn(u, w, s, p, beta=3.0):
    x = [f(sum([w[i][j]*u[p][j] for j in range(3)]), beta) for i in range(2)] + [1.0]
    y = f(sum([s[i]*x[i] for i in range(3)]), beta)
    
    return y


if __name__ == '__main__':
    print("### ZADANIE 1 ### \n")
    for p in range(4):
        print("y({}) = {:.4f}".format(p+1, dnn(u, w1, s1, p)))
    print("### ZADANIE 2 ### \n")
    for p in range(4):
        print("y({}) = {:.4f}".format(p+1, dnn(u, w2, s2, p)))

