u4 = [[0,0,1], [0,1,1], [1,0,1], [1,1,1]]

def neuron(x, w):
    return sum([u*w for u, w in zip(x, w)])

f = lambda x: 1 if x >= 0  else 0

def mcculloh_pitts(x, w):
    return f(neuron(x, w))

def logic_not():
    w = [-2, 1]
    return [mcculloh_pitts(u_n, w) for u_n in [[0,1], [1,0]]]

def logic_and():    
    w = [2, 2, -3]
    return [mcculloh_pitts(u_n, w) for u_n in u4]

def logic_nand():
    w = [-2, -2, 3]
    return [mcculloh_pitts(u_n, w) for u_n in u4]

def logic_or():
    w = [2, 2, -1]
    return [mcculloh_pitts(u_n, w) for u_n in u4]
    

if __name__ == '__main__':
    print(logic_not())
    print(logic_and())
    print(logic_nand())
    print(logic_or())
