class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self, step=0) -> str:
        string = f"node with value:{self.value}"
        if self.left is not None:
            string += f", left-brench:{self.left.__str__(step+1)}"
        if self.right is not None:
            string += f", right-brench:{self.right.__str__(step+1)}"
        return "\n" + "   "*step + "{\n}" + "   "*step + string + "\n" +  "   "*step + "}\n"
    
def create_btree(list_sorted):
    if len(list_sorted) == 1:
        return Node(list_sorted[0])
    if len(list_sorted) == 2:
        return Node(list_sorted[0], None, Node(list_sorted[1]))
    mid = (len(list_sorted)) // 2

    return Node(list_sorted[mid], create_btree(list_sorted[:mid]), create_btree(list_sorted[mid+1:]))

def add_node(tree:Node, newNode:Node, values_map):
    if values_map[newNode.value] > values_map[tree.value]:
        if tree.right is None:
            tree.right = newNode
        else:
            add_node(tree.right, newNode, values_map)
    elif values_map[newNode.value] < values_map[tree.value]:
        if tree.left is None:
            tree.left = newNode
        else:
            add_node(tree.left, newNode, values_map)

def find_path(tree:Node, value, values_map, path=[]):
    '''
    get the path, in a list
    0 means left, 1 means right
    -1 for unfound
    '''
    if value > values_map[tree.value]:
        if tree.right is None:
            return -1
        return find_path(tree.right, value, values_map, path=path + [1])
    if value < values_map[tree.value]:
        if tree.left is None:
            return -1
        return find_path(tree.left, value, values_map, path=path+[0])
    if tree.value == value:
        return path

def delete_node(tree:Node, path)->Node:
    # None if path invalid
    if path == -1 or len(path)==0:
        return None
    if len(path) == 1:
        if path[0]:
            swap = tree.right
            tree.right = None
            return swap
        swap = tree.left
        tree.left = None
        return swap
    
    if path[0]:
        return delete_node(tree.right, path[1:])
    return delete_node(tree.left, path[1:])
    
        

tree = create_btree([0,1,2,3,4,5])
values = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    3.5:3.5
}
print(tree)
print(delete_node(tree, find_path(tree, 2, values)))
print(tree)