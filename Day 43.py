class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

n = int(input("Enter number of descriptions: "))

descriptions = []

for i in range(n):
    parent = int(input("Parent: "))
    child = int(input("Child: "))
    isLeft = int(input("Is Left (1/0): "))

    descriptions.append([parent, child, isLeft])

nodes = {}
children = set()

for parent, child, isLeft in descriptions:

    if parent not in nodes:
        nodes[parent] = TreeNode(parent)

    if child not in nodes:
        nodes[child] = TreeNode(child)

    if isLeft == 1:
        nodes[parent].left = nodes[child]
    else:
        nodes[parent].right = nodes[child]

    children.add(child)

for node in nodes:
    if node not in children:
        root = nodes[node]
        break

print("Root Node:", root.val)

Enter number of descriptions: 3

Parent: 1
Child: 2
Is Left (1/0): 1

Parent: 2
Child: 3
Is Left (1/0): 0

Parent: 3
Child: 4
Is Left (1/0): 1
Root Node: 1