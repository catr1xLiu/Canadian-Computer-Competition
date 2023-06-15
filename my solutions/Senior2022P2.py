'''
Problem Description
A class has been divided into groups of three. This division into groups might violate two
types of constraints: some students must work together in the same group, and some students
must work in separate groups.
Your job is to determine how many of the constraints are violated.
Input Specification
The first line will contain an integer X with X ≥ 0. The next X lines will each consist of
two different names, separated by a single space. These two students must be in the same
group.
The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of
two different names, separated by a single space. These two students must not be in the
same group.
Among these X + Y lines representing constraints, each possible pair of students appears at
most once.
The next line will contain an integer G with G ≥ 1. The last G lines will each consist of
three different names, separated by single spaces. These three students have been placed in
the same group.
Each name will consist of between 1 and 10 uppercase letters. No two students will have
the same name and each name appearing in a constraint will appear in exactly one of the G
groups.
The following table shows how the available 15 marks are distributed at the Junior level.
Marks Awarded
Number of Groups
Number of Constraints
4 marks
G ≤ 50
X ≤ 50 and Y = 0
10 marks
G ≤ 50
X ≤ 50 and Y ≤ 50
1 mark
G ≤ 100 000
X ≤ 100 000 and Y ≤ 100 000
The following table shows how the available 15 marks are distributed at the Senior level.
Marks Awarded
Number of Groups
Number of Constraints
3 marks
G ≤ 50
X ≤ 50 and Y = 0
5 marks
G ≤ 50
X ≤ 50 and Y ≤ 50
7 marks
G ≤ 100 000
X ≤ 100 000 and Y ≤ 100 000
Output Specification
Output an integer between 0 and X +Y which is the number of constraints that are violated.
'''

x = int(input()) # the number of pairs that must be in a same group
pair_must_stick = [] # in the form of [(student1, student2),(student3,student4)]
for i in range(x):
    pair_must_stick.append(tuple(map(str, input().split())))

y = int(input()) # the number of pairs that must NOT be in a same group
pair_must_seperate = [] # in the form of [(student5, student6),(student7,student8)]
for i in range(y):
    pair_must_seperate.append(tuple(map(str, input().split())))

count = 0
g = int(input())
for i in range(g):
    group = list(map(str, input().split()))
    for j in range(x):
        if pair_must_stick[j][0] in group and (not pair_must_stick[j][1] in group):
            count += 1
    for j in range(y):
        if pair_must_seperate[j][0] in group and pair_must_seperate[j][1] in group:
            count += 1

print(count)