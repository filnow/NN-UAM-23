from typing import List


def padding(matrix: List[List[int]],
             padding_size: int):
    rows = len(matrix)
    cols = len(matrix[0])
    
    padded_matrix = [[0.0] * (cols + 2 * padding_size) for _ in range(rows + 2 * padding_size)]
    
    for i in range(rows):
        for j in range(cols):
            padded_matrix[i + padding_size][j + padding_size] = matrix[i][j]
    
    return padded_matrix

def conv(u: List[List[int]], 
         w: List[List[int]], 
         theta: float, 
         H: int = 1):
    N = len(u)
    x = [[0.0] * (N-2) for _ in range(N-2)]
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            sum_val = 0.0
            for i_prime in range(-H, H+1):
                for j_prime in range(-H, H+1):
                    sum_val += w[i_prime + H][j_prime + H] * u[i + i_prime][j + j_prime]
            x[i-1][j-1] = f(sum_val - theta)
  
    return x

def pooling(x: List[List[int]], 
            theta_prime: float, 
            H: int = 1):
    N = len(x)
    y = [[0.0] * (N-2) for _ in range(1, N-1)]
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            sum_val = 0.0
            for i_prime in range(-H, H+1):
                for j_prime in range(-H, H+1):
                    sum_val += x[i + i_prime][j + j_prime]
            y[i-1][j-1] = f(((1/(2*H+1)**2) * sum_val) - theta_prime)
    
    return y

def f(x):
    return 1.0 if x >= 0 else 0.0

def ex1():
    THETA = 2.5

    u_1 = [[0.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 1.0, 1.0, 0.0],
          [0.0, 1.0, 0.0, 1.0, 0.0],
          [0.0, 1.0, 1.0, 1.0, 0.0],
          [0.0, 0.0, 0.0, 0.0, 0.0]]
    
    u_2 = [[0.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 0.0, 0.0, 0.0],
          [1.0, 1.0, 1.0, 0.0, 0.0],
          [1.0, 0.0, 1.0, 0.0, 0.0],
          [1.0, 1.0, 1.0, 0.0, 0.0]]
    
    u_3 = [[0.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 1.0, 1.0],
          [0.0, 0.0, 1.0, 0.0, 1.0],
          [0.0, 0.0, 1.0, 1.0, 1.0],
          [0.0, 0.0, 0.0, 0.0, 0.0]]
    
    u_4 = [[0.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 1.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0],]
    
    u_5 = [[0.0, 0.0, 0.0, 0.0, 0.0],
          [1.0, 1.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0],]
    

    u = [padding(u_1, 1),
         padding(u_2, 1),
         padding(u_3, 1),
         padding(u_4, 1),
         padding(u_5, 1),]

    w = [[1.0, 1.0, 1.0],
         [1.0, 0.0, 0.0],
         [1.0, 0.0, 0.0],]
    
    for id, i in enumerate(u):
        print(f'Image u{id+1}: \n')
        for j in conv(i, w, THETA):
            print(j)
        print('\n')

def ex2():
    D_THETA = 2.5/9.0

    x_1 = [[0.0, 1.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0]]

    x_2 = [[0.0, 0.0, 0.0, 1.0, 0.0],
          [0.0, 0.0, 0.0, 0.0, 1.0],
          [0.0, 0.0, 0.0, 1.0, 0.0],
          [0.0, 0.0, 0.0, 0.0, 1.0],
          [0.0, 0.0, 0.0, 1.0, 0.0]]
    
    x = [padding(x_1, 1), 
         padding(x_2, 1)]
    
    for id, i in enumerate(x):
        print(f'Image x{id+1}: \n')
        for j in pooling(i, D_THETA):
            print(j)
        print('\n')

if __name__ == "__main__":
    print('Exercise 1: \n')
    ex1()
    print('Exercise 2: \n')
    ex2()
    