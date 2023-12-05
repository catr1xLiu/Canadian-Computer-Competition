'''
Problem S3: Good Samples
Problem Description
You are composing music for the Cool Clarinet Competition (CCC). You have been instructed to make a piece of music with exactly N notes. A note is represented as a positive
integer, indicating the pitch of the note.
We call a non-empty sequence of consecutive notes in the piece a sample. For instance,
(3, 4, 2), (1, 2, 3, 4, 2) and (4) are samples of 1, 2, 3, 4, 2. Note that (1, 3) is not a sample of
1, 2, 3, 4, 2. We call two samples different if they start or end at a different position in the
piece.
We call a sample good if no two notes in the sample have the same pitch.
The clarinet players are picky in two ways. First, they will not play any note with pitch
higher than M. Second, they want a piece with exactly K good samples.
Can you construct a piece to satisfy the clarinet players?
Input Specification
The first and only line of input will contain 3 space-separated integers, N, M and K.
The following table shows how the available 15 marks are distributed.
Marks Awarded
Bounds on N
Bounds on M
Bounds on K
3 marks
1 ≤ N ≤ 16
M = 2
1 ≤ K ≤ 1 000
3 marks
1 ≤ N ≤ 106
M = 2
1 ≤ K ≤ 1018
4 marks
1 ≤ N ≤ 106
M = N
1 ≤ K ≤ 1018
5 marks
1 ≤ N ≤ 106
1 ≤ M ≤ N
1 ≤ K ≤ 1018
Output Specification
If there is a piece of music that satisfies the given constraints, output N integers between 1
and M, representing the pitches of the notes of the piece of music. If there is more than one
such piece of music, any such piece of music may be outputted.
Otherwise, output −1.
Sample Input 1
3 2 5
Sample Output 1
1 2 1
Explanation of Output for Sample Input 1
Notice that the piece is composed of N = 3 notes, each of which is one of M = 2 possible
pitches, 1 and 2. That piece of music has a total of 6 samples, but only K = 5 good samples:
(1), (1, 2), (2), (2, 1), (1). Notice that the two good samples of (1) are different since they
start at two different positions.
Note that the piece 2 1 2 is the only other valid output for this input.
One example of an output that would be incorrect is 3 2 3, since it has notes with pitches
larger than 2. Another incorrect output would be 1 1 2, since it only has four good samples:
(1), (1), (2) and (1, 2).
Sample Input 2
5 5 14
Sample Output 2
1 5 3 2 1
Explanation of Output for Sample Input 2
The 14 good samples are: (1), (1, 5), (1, 5, 3), (1, 5, 3, 2), (5), (5, 3), (5, 3, 2), (5, 3, 2, 1), (3),
(3, 2), (3, 2, 1), (2), (2, 1), (1).{}
Sample Input 3
5 5 50
Sample Output 3
-1
Explanation of Output for Sample Input 3
There are no pieces with 5 notes that can produce 50 different good samples.
'''
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
if k == good_samples_max:  # if it happens to be the right answer
    nums = []
    # generate a sequence like this:1234123
    i = 1
    while len(nums) < n:
        if i > k:
            i = 1
        nums.append(i)
        i += 1
    for i in nums:
        print(i, end=" ")
    sys.exit(0)

nums = [1 for i in range(n)]


def update_good_samples_count(nums, index, new_num, original_count):
    if nums[index] == new_num:
        return original_count
    ans = original_count
    # go through all the samples related to this number
    for L in range(2, len(nums) + 1):
        # imagine a window of length L sliding through the number, where i is the distance between the tail of the
        # current sample to the use a list to represent the amount of a pitch inside the sample and use it to
        # identify if there is a repetition
        pitches_amount = [0 for i in range(k)]  # pitches_amount[i-1] is the amount of pitch i in the current sample
        # find the initial value
        for pitch in nums[max(index - L + 1, 0):max(index - L + 1, 0) + L]:  # go through the starting sample
            pitches_amount[pitch - 1] += 1
        for i in range(0, L):
            window = (index + i - L + 1, index + i + 1)
            if window[0] < 0:
                continue
            if window[1] > len(nums):
                break
            sample_left = nums[window[0]:index]
            sample_right = nums[index + 1:window[1]]
            # print(nums[window[0]:window[1]], pitches_amount)

            # judge whether the amount of good samples increases or decreases
            if max(pitches_amount) == pitches_amount[nums[index] - 1] == 2 and pitches_amount[
                new_num - 1] == 0:  # if the updated element happens to be the only repetition is the sample, and it becomes non-repeating, ans will increase by 1
                ans += 1
            elif max(pitches_amount) == pitches_amount[
                new_num - 1] == 1:  # if the updated number becomes the first repetition
                ans -= 1

            # update the amount of each pitch
            if window[1] - window[0] == L:  # if the windows is not as
                pitches_amount[nums[window[0]] - 1] -= 1  # the left border disappears
            try:
                pitches_amount[nums[window[1]] - 1] += 1
            except IndexError:
                break
    return ans


good_samples_count = n  # all the samples with length 1 are always good
while good_samples_count != k:
    best_move = tuple()
    closest_distance = float("inf")
    greatest_pitch = max(nums)  # don't go to high,because there might be a really big k
    good_samples_count_tmp = 0
    for i in range(len(nums)):
        for j in range(nums[i], min(greatest_pitch + 1, m)+1):
            good_samples_count_tmp = update_good_samples_count(nums, i, j, good_samples_count)
            if abs(k - good_samples_count_tmp) < closest_distance:
                closest_distance = abs(k - good_samples_count_tmp)
                best_move = (i, j)
    good_samples_count = update_good_samples_count(nums, best_move[0], best_move[1], good_samples_count)
    nums[best_move[0]] = best_move[1]

for i in nums:
    print(i, end=" ")