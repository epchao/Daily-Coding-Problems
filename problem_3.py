# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)


def serialize(root):
    if not root:
        return None

    serialized_tree_map = dict()
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    serialized_tree_map['val'] = root.val
    if serialized_left:
        serialized_tree_map['left'] = serialized_left
    if serialized_right:
        serialized_tree_map['right'] = serialized_right
    
    return json.dumps(serialized_tree_map)

def deserialize(s):
    serialized_tree_map = json.loads(s)

    node = Node(serialized_tree_map['val'])
    if 'left' in serialized_tree_map:
        node.left = deserialize(serialized_tree_map['left'])
    if 'right' in serialized_tree_map:
        node.right = deserialize(serialized_tree_map['right'])
    
    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
# testp
assert deserialize(serialize(node)).left.left.val == 'left.left'