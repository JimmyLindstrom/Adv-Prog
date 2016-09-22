import sys
sys.stdin = open("input_data", "r")


# decides wheter s is a subsequence of t if by removing characters
# from t you can end up with s
def s_is_subsequence_of_t(s, t):
    j = 0
    # if both strings are same length you can't remove any characters
    if len(s) == len(t):
        return("No")
    # loop through characters in s
    for i in range(0, len(s)):
        # loop through caracters in t
        while j < len(t):
            # if matching character
            if s[i] == t[j]:
                # if you are at the last letter in s then you have a
                # complete match return Yes
                if i == len(s) - 1:
                    return("Yes")
                # if not at last letter in s check, next letter in s
                else:
                    j += 1
                    break
            # if not a matching letter and you have to few letters
            # left in t to be able to get a match, stop the search
            # by returning No
            elif j > len(t) - 1 - i :
                return("No")
            j += 1

def start():
    s, t = input().split()
    while True:
        print(s_is_subsequence_of_t(s, t))
        try:
            s, t = input().split()
        except EOFError:
            break

start()


