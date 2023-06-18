'''
请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。

请实现 Fancy 类 ：

Fancy() 初始化一个空序列对象。
void append(val) 将整数 val 添加在序列末尾。
void addAll(inc) 将所有序列中的现有数值都增加 inc 。
void multAll(m) 将序列中的所有现有数值都乘以整数 m 。
int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 109 + 7 取余。如果下标大于等于序列的长度，请返回 -1 。
 

示例：

输入：
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
输出：
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

解释：
Fancy fancy = new Fancy();
fancy.append(2);   // 奇妙序列：[2]
fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
fancy.append(7);   // 奇妙序列：[5, 7]
fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // 返回 10
fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10);  // 奇妙序列：[13, 17, 10]
fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // 返回 26
fancy.getIndex(1); // 返回 34
fancy.getIndex(2); // 返回 20
'''

class Fancy:
    '''
    思路：先存下所有加或乘的操作，每次操作叫一步。把append的原始数据存储下来，并存储他们是在哪一步被存下来的。
    对于任何一个加操作的加数adder，它最终加在一个数上的值等于adder * m1 * m2 * m3 * ...， 其中mi为这个加操作之后所有的乘操作的乘数
    而对于乘操作，我们可以将多次乘法操作合并，存储下他们取模后的积，当需要把原始输入乘以他后面乘法操作的值时，只需要把这些取模后的合并积乘起来，节省时间
    '''
    mod_base = 10e9 + 7
    raw_inputs = [] # in the form of [(num1,timeinserted), ....]
    operations = [] # in the form of [(0 for add, adder1), (1 for multiplication, factor 2)]
    combined_factors = [] # in the form of [[from, to, product(moded)], ...]
    
    def __init__(self):
        pass
    def append(self, val: int) -> None:
        self.raw_inputs.append((val, len(operations)))

    def addAll(self, inc: int) -> None:
        self.operations.append((0, inc))
    def multAll(self, m: int) -> None:
        self.operations.append((1,m))
    def getIndex(self, idx: int) -> int:



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)