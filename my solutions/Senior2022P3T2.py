import sys

n, m, k = map(int, input().split())

# to achieve maximum amount of good samples, we make the sequence like this:12341234
# this way, all the samples with length 0 < L <= m are all good
good_samples_max = 0
for L in range(1, m + 1):
    # there are n-L+1 samples with length L
    good_samples_max += n - L + 1
if k > good_samples_max or k < n:
    print(-1)
    sys.exit(0)
if k == n:
    print([1] * n)

'''
my idea to solve this problem, after seeing the commentaries
just decide on what to append to the tail every time, and make up the song note by note
there are n good samples at the start, since all samples with length 1 are good
as we append more and more notes to its tail, the amount of good samples changes, represented as s
we append a number that equals to the last number, s does not change, since all the newly added samples are bad
if we append a number that is different to all the last d numbers, than there will be an additional d-1 good samples


but before we start, we can generate a piece in the form of 1234123
with its length as big as possible, but do let the good samples within it exceed k 
this will reduce the time usage of the program
but we can't do this if k is smaller than the amount of good samples of a piece that goes 1234...m
all samples in 1234...m are good since all the notes are unique, so there are 1 + 2 + 3 + 4 + ... + m good samples 
'''

if m < n and (m+1)*m/2 < k and True:
    nums = [i for i in range(1, m+1)]
    amount_of_good_samples_needed = k-(m+1)*m/2
    pitch = 1
    for i in range(int(amount_of_good_samples_needed / m)):
        nums.append(pitch)
        pitch += 1
        if pitch > m:
            pitch = 1
    good_samples = int(amount_of_good_samples_needed / m) * m
    good_tail_length = m
    nums_max = m
else:
    nums = [1]  # the list that contains the current numbers
    good_samples = n  # the amount of good samples in the current numbers
    good_tail_length = 1  # the length of the longest tail without a repeating element
    nums_max = 1

while len(nums) <= n:
    if good_samples == k:
        nums += [nums[-1]] * (n - len(nums))
        break
    best_choice = 1
    best_choice_good_tail_length = 0
    for choice in range(1, min(nums_max + 1, m) + 1):
        good_tail_tmp = 1
        for j in range(good_tail_length):
            if choice == nums[-1 - j]:
                break
            good_tail_tmp += 1
        if good_tail_tmp - 1 + good_samples > k:
            continue
        if good_tail_tmp > best_choice_good_tail_length:
            best_choice_good_tail_length = good_tail_tmp
            best_choice = choice
    nums.append(best_choice)
    if best_choice > nums_max:
        nums_max = best_choice
    good_tail_length = best_choice_good_tail_length
    good_samples += good_tail_length-1
    print(len(nums), "/", n, good_tail_length)
print(nums)