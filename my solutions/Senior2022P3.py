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
(3, 2), (3, 2, 1), (2), (2, 1), (1).
Sample Input 3
5 5 50
Sample Output 3
-1
Explanation of Output for Sample Input 3
There are no pieces with 5 notes that can produce 50 different good samples.
'''
import sys
n,m,k = map(int,input().split())

# step 1, get the most good samples
# just go increasing lile 12345123, that gets you the most good samples
nums = []

i = 0
while len(nums) < n:
    nums.append(i += 1)
    if i > m:
        i = 1

# now, if our sequence nums has lenght n and highest pitch k, then all the samples with length k < x <= n are bad samples, and there are n-x+1 samples with legnth x
total_samples = (k+1) * k / 2
bad_samples = 0
for x in range(k+1, n+1):
    bad_samples += n-x+1

good_samples = total_samples - bad_samples
if good_samples < m:
    print(-1)
    sys.exit(0)

