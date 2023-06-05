# solution for senior 2023 question 3
'''
Problem Description
Ryo and Kita are designing a new poster for Kessoku Band. After some furious brainstorming, they came to the conclusion that the poster should come in the form of a 2-D grid of lowercase English letters (i.e. a to z), with N rows and M columns.
Furthermore, it is known that Ryo and Kita both have peculiar tastes palindromes.  Ryo will only be satisfied with the poster if exactly R of its rows are palindromes, and Kita will only be satisfied with the poster if exactly C of its columns are palindromes.
Can you design a poster that will satisfy both Ryo and Kita, or determine that it is impossible to do so?
Note: A string is considered a palindrome if it is the same when read forwards and backwards. For example, kayak and bb are palindromes, whereas guitar and live are not.

Input Specification
The first and only line of input consists of 4 space-separated integers N, M, R, and C.

Output Specification
If it is impossible to design a poster that will satisfy both Ryo and Kita, output IMPOSSIBLE on a single line.
Otherwise, your output should contain N lines, each consisting of M lowercase English letters, representing your poster design. If there are multiple possible designs, output any of them.


Sample Input 1
4 5 1 2
Output for Sample Input 1
union
radar
badge
anime
Explanation of Output for Sample Input 1

In the given design, only the second row (namely radar) and the second and third columns (namely naan and iddi) are palindromes. Since exactly R = 1 of the rows and C = 2 of the columns are palindromes, this is an acceptable design.


Sample Input 2
2 2 2 1
Output for Sample Input 2
IMPOSSIBLE
Explanation of Output for Sample Input 2
In this case, it can be proven that it is impossible to satisfy both Ryo and Kita.

'''
from copy import deepcopy as cp
from os import system


