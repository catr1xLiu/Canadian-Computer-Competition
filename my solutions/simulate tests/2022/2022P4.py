import sys

n, m, k = map(int, input().split())

# 首先，我们让音乐（在符合nmk的要求下）有最多的good_samples
# 办法就是让音符一直递增，碰到k就归零，这样两个相同的音符之间的距离最远，他们中间形成的good_samples就越多

music = [1]
for i in range(n-1):
    music.append((music[-1]+1)%m)
    
#  this way, we have all samples with length below or equals m good samples
good_samples_count = 0
for piece_length in range(1,m+1):
    good_samples_count += (n-piece_length+1)

if good_samples_count < k:
    print(-1)
    sys.exit(1)

# 接下来，将所有good_samples存入一个列表
# 列表的第i项表示从第i个音符开始的samples中有x_i个good_samples
# 需要注意的是这同时也意味着，以音符i开头的samples中长度小于等于x_i的是good_samples，因为如果长度为x_i的sample是good sample， 那比他短而且也从i开始的sample都是good sample
good_samples_amounts = [min(k, n-i) for i in range(n)]
# this way we know how much good_samples_count decreases each time we change a pitch to some different value
# 思路：如果我们把k个音符变成12341234....然后1111（这里也可以2222或其他，就是要和最后一位不一样），那总good samples数 = 后面的1的数量+前面1234123的good samples数。 我们让数列一直1234123，直到good samples数超过要求，然后再弄掉几个good samples就好了
while good_samples_count != k:
    