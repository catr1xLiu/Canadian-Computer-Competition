# 思路：如果我们把k个音符变成12341234....然后1111（这里也可以2222或其他，就是要和最后一位不一样），那总good samples数 = 后面的1的数量+前面1234123的good samples数。 我们让数列一直1234123，直到good samples数超过要求，然后再弄掉几个good sample 来达到要求

import sys

n, m, k = map(int, input().split())

# 首先，我们让音乐（在符合nmk的要求下）有最多的good_samples
# 办法就是让音符一直递增，碰到k就归零，这样两个相同的音符之间的距离最远，他们中间形成的good_samples就越多
music = [1]
good_samples_count = n # 长度为1的样本都是好的
good_samples_stopat = 0
for i in range(n-1):
    good_samples_max_length = min(k, i+1)
    good_samples_count += (good_samples_max_length+2)/2*(good_samples_max_length-1)
    if good_samples_count >= k:
        good_samples_stopat = len(music)
        break
    music.append((music[-1]+1)%m)

def printmusic(music):
    for i in music:
        print(i, end=" ")
if good_samples_count < k:
    print(-1)
    sys.exit(1)
else if good_samples_count == k:
    music += [music[-1]+1] * (k-len(music))
    printmusic(music)
    
# 增加未达到数量要求的good sample
good_samples_needed = k-good_samples_count
music.append(music[good_samples_stopat-good_samples_needed-1])
