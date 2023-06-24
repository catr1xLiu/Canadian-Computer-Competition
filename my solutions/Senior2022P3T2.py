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


before we start, we can generate a piece in the form of 1234123
with its length as big as possible, but do let the good samples within it exceed k 
this will reduce the time usage of the program
but we can't do this if k is smaller than the amount of good samples of a piece that goes 1234...m
all samples in 1234...m are good since all the notes are unique, so there are 1 + 2 + 3 + 4 + ... + m good samples 
'''


# before we start, we can generate a piece in the form of 1234123
# with its length as big as possible, but do let the good samples within it exceed k
# this will reduce the time usage of the program

nums = []  # the piece to be generated
good_samples = 0  # the amount of good samples in the current piece
pitch = 1  # the next pitch to add on the piece
while True:
    additional_good_samples = min(m, len(nums)+1)  # the increased good samples as a result of adding the next pitch, is all the samples who ends at the next pitch, with length from 1~m
    if good_samples + additional_good_samples > k:  # if the amount of good samples exceeds k
        break  # go to the next stage

    good_samples += additional_good_samples
    nums.append(pitch)  # add the pitch to the end of the piece
    pitch += 1
    if pitch > m:
        pitch = 1  # increase the pitch by one or bring it back down to 1, so the pitch goes 12345123...
good_tail_length = min(m, len(nums))  # the length of the longest tail sample (samples that end at the the end of the piece) that does not have repeating pitches
nums_max = max(nums)  # the highest pitch in the piece
print(good_samples)

while len(nums) <= n:
    if good_samples == k:  # if the amount of good samples needed is already achieved
        nums += [nums[-1]] * (n - len(nums))  # complete the piece by repeting the last pitch, this will not bring any more good samples
        break
    best_choice = 1  # find the best choice of the pitch to be appended to the piece
    best_choice_good_tail_length = 0  # the amount of good samples that the best choice will bring to us
    for choice in range(1, min(nums_max + 1, m) + 1):  # try all the pitches that can be played, except the ones that are too much higher than any other pitches, because there's no point
        good_tail_tmp = 1  # the length of the longest tail sample that does not have repeating pitches, after placing the choosen pitch
        for j in range(good_tail_length):  # go back to see the whole good tail
            if choice == nums[-1 - j]:
                break  # if the chosen pitch repeated, the new good tail ends here
            good_tail_tmp += 1  # otherwise, it's length increases by one each time
        if good_tail_tmp + good_samples > k:  # if the amount of good samples exceeds the required value
            continue  # this choice will not work
        if good_tail_tmp > best_choice_good_tail_length:  # if the current choice is better than the best choice
            best_choice_good_tail_length = good_tail_tmp
            best_choice = choice  # it becomes the best choice
    nums.append(best_choice)  # go for the best choice
    if best_choice > nums_max:
        nums_max = best_choice  # update the highest pitch
    good_tail_length = best_choice_good_tail_length  # update the length of the longest good tail
    good_samples += good_tail_length  # update the amount of the good samples
    print(len(nums), "/", n, good_tail_length)  # show the process of the work
print(nums)