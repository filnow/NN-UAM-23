import math


C = 0.01
EPS = 0.0001
BETA = 1.0

u = [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]] # input
z = [0.0, 1.0, 1.0, 0.0] # XOR


def sigmoid(x, beta):
    return 1.0 / (1.0 + math.exp(-beta * x))
def d_sigmoid(x, beta):
    return beta * math.exp(-beta*x) / ((1.0 + math.exp(-beta * x))**2)

x_result = lambda u, w, p: [sigmoid(sum([w[i][j]*u[p][j] for j in range(3)]), BETA) for i in range(2)] + [1.0]
y_result = lambda u, w, p, s: sigmoid(sum([s[i]*x_result(u, w, p)[i] for i in range(3)]), BETA)

def DE_bias(u, w, s, z, i):
    delta = 0.0
    for p in range(4):
        x = [sigmoid(sum([w[i][j]*u[p][j] for j in range(3)]), BETA) for i in range(2)] + [1.0]
        y = sigmoid(sum([s[i]*x[i] for i in range(3)]), BETA)
        delta += (y - z[p])*d_sigmoid(sum([s[k]*x[k] for k in range(3)]), BETA) * x[i]
    return delta

def DE_weight(u, w, s, z, i, j):
    delta = 0.0
    for p in range(4):
        x = [sigmoid(sum([w[i][j]*u[p][j] for j in range(3)]), BETA) for i in range(2)] + [1.0]
        y = sigmoid(sum([s[i]*x[i] for i in range(3)]), BETA)
        delta += (y - z[p])*d_sigmoid(sum([s[k]*x[k] for k in range(3)]), BETA) * s[i] * d_sigmoid(sum([w[i][l]*u[p][l] for l in range(2)]), BETA) * u[p][j]
    return delta

def max_s(s_old, s_new):
    return max([abs(s_new[i] - s_old[i]) for i in range(3)])

def max_w(w_old, w_new):
    return max([abs(w_new[i][j] - w_old[i][j]) for j in range(3) for i in range(2)])

w_old = [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]
s_old = [0.0, 1.0, 2.0]

s_new = [s_old[i] - C * DE_bias(u, w_old, s_old, z, i) for i in range(3)]
w_new = [[w_old[i][j] - C * DE_weight(u, w_old, s_old, z, i, j) for j in range(3)] for i in range(2)]

while max(max_s(s_old, s_new), max_w(w_old, w_new)) > EPS:
    print(max(max_s(s_old, s_new), max_w(w_old, w_new)))
    s_old = s_new.copy()
    w_old = w_new.copy()
    
    s_new = [s_old[i] - C * DE_bias(u, w_old, s_old, z, i) for i in range(3)]
    w_new = [[w_old[i][j] - C * DE_weight(u, w_old, s_old, z, i, j) for j in range(3)] for i in range(2)]

print([y_result(u, w_new, p, s_new) for p in range(4)])
print("w = ",w_old)
print("s = ", s_old)



