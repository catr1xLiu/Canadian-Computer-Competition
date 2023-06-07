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
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
   
