from copy import deepcopy as cp
from math import sqrt


def count_prime_factors(num):
    factors = get_prime_factors(num)
    count = len(set(factors))
    return count

def get_prime_factors(num, factors=list()):
    for i in range(2, int(sqrt(num))+2):
        if (int(num/i) != num/i):  # how is this so freaking slow?
            continue
        factors = cp(factors) # copy it
        factors.append(i)
        return get_prime_factors(int(num/i), factors)
    factors.append(num)
    return factors


def calc(n:str, p:int) -> str:
    p = len(n) - p
    result = ""
    for i in range(0, p):
        result += str(int(n[i]) + int(n[p]))
    result += str(count_prime_factors(int(n)))
    for i in range(p+1, len(n)):
        result += str(abs(int(n[i]) - int(n[p])))

    return result

for i in range(5):
    n, p = input().split()
    print(calc(n, int(p)))