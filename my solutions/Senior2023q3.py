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
  nums = [] # nums[row][colum]
  colums_asymmetry = [] # 1 for not symmetric
  rows_asymmetry = []
  def __init__(self, n, m): # n and m is the number of rows and colums
    self.nums = [[0 for i in range(m)] for j in range(n)]
    self.colums_asymmetry = [0 for i in range(m)]
    self.rows_asymmetry = [0 for i in range(n)]
    
  def update(self, row, col, value):
    self.nums[row][col] = value
    row_asymmetry = 0
    for i in range(int(len(self.colums_asymmetry)/2)):
      if self.nums[row][i] != self.nums[row][-1-i]:
        row_asymmetry = 1
        break
    self.rows_asymmetry[row] = row_asymmetry
    
    col_asymmetry = 0
    for i in range(int(len(self.rows_asymmetry)/2)):
      if self.nums[i][col] != self.nums[-1-i][col]:
        col_asymmetry = 1
        break
    self.colums_asymmetry[col] = col_asymmetry
    
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
  
  def get_number_of_asymmetric_colums(self):
    result = 0
    for i in self.colums_asymmetry:
      result += i
    return result
    
  def copy(self):
    copied_self = Grid(n, m)
    copied_self.nums = cp(self.nums)
    copied_self.rows_asymmetry = cp(self.rows_asymmetry)
    copied_self.colums_asymmetry = cp(self.colums_asymmetry)
    return copied_self
    
  def __str__(self):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in range(len(self.rows_asymmetry)):
      for j in range(len(self.colums_asymmetry)):
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
def dfs(grid:Grid):
  global found, ans
  if grid.get_number_of_asymmetric_rows() == r and grid.get_number_of_asymmetric_colums() == c:
    ans = grid
    found = True
    return
  
  if found:
    return
  
  # go through all the options we can do
  options_both_closing = [] # the options that can make the grid have both r and c closer to the targeted
  options_rows_closing = [] # the options that can make the amount of asymmetric rows approaching the objective quantity
  options_colums_closing = [] # the options for colums
  # TODO better sort all the options of best to worse in the order of how good it is leading to the required r and c
  for i in range(n):
    for j in range(m):
      option = grid.copy()
      if option.nums[i][j] + 1 >= 2:
        continue
      option.update(i, j, option.nums[i][j] + 1)
      if (option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums()) in path:
        continue
      path.add((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums()))
      rows_closing = (option.get_number_of_asymmetric_rows() - grid.get_number_of_asymmetric_rows()) * (r - grid.get_number_of_asymmetric_rows()) > 0 # if we are moving in the right direction in the matter of the amount of asymmetric rpws required
      colums_closing = (option.get_number_of_asymmetric_colums() - grid.get_number_of_asymmetric_colums()) * (c - grid.get_number_of_asymmetric_colums()) > 0 # in the matter of colums
      # print((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums(), rows_closing, colums_closing))
      if rows_closing:
        if colums_closing:
          options_both_closing.append(option)
        else:
          options_rows_closing.append(option)
      elif colums_closing:
        options_colums_closing.append(option)
  
  for option in options_both_closing:
    dfs(option)
  for option in options_colums_closing:
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
