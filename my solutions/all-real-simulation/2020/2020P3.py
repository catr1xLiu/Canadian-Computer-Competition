import sys
n = input()
h = input()

if (len(h) < len(n)):
    print(0)
    sys.exit()

# {letter:amount}
letters_amounts_countained_in_n = dict() 
letters_amounts_contained_in_current_windows = dict()
for a in "abcdefghijklmnopqrstuvwxyz":
    letters_amounts_countained_in_n[a] = 0
    letters_amounts_contained_in_current_windows[a] = 0

# print(letters_amounts_countained_in_n)

for i in n:
    letters_amounts_countained_in_n[i] += 1

ans = set()
for i in range(len(n)):
    letters_amounts_contained_in_current_windows[h[i]] += 1


for windows_bias in range(0, len(h)-len(n)+1):
    flag = True
    for a in "abcdefghijklmnopqrstuvwxyz":
        flag = flag and letters_amounts_countained_in_n[a] == letters_amounts_contained_in_current_windows[a]
    if flag:
        ans.add(hash(h[windows_bias:windows_bias+len(n)]))
    letters_amounts_contained_in_current_windows[h[windows_bias]] -= 1
    if windows_bias+len(n) < len(h):
        letters_amounts_contained_in_current_windows[h[windows_bias+len(n)]] += 1

print(len(ans))