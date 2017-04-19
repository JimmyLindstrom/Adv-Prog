import sys
sys.stdin = open("input_data", "r")


def start():
    rows, cols = [int(i) for i in input().split(" ") if len(i) > 0]
    while True:
        matrix = [[0] * cols] * rows
        MAX_VALUE = 1000000000000
        # stores minimum weight for all pairs initialized to MAX_VALUE
        dist = [[MAX_VALUE] * cols] * rows
        # stores link to next element in minimum weight path initialized to -1
        next = [[-1] * cols] * rows
        # stores the different directions an edge has
        dir = {}
        row = 0
        col = 0
        count = 0
        # creating matrix of the input.
        while count < rows * cols:
            new_row = [int(i) for i in input().split(" ") if len(i) > 0]
            count_input = 0
            while count_input < len(new_row):
                matrix[row][col] = new_row[count_input]
                if col == cols - 1:
                    dist[row][col] = matrix[row][col]
                count += 1
                count_input += 1
                if not col < cols:
                    row +=1
                col = (col +1) % cols




        #
        # for i in range(0, rows):
        #     matrix.append([])
        #     dist.append([])
        #     next.append([])
        #     new_row = [int(i) for i in input().split()]
        #     try:
        #         for j in range(0, cols):
        #             matrix[i].append(new_row[j])
        #             next[i].append(-1)
        #             if j == cols - 1:
        #                 dist[i].append(matrix[i][j])
        #             else:
        #                 dist[i].append(MAX_VALUE)
        #     except IndexError:
        #         print("INDEX ERROR on rows: ", rows, "columns: ", cols )
        #         print(new_row)

        for line in matrix:
            print(line)

        for c in range(cols - 2, -1, -1):
            for r in range(0, rows):
                dir["up"] = rows - 1 if r == 0 else r - 1
                dir["down"] = (r + 1) % rows
                dir["right"] = c + 1

                min_weight = min(dist[dir["up"]][dir["right"]], dist[r][dir["right"]], dist[dir["down"]][dir["right"]])
                dist[r][c] = matrix[r][c] + min_weight

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



        # getting shortest path and distance
        start = 1000
        min_value = MAX_VALUE
        distance = 0
        for i in range(0, rows):
            if min_value > dist[i][0]:
                min_value = dist[i][0]
                start = i

        path = str(start + 1)
        try:
            distance = dist[start][0]
            next_col = next[start][0]
        except IndexError:
            print("index:", start, ",", i, "\n",
                  "rows, cols:", rows, ",", cols)
        for i in range(0, cols -1):
            # next_col = next[start][i]
            try:
                path += " " + str(next[next_col][i] + 1)
                next_col = next[next_col][i]
            except IndexError:
                print("index:" , next_col, ",", i+1, "\n",
                      "rows, cols:", rows, ",", cols)
        print(path)
        print(distance)


        break
        try:
            test = input()
            if test[-1:] == ' ':
                test = test[0:-1]
            rows, cols = [int(i) for i in test.split(" ") if len(i) > 0]
        except EOFError:
            break

start()
