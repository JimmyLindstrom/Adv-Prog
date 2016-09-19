import sys
sys.stdin = open("input_data", "r")

def calculate_minimum_moves(number_of_stacks, set):
    stacks = input().split()
    bricks = 0
    for stack in stacks:
        bricks += int(stack)
    average_height = int(bricks / number_of_stacks)
    moves = 0
    for stack in stacks:
        if int(stack) < average_height:
            moves += int(average_height) - int(stack)
        elif int(stack) > average_height:
            moves += int(stack) - int(average_height)
    moves = int(moves /2)
    print("Set #" + str(set))
    print("The minimum number of moves is", str(moves) +".\n")

def start():
    number_of_stacks = int(input())
    set = 1
    while number_of_stacks != 0:
        calculate_minimum_moves(number_of_stacks, set)
        set += 1
        number_of_stacks = int(input())

start()