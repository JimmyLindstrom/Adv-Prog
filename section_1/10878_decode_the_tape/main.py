import sys
sys.stdin = open("input_data", "r")

def start():
    new_line = input()
    new_line = input()
    message = ""
    while new_line:
        character = ""
        if new_line[0] == "|":
            for char in new_line:
                if char == "|" or char == ".":
                    continue
                elif char == "o":
                    character += "1"
                else:
                    character += "0"
            int_character = int(character, 2)
            message += chr(int_character)
            print(chr(int_character), end="")
        try:
            new_line = input()
        except EOFError:
            break

start()