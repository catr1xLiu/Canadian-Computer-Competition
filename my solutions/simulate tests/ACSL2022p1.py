w = [1,1,2,3,5]

v = {"R":60, "W":0, "B":60+5, "G":5}

for i in range(5):
    _ = input().split()
    ans = 0
    for j in range(len(_)):
        ans += w[j] * v[_[j]]
    hour = str(int(ans/60)%12)
    minute = str(ans%60)
    if hour == "0":
        hour = "00"
    if minute == "0":
        minute = "00"
    print(hour+":"+minute)