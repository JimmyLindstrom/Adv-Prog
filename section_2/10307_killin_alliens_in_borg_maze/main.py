import sys
sys.stdin = open("input_data", "r")


class Node:
    'Common base class for all Nodes'
    empCount = 0

    def __init__(self, x, y, weight, alien):
        self.x = x
        self.y = y
        self.visited = False
        self.alien = alien
        self.weight = weight
        Node.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Node.empCount

    def displayNode(self):
        print("X : ", self.x, ", Y: ", self.y,
               ", weight: ", self.weight, ", visited:  ",
              self.visited, ", alien: ", self.alien)



def start():
    # getting test cases
    test_cases = int(input())
    # looping test_cases times
    x, y = [int(i) for i in input().split()]
    start_Node = None
    map = []
    for i in range(0, y):
        map.append([])
        new_input = input().split()
        for j in range(0, x):
            if new_input[j] == "S":
                node = Node(i, j, 0, False)
                start_Node = node
            elif new_input[j] == "A":
                node = Node(i, j, 0, True)
            elif new_input[j] == "#":
                node = Node(i, j, 0, False)
            else:
                node = Node(i, j, 0, False)
            map[i].append(node)
            node.displayNode()

    while test_cases > 0:
        test_cases -= 1


start()



# merge two nodes, w and y, to a set in the citizens array
def union(x, y, citizens):
    # fins the nodes roots
    x_root = find(x, citizens)
    y_root = find(y, citizens)
    # If they have same root they are already in same set
    if x_root == y_root:
        return
    # if they are not in the same set merge the smaller set with
    # the bigger, by increasing the bigger set with the smaller sets
    # size, and set parent node in smaller set = parent node of bigger
    # set
    if citizens[x_root] > citizens[y_root]:
        citizens[y_root] += citizens[x_root]
        citizens[x_root] = y_root
    elif citizens[x_root] < citizens[y_root]:
        citizens[x_root] += citizens[y_root]
        citizens[y_root] = x_root
    # if the sets are equaly big join y_root with x_root
    else:
        citizens[x_root] += citizens[y_root]
        citizens[y_root] = x_root


# find the root_node of a set, and sets the root_node as parent for all
# the nodes in the set
def find(x, citizens):
    # if it is not already a root node
    if citizens[x] >= 0:
        # goto the nodes parent-node
        citizens[x] = find(citizens[x], citizens)
    # if it is a root node return the index
    if citizens[x] < 0:
        return x
    # if it is not a root node return the roots parent index
    else:
        return citizens[x]

