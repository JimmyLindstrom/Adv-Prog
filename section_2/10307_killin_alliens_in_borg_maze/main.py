from queue import Queue
import sys
sys.stdin = open("input_data", "r")


# array for the different directions we can travel in the map
directions = [[-1,  0],
              [ 0, -1],
              [ 1,  0],
              [ 0,  1]]


def make_set(x, parents):
    parents[x].append(x)
    parents[x].append(0)


# ------- Union find Algorith ----------
def union(x, y, parents):
    x_root = find(x, parents)
    y_root = find(y, parents)

    if x_root == y_root:
        return

    if parents[x_root]["rank"] < parents[y_root]["rank"]:
        parents[x_root]["parent"] = y_root
    elif parents[x_root]["rank"] > parents[y_root]["rank"]:
        parents[y_root]["parent"] = x_root
    else:
        parents[y_root]["parent"] = x_root
        parents[x_root]["rank"] = parents[x_root]["rank"] + 1


def find(x, parents):
    if parents[x]["parent"] != x:
        parents[x]["parent"] = find(parents[x]["parent"], parents)
    return parents[x]["parent"]
# --------- Union find end --------------


# -------- Kruskals algorith ------------
# Kruskals algoritm for finding minimum spanning tree
def kruskal(G, nodes, parents):
    e = []
    for node in G:
        parents[node] = {"parent": node, "rank": 0} # the make_set operation !
        for edge in G[node]:
            e.append(edge)
    # for node in nodes:
    #     make_set(node, parents)
    X = []
    for edge in sorted(e, key=lambda e: e[2]):
        if find(edge[0], parents) != find(edge[1], parents):
            X.append(edge)
            union(edge[0], edge[1], parents)
    return X
# -------- Kruskals end--------------


# ----------- BFS --------------------
# nethod for traversing the graph and finding edges and their length
def breadth_first_search(map, starting_node, edges, bfs):
    node_queue = Queue(maxsize=0)
    node_queue.put(starting_node)
    edges[starting_node] = []
    # setting startnodes dist to 0 in bfs array
    bfs[starting_node[0]][starting_node[1]] = 0

    while node_queue.qsize() > 0:
        u = node_queue.get()
        x = u[0]
        y = u[1]
        for dir in directions:
            new_x = x + dir[0]
            new_y = y + dir[1]
            node_type = map[new_x][new_y]
            node = (new_x, new_y)

            if node_type == "#" or bfs[new_x][new_y] < 100 or node_type == "S":
                continue
            elif node_type == "A": # or node_type == "S":
                # if node_type == "S":
                #     continue
                    # bfs[new_x][new_y] = (bfs[x][y]) + 1
                    # node_queue.put((new_x, new_y))
                # if bfs[new_x][new_y] > (bfs[x][y]) + 1:
                bfs[new_x][new_y] = (bfs[x][y]) + 1
                # node_queue.put((new_x, new_y))
                edge = (starting_node, node, bfs[x][y] + 1)
                if not counter_edge_exists(edge, edges): # check for same edge the other way
                    edges[starting_node].append(edge)
            elif node_type == " ":
                bfs[new_x][new_y] = (bfs[x][y]) + 1
                node_queue.put(node)
# ------------BFS end -----------------


# function reseting distance values in bfs array
def reset_bfs_array(bfs):
    for i in range(0, len(bfs)):
        bfs[i] = [100] * len(bfs[i])


# method for checking if an edge already exists the other
# way som not to create it again
def counter_edge_exists(new_edge, edges):
    try:
        for edge in edges[new_edge[1]]:
            if edge == (new_edge[1], new_edge[0], new_edge[2]):
                return True
    except KeyError:
        return False

def start():
    # getting test cases
    test_cases = int(input())
    while test_cases > 0:
        x, y = [int(i) for i in input().split()]
        map = []
        # Bfs array holds the distances temporary
        bfs = []
        # dictionary for the edges, key is the node edges come from
        edges = {}
        nodes = []

        # building the map line by line and saving
        # aliens and startpoint as nodes
        for i in range(0, y):
            new_input = input()
            map.append([])
            bfs.append([])
            for j in range(0, len(new_input)):
                if new_input[j] == "S" or new_input[j] == "A":
                    node = (i, j)
                    nodes.append(node)
                map[i].append(new_input[j])
                bfs[i].append(100) # setting all distances to 100


        # for all nodes get the edges with distance
        for starting_node in nodes:
            breadth_first_search(map, starting_node, edges, bfs)
            reset_bfs_array(bfs)
        #
        # print("----- EDGES ------")
        # edge_count = 0
        for node in edges:
            print(node)
            for edge in edges[node]:
                # edge_count += 1
                print(edge)
        # print("AMOUNT OF EDGES!! ", edge_count)

        # Calculate MST and from MST the minimum distance
        # parents is dictionary to hold parents and rank value for union find algorithm
        parents = {}
        MST = kruskal(edges, nodes, parents)
        distance = 0
        for edge in MST:
            distance += edge[2]
        print(distance)

        test_cases -= 1


start()
