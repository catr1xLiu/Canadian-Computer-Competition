from copy import deepcopy as cp
def count_prime_factors(num, factors=set()):
    for i in range(2, num+1):
        print(num, i)
        
        if (num%i != 0):
            factors = set(cp(list(factors))) # copy it
            factors.add(i)
            return count_prime_factors(int(num/i), factors)
    
        # if (num%i == 0):
        #     continue
        # factors = set(cp(list(factors))) # copy it
        # factors.add(i)
        # return count_prime_factors(int(num/i), factors)
        
    return len(list(factors))


def calc(n:str, p:int) -> str:
    p = len(n) - p
    result = ""
    for i in range(0, p):
        result += str(int(n[i]) + int(n[p]))
    result += str(count_prime_factors(int(n)))
    for i in range(p+1, len(n)):
        result += str(abs(int(n[i]) - int(n[p])))

    return result

# for i in range(5):
#     n, p = input().split()
#     print(calc(n, int(p)))

print(count_prime_factors(60098065452))