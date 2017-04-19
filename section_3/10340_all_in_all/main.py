import sys
sys.stdin = open("input_data", "r")


# decides wheter s is a subsequence of t
def s_is_subsequence_of_t(s, t):
    j = 0
    # count holds value of found matching characters
    count = 0
    # loop through t
    for i in range(0, len(t)):
        # if count equals the length of s we are done
        if count == len(s):
            break
        # if match found increment count with 1
        if t[i] == s[count]:
            count += 1
    # if count equals length of s we have a match and return "Yes"
    if count == len(s):
        return "Yes"
    # if not return "No"
    else:
        return "No"



def start():
    s, t = input().split()
    while True:
        print(s_is_subsequence_of_t(s, t))
        try:
            s, t = input().split()
        except EOFError:
            break

start()