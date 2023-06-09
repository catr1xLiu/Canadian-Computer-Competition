'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符

'*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 

示例 1：

输入：s = "aa", p = "a"

输出：false

解释："a" 无法匹配 "aa" 整个字符串。

示例 2:

输入：s = "aa", p = "a*"

输出：true

解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：

输入：s = "ab", p = ".*"

输出：true

解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
'''

'''
My solution:
dots can represent any amount of the element before it,
so if we set diff = len(s) - len(p) - (the amount of *),
the total elements that * represents will be diff, and for countable amount of *, there is countable amount of ways to allocate these elements
we just need to try all of these ways and see if there is one way that can match
'''

from copy import deepcopy as cp

class Solution:
    ans = False
    def isMatch(self, s: str, p: str) -> bool:
        stars_count = 0
        for i in p:
            stars_count += int(i=="*")
        amount_of_elements_by_star = len(s) - (len(p) - stars_count)
        
        def equals(s, p):
            if len(s) != len(p):
                return False
            for i in range(len(s)):
                if s[i] == p[i] or p[i] == ".":
                    continue
                return False
            return True
        
        if equals(s, p):
            return True

        separated_list = p.split("*")
        if separated_list[-1] == "":
            separated_list.pop(-1)
        def combine(elements_by_star_list) -> str:
            string = ""
            for i in range(len(elements_by_star_list)):
                string += separated_list[i-1] + separated_list[i-1][-1] * elements_by_star_list[i] # repeat the last element
            return string

        def dfs(star_num=0, elements_by_star_list:list=[]):
            if star_num == stars_count:
                attempt = combine(elements_by_star_list)
                if p[-1] != ".": # there will be one more part to connect
                    attempt += separated_list[-1]
                self.ans = equals(s, attempt) or self.ans
                return

            for elements_by_current in range(amount_of_elements_by_star - sum(elements_by_star_list)):
                string = combine(cp(elements_by_star_list) + [elements_by_current])
                if equals(s[0:len(string)], string):
                    dfs(star_num +1, cp(elements_by_star_list) + [elements_by_current])
        dfs()
        return self.ans

solution = Solution()
print(solution.isMatch("ab", ".*"))