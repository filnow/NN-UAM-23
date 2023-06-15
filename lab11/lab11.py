import random


def GCD(a: int, b: int):
    while b:
        a, b = b, a%b
    return abs(a)

def factorian(N: int):
    t = N**2    
    while True:
        a = random.randint(0, N)

        tGCD = GCD(N, a)
        r = 0

        if tGCD > 1: return tGCD

        while ((a**r-1)%N == 0) and ((a**r) < t):
            r += 1
            
        if r%2:
            if (GCD(N, a**(r/2)-1) > 1) or (GCD(N, a**(r/2)+1) > 1):
                return tGCD


if __name__ == '__main__':
    numbers = [12, 91, 57, 143, 1737, 1859, 13843, 988027]
    for number in numbers:
        print(f'Liczba {number} = {factorian(number)} \n')
