import sys
sys.stdin = open("input_data", "r")


def start():
    inhabitants = int(input())
    while inhabitants != 0:
        consumption = [int(i) for i in input().split()]
        sum = 0
        cost = 0
        for i in range(0, len(consumption)):
            sum += consumption[i]
            cost += abs(sum)
        print(cost)
        inhabitants = int(input())


start()


