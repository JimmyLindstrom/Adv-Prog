import sys
sys.stdin = open("input_data", "r")

# To ensure the numbers never grow to big we split the
# calculation to smaller parts and then add these parts
def calculate(B, P, M):
    if P == 0:
        return 1
    # to minimize the number of operations we square P
    z = calculate(B, P//2, M)
    if P % 2 == 0:
        return z**2 % M
    else:
        return B * z**2 % M


def start():
    while True:
        B = int(input())
        P = int(input())
        M = int(input())
        print(calculate(B, P, M))
        try:
            emtpy = input()
        except EOFError:
            break

start()
