n, m, k = map(input().split(), int)

# first, make the music have the most possible amount of good samples

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

# next, store all good samples in the form of (start,end), and sprt them by length 
# this way we know how much good_samples_count decreases each time we change a pitch to some different value
while good_samples_count != k:
     