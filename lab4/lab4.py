import torch
import numpy as np
import torch.nn as nn

N = 50

def function1():
    F_1 = lambda X, Y, Z: 2*X**2 + 2*Y**2 + Z**2 - 2*X*Y - 2*Y*Z - 2*X + 3

    for _ in range(5):
        X, Y, Z = [torch.tensor(np.random.uniform(-N, N), requires_grad=True) for _ in range(3)]
        optimizer = torch.optim.SGD([X, Y, Z], lr=0.01, momentum=0.99)
        
        for epoch in range(2000):    
            optimizer.zero_grad()
            loss = F_1(X,Y,Z)
            loss.backward()
            optimizer.step()
            
            print(f'{X.detach().numpy():.3f}, {Y.detach().numpy():.3f}, {Z.detach().numpy():.3f}, {F_1(X,Y,Z).detach().numpy():.3f}', end="\r")
        
        print(X.detach().numpy(), Y.detach().numpy(), Z.detach().numpy(), F_1(X,Y,Z).detach().numpy(), '\n',)
 
def function2():
    F_2 = lambda X, Y: 3*X**4+4*X**3-12*X**2+12*Y**2-24*Y

    for _ in range(5):
        X, Y = [torch.tensor(np.random.uniform(-N, N), requires_grad=True) for _ in range(2)]
        optimizer = torch.optim.SGD([X, Y], lr=0.00001, momentum=0.99)
        
        for epoch in range(2000):    
            optimizer.zero_grad()
            loss = F_2(X,Y)
            loss.backward()
            optimizer.step()
            
            print(f'{X.detach().numpy():.3f}, {Y.detach().numpy():.3f}, {F_2(X,Y).detach().numpy():.3f}', end="\r")
        
        print(X.detach().numpy(), Y.detach().numpy(), F_2(X,Y).detach().numpy(), '\n')


if __name__ == "__main__":
    print('######## Function 1 ########\n')
    function1()
    print('######## Function 2 ########\n')
    function2()