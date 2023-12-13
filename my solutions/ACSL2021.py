n2s = "0123456789ABCDEF"
s2n = dict()
for i in range(len(n2s)):
    s2n[n2s[i]] = i

def hex_to_dec(hex:str) -> int:
    dec = 0
    for i in range(len(hex)):
        exp = len(hex)-1-i
        dec += s2n[hex[i]] * (16**exp)
    return dec



def dec_to_hex(dec:int) -> str:
    hex = ""
    while dec!= 0:
        # print(dec, hex)
        hex = n2s[dec%16] + hex
        dec = int(dec/16)
    
    return hex


def simplify(x:int) -> str:
    if (x<=15):
        return n2s[x]
    sum = 0
    for i in dec_to_hex(x):
        sum += s2n[i]
    return simplify(sum)

def solve(s:str,d:str,r:int) -> int:
    s = hex_to_dec(s)
    d = hex_to_dec(d)
    ans = 0
    def get_num(i):
        return s+i*d
    for term in range(int(r*(r-1)/2), int(r*(r-1)/2+r)):
        dec = get_num(term)
        for i in dec_to_hex(dec):
            ans += s2n[i]
    return ans

for i in range(5):
    tmp = input().split()
    print(simplify(solve(tmp[0], tmp[1], int(tmp[2]))))