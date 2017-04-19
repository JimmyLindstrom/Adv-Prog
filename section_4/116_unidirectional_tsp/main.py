import sys
sys.stdin = open("input_data", "r")


def start():
    rows, cols = [int(i) for i in input().split(" ") if len(i) > 0]
    while True:
        matrix = [[]]
        MAX_VALUE = 1000000000000
        # stores minimum weight for all pairs
        dist = [[]]
        # stores link to next element in minimum weight path
        next = [[]]
        # stores the 3 directions you can move from a node to its neighbor
        dir = {}

        # creating matrix from the input.
        row, col, count = 0, 0, 0
        while count < rows * cols:
            new_row = [int(i) for i in input().split(" ") if len(i) > 0]
            count_input = 0
            while count_input < len(new_row):
                matrix[row].append(new_row[count_input])
                dist[row].append(MAX_VALUE)
                next[row].append(-1)
                # matrix[row][col] = new_row[count_input]
                if col == cols - 1:
                    dist[row][col] = matrix[row][col]
                    row += 1
                    if row < rows:
                        matrix.append([])
                        dist.append([])
                        next.append([])
                count += 1
                count_input += 1
                col = (col + 1) % cols

        # updating the dist array with minimum distances
        for c in range(cols - 2, -1, -1):
            for r in range(0, rows):
                dir["up"] = rows - 1 if r == 0 else r - 1
                dir["down"] = (r + 1) % rows
                dir["right"] = c + 1

                min_weight = min(dist[dir["up"]][dir["right"]], dist[r][dir["right"]], dist[dir["down"]][dir["right"]])
                dist[r][c] = matrix[r][c] + min_weight

                # uppdating next array with column index to its "closest" neighbor
                next[r][c] = MAX_VALUE
                rows_to_try = [dir["up"], r, dir["down"]]
                # sorts the rows_to_try so we can pick the one with minimum weight AND
                # minimum index.
                rows_to_try.sort()
                for row_to_try in rows_to_try:
                    if next[r][c] == MAX_VALUE or \
                            (dist[row_to_try][dir["right"]] == min_weight and
                                 dist[row_to_try][dir["right"]] < dist[next[r][c]][dir["right"]]):
                        next[r][c] = row_to_try


        # getting shortest path and total distance
        start = 1000
        min_value = MAX_VALUE
        for i in range(0, rows):
            if min_value > dist[i][0]:
                min_value = dist[i][0]
                start = i

        path = str(start + 1)
        distance = dist[start][0]
        for i in range(0, cols -1):
            path += " " + str(next[start][i] + 1)
            start = next[start][i]

        print(path)
        print(distance)


        try:
            rows, cols = [int(i) for i in input().split(" ") if len(i) > 0]
        except EOFError:
            break

start()