class Grid:
    nums = []  # nums[row][colum]
    columns_asymmetry = []  # 1 for not symmetric
    rows_asymmetry = []

    def __init__(self, n, m):  # n and m is the number of rows and colums
        self.nums = [[0 for i in range(m)] for j in range(n)]
        self.columns_asymmetry = [0 for i in range(m)]
        self.rows_asymmetry = [0 for i in range(n)]

    def update(self, row, col, value):
        self.nums[row][col] = value
        row_asymmetry = 0
        for i in range(int(len(self.columns_asymmetry) / 2)):
            if self.nums[row][i] != self.nums[row][-1 - i]:
                row_asymmetry = 1
                break
        self.rows_asymmetry[row] = row_asymmetry

        col_asymmetry = 0
        for i in range(int(len(self.rows_asymmetry) / 2)):
            if self.nums[i][col] != self.nums[-1 - i][col]:
                col_asymmetry = 1
                break
        self.columns_asymmetry[col] = col_asymmetry

    def equals(self, grid):
        for i in range(len(self.rows_asymmetry)):
            for j in range(len(self.cols_asymmetry)):
                if grid.nums[i][j] != self.nums[i][j]:
                    return False
        return True

    def get_number_of_asymmetric_rows(self):
        result = 0
        for i in self.rows_asymmetry:
            result += i
        return result

    def get_number_of_asymmetric_columns(self):
        result = 0
        for i in self.columns_asymmetry:
            result += i
        return result

    def copy(self):
        copied_self = Grid(n, m)
        copied_self.nums = cp(self.nums)
        copied_self.rows_asymmetry = cp(self.rows_asymmetry)
        copied_self.columns_asymmetry = cp(self.columns_asymmetry)
        return copied_self

    def __str__(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        string = ""
        for i in range(len(self.rows_asymmetry)):
            for j in range(len(self.columns_asymmetry)):
                string += alphabet[self.nums[i][j]]
            string += "\n"
        return string


n, m, r, c = input().split()
n = int(n)
m = int(m)
r = n - int(r)
c = m - int(c)
grid = Grid(n, m)

ans = "IMPOSSIBLE"
found = False

path = set()


def dfs(grid: Grid):
    global found, ans
    if grid.get_number_of_asymmetric_rows() == r and grid.get_number_of_asymmetric_columns() == c:
        ans = grid
        found = True
        return

    if found:
        return

    # go through all the options we can do
    options_both_closing = []  # the options that can make the grid have both r and c closer to the targeted
    options_rows_closing = []  # the options that can make the amount of asymmetric rows approaching the objective quantity
    options_columns_closing = []  # the options for columns
    # TODO better sort all the options of best to worse in the order of how good it is leading to the required r and c
    for i in range(n):
        for j in range(m):
            option = grid.copy()
            if option.nums[i][j] + 1 >= 3:
                continue
            option.update(i, j, option.nums[i][j] + 1)
            if (option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_columns()) in path:
                continue
            path.add((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_columns()))
            rows_closing = (option.get_number_of_asymmetric_rows() - grid.get_number_of_asymmetric_rows()) * (
                    r - grid.get_number_of_asymmetric_rows()) > 0  # if we are moving in the right direction in the matter of the amount of asymmetric rpws required
            columns_closing = (option.get_number_of_asymmetric_columns() - grid.get_number_of_asymmetric_columns()) * (
                    c - grid.get_number_of_asymmetric_columns()) > 0  # in the matter of columns
            # print((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_columns(), rows_closing,
            # columns_closing))
            if rows_closing:
                if columns_closing:
                    options_both_closing.append(option)
                else:
                    options_rows_closing.append(option)
            elif columns_closing:
                options_columns_closing.append(option)

    for option in options_both_closing:
        dfs(option)
    for option in options_columns_closing:
        dfs(option)
    for option in options_rows_closing:
        dfs(option)


dfs(grid)
print(ans)

'''
answer from gpt

这是一个简单的构造题，可以使用贪心策略。我们需要构造一个 N * M 的矩阵，使得恰好有 R 行是回文串，且恰好有 C 列是回文串。

思路如下：

如果 R * C > N 或者 R * C > M，那么无论怎样构造都不可能满足条件，此时输出'IMPOSSIBLE'即可。

否则，我们可以将矩阵分为两个部分，第一部分是所有行和列的交叉点（即交点）所在的子矩阵，第二部分是剩余的部分，也就是除去第一部分的所有行或列组成的子矩阵，这部分的大小为 (N - R) * (M - C)。

我们先考虑如何构造第一部分。设 K = min(R, C)，那么我们可以将矩阵划分为 K 个子矩阵，每个子矩阵恰好含有一个回文行和一个回文列。具体地，我们可以让这个子矩阵的第 i 行和第 i 列是相同的回文串（比如说 aa）。对于其他的交点，我们可以随意填充 lowercase English letters 中的任何字母，以保证该交点不是一个回文点。

考虑到第一部分已经有了恰好 R 行和 C 列是回文串，为了满足要求，我们只需要在第二部分找到剩下的 R - K 行和 C - K 列，让它们各自是一个回文串即可。 如果此时无 SOLUTION，则输出'IMPOSSIBLE'。

时间复杂度为 O(NM)O(NM)。


n, m, r, c = map(int, input().split())
if r*c > n*m:
    print('IMPOSSIBLE')
else:
    # 构造第一部分子矩阵
    row = min(n, r)
    col = min(m, c)
    grid = [[''] * col for _ in range(row)]
    for i in range(min(row, col)):
        grid[i][i] = 'a'
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '':
                grid[i][j] = 'b'
    
    # 构造第二部分子矩阵
    for i in range(row, n):
        for j in range(m):
            grid[i][j] = 'c'
    for i in range(n):
        for j in range(col, m):
            if grid[i][j] == '':
                grid[i][j] = 'd'

    # 输出结果
    for i in range(n):
        print(''.join(grid[i]))
'''

''' answer chatgpt 

To solve this problem, we can follow these steps:

1. Read the input values for N, M, R, and C.
2. Check if it is possible to satisfy both Ryo and Kita's requirements:
   - If R and C are both greater than 1, or both less than or equal to 1, it is impossible to satisfy both requirements. In this case, print "IMPOSSIBLE" and return.
3. Create an empty grid of size N x M.
4. Fill the grid with lowercase English letters in any arbitrary way.
5. Iterate over each row in the grid and check if the row is a palindrome:
   - If the current row is not a palindrome and the number of palindromic rows found so far is less than R, make it a palindrome by reversing it.
6. Iterate over each column in the grid and check if the column is a palindrome:
   - If the current column is not a palindrome and the number of palindromic columns found so far is less than C, make it a palindrome by reversing it.
7. Print the final grid.

Here's the implementation of the above algorithm in Python:

```python
def create_palindrome_poster(N, M, R, C):
    if (R > 1 and C > 1) or (R <= 1 and C <= 1):
        print("IMPOSSIBLE")
        return

    # Create an empty grid
    grid = [['a'] * M for _ in range(N)]

    # Fill the grid with arbitrary letters
    for i in range(N):
        for j in range(M):
            grid[i][j] = chr(ord('a') + (i + j) % 26)

    # Check and modify rows to satisfy Ryo's requirement
    palindromic_rows = 0
    for i in range(N):
        if not is_palindrome(grid[i]) and palindromic_rows < R:
            grid[i] = grid[i][::-1]  # Reverse the row
            palindromic_rows += 1

    # Check and modify columns to satisfy Kita's requirement
    palindromic_columns = 0
    for j in range(M):
        column = [grid[i][j] for i in range(N)]
        if not is_palindrome(column) and palindromic_columns < C:
            for i in range(N):
                grid[i][j] = grid[i][j][::-1]  # Reverse the element in the column
            palindromic_columns += 1

    # Print the final grid
    for row in grid:
        print(''.join(row))


def is_palindrome(s):
    return s == s[::-1]


# Read input values
N, M, R, C = map(int, input().split())

# Create the palindrome poster
create_palindrome_poster(N, M, R, C)
```

You can now run the program and provide the input to get the desired output.
'''



''' second attempt: easier calculations to satisfy most test questions'''
n, m, r, c = map(int, input().split())
r = n-r # instead of counting about how many symmetric rows, we use the opposites, which are asymmetric rows for easier computation 
c = m-c

def solve(n, m, r, c):
    grid = [["a" for i in range(m)] for j in range(n)] # grid[row][column]
    if n == m == 0: # if the all the rows and columns are asked to be symmetric
        return grid

    # for most cases,simply crate a grid full of 'a' with side length m*n, and change the first r rows and c columns into 'b'day, so that r rows and c columns become asymmetric and the remaining rows and columns are still symmetric
    for i in range(r):
        for j in range(c):
            grid[i][j] = "b"
    if 0 < r < n and 0 < c < m:
        return grid
    
    # in the case where r is zero and c is nonzero
    grid = [["a" for i in range(m)] for j in range(n)]
    if c % 2: # all the rows are symetric, so the whole grid is horizontally symetric, so any odd number of asymtric columns are impossible
        return "IMPOSSIBLE"
    for i in range(c/2):
        grid[0][i] = grid[0][-1-i] = "b"
    if r == 0:
        return grid

    # in the case where c is zero and r is nonezero
    grid = [["a" for i in range(m)] for j in range(n)]
    if r % 2: # all the rows are symetric, so the whole grid is horizontally symetric, so any odd number of asymtric columns are impossible
        return "IMPOSSIBLE"
    for i in range(r/2):
        grid[i][0] = grid[-1-i][0] = "b"
    if c == 0:
        return grid

    # TODO write the code for the case where all rows or all columns are required to be symetric (based on what we have in the first condition, use "c"s to make more colums or lines asymetric)

