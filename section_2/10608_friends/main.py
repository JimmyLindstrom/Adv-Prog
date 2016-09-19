import sys
sys.stdin = open("input_data", "r")


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


def start():
    # getting test cases
    test_cases = int(input())
    # looping test_cases times
    while test_cases > 0:
        # reading N = citizens, M = couples
        N, M = [int(i) for i in input().split()]
        # creating an N-size array, to store all sets in,
        # with -1 as values. Negative values means they are root
        # nodes in the set and how many nodes that are in the set.
        # Positive value point to the element that is the root of
        # the set it is in.
        citizens = [-1] * N
        for i in range(0, M):
            x, y = [int(i) for i in input().split()]
            # merge to a previous or new set.
            union(x - 1, y - 1, citizens)
        # variable for largest group
        biggest_group = 0
        # loop through the citizens array and finding
        # the number that is the smallest as it is negative
        # for the roots of the sets
        for i in citizens:
            if i < biggest_group:
                biggest_group = i
        # if the biggest set found is -1 then there are no sets
        # with more than one node, so no groups then print 0
        if biggest_group == -1:
            print(0)
        # print the set in positive
        else:
            print(-biggest_group)
        test_cases -= 1


start()
