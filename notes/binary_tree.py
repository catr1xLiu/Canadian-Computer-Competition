class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self, step=0) -> str:
        ## TODO work on string format
        string = f"node with value:{self.value}"
        if self.left is not None:
            string += f", left-brench:{self.left.__str__(step+1)}"
        if self.right is not None:
            string += f", right-brench:{self.right.__str__(step+1)}"
        return "\n" + "{\n" + "   "*step + string + "\n}"
    
def create_btree(list_sorted, left=0, right=-1):
    if right == -1:
        right = len(list_sorted)

    if right-left == 1:
        return Node(left)
    if right-left == 2:
        return Node(left, None, Node(right))
    mid = (left+right) // 2

    return Node(list_sorted[mid], create_btree(list_sorted, left, mid), create_btree(list_sorted, mid, right))

print(create_btree([0,1,2,3,4,5]))

