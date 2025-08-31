nums, length = map(int, input().split())
'''
3 4
abcb
bcbb
babc
'''

alphabits = "abcdefghijklmnopqrstuvwxyz"
def to_Ls_and_Hs(s:str):
    count = dict()
    for a in alphabits:
        count[a] = 0
    for i in s:
        count[i] += 1
    res = ""
    for i in s:
        if count[i] > 1:
            res += "H"
        else:
            res += "L"
    return res

def is_alternating(Ls_and_Hs:str):
    for i in range(len(Ls_and_Hs)-1):
        if Ls_and_Hs[i] == Ls_and_Hs[i+1]:
            return False
    return True

for i in range(nums):
    s = input()
    if is_alternating(to_Ls_and_Hs(s)):
        print("T")
    else:
        print("F")