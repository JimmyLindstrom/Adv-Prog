import sys
sys.stdin = open("input_data", "r")


def start():
    next_input = [int(i) for i in input().split(" ")]
    while next_input != [0, 0]:
        N = next_input[0]
        K = next_input[1]

        # creating 2d array for calculating with K +1 rows
        # and N+1 columns, to calculate using synamic programming
        numbers = []
        for i in range(0, 2):
            # if K is 1 there is always only 1 way to add up to N
            if i == 1:
                numbers.append([1] * (N + 1))
            # if K is 0 or greater than 1 initialize fields to 0
            else:
                numbers.append([0] * (N + 1))

        # loop all rows of numbers
        for k in range(2, K + 1):
            numbers.append([0] * (N + 1))
            # all columns of that row
            for n in range(0, N + 1):
                # numbers[k][n] is equal to sum of element[k][n-1] and element [k-1][n]
                numbers[k][n] = (numbers[k][n-1] + numbers[k - 1][n]) % 1000000

        print(numbers[K][N])
        next_input = [int(i) for i in input().split(" ")]

start()
