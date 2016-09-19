import sys
sys.stdin = open("input_data", "r")


# Checks the balance recursively
def check_balance():
    # read a line(mobile) to an array of ints
    mobile = [int(i) for i in input().split()]
    # Goes left in the mobile to a sub-mobile
    if mobile[0] == 0:
        mobile[0] = check_balance()
    # Goes right in the mobile to a sub-mobile
    if mobile[2] == 0:
        mobile[2] = check_balance()
    # Checking the balance of a mobile with no sub-mobiles.
    # if not balanced setting the global balanced variable
    # to false!
    if mobile[0] * mobile[1] != mobile[2] * mobile[3]:
        global balanced
        balanced = False
    # returning the combined weight of a submobile (WL + WR)
    return mobile[0] + mobile[2]


def start():
    test_cases = int(input())
    new_line = input()
    global balanced
    while test_cases > 0:
        if new_line == "":
            balanced = True
            check_balance()
            test_cases -= 1
            if balanced:
                if test_cases >= 1:
                    print("YES\n")
                else:
                    print("YES")
            else:
                if test_cases >= 1:
                    print("NO\n")
                else:
                    print("NO")
        try:
            new_line = input()
        except EOFError:
            break

start()