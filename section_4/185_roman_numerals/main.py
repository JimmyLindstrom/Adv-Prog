import sys
sys.stdin = open("input_data", "r")

import re
roman_numbers = []
arabic_sum = 0
digits = []
digits_dict = {}


# loopar för att få ut alla olika kombinationer på de 7 olika romerska tecknen
# eller så många som faktiskt förekommer i summan. provar värden från 0-9
def check_combinations():
    counter = 0
    for i1 in range(0, 10):
        digits_dict[digits[0]] = i1

        for i2 in range(0, 10):
            if i2 == i1:
                continue
            if 1 == len(digits):
                counter = check_arabic_sum(counter)
                if counter > 1:
                    return counter
                break
            digits_dict[digits[1]] = i2

            for i3 in range(0, 10):
                if i3 == i2 or i3 == i1:
                    continue
                if 2 == len(digits):
                    counter = check_arabic_sum(counter)
                    if counter > 1:
                        return counter
                    break
                digits_dict[digits[2]] = i3

                for i4 in range(0, 10):
                    if i4 == i3 or i4 == i2 or i4 == i1:
                        continue
                    if 3 == len(digits):
                        counter = check_arabic_sum(counter)
                        if counter > 1:
                            return counter
                        break
                    digits_dict[digits[3]] = i4

                    for i5 in range(0, 10):
                        if i5 == i4 or i5 == i3 or i5 == i2 or i5 == i1:
                            continue
                        if 4 == len(digits):
                            counter = check_arabic_sum(counter)
                            if counter > 1:
                                return counter
                            break
                        digits_dict[digits[4]] = i5

                        for i6 in range(0, 10):
                            if i6 == i5 or i6 == i4 or i6 == i3 or i6 == i2 or i6 == i1:
                                continue
                            if 5 == len(digits):
                                counter = check_arabic_sum(counter)
                                if counter > 1:
                                    return counter
                                break
                            digits_dict[digits[5]] = i6

                            for i7 in range(0, 10):
                                if i7 == i6 or i7 == i5 or i7 == i4 or i7 == i3 or i7 == i2 or i7 == i1:
                                    continue
                                if 6 == len(digits):
                                    counter = check_arabic_sum(counter)
                                    if counter > 1:
                                        return counter
                                    break
                                digits_dict[digits[6]] = i7
                                counter = check_arabic_sum(counter)
                                if counter > 1:
                                    return counter
    return counter


def check_arabic_sum(counter):
    numbers = ["", "", ""]
    index = -1
    for number in roman_numbers:
        index += 1
        for i in range(0,len(number)):
            if i == 0 and digits_dict[number[i]] == 0: # börjar det med 0 så returnera direkt
                return counter
            numbers[index] += str(digits_dict[number[i]])
    # print(numbers[0], "+", numbers[1], "=", numbers[2])
    if int(numbers[0]) + int(numbers[1]) == int(numbers[2]):
        # print("TEST")
        counter += 1
    return counter


def roman_to_arabic(roman_numbers):
    roman_values = {"M": 1000,
                    "D": 500,
                    "C": 100,
                    "L": 50,
                    "X": 10,
                    "V": 5,
                    "I": 1}

    numbers = [0, 0, 0]

    # översätt de romerska numrena till arabiska
    for i in range(0, len(roman_numbers)):
        for j in range(0, len(roman_numbers[i])):
            temp = roman_values[roman_numbers[i][j]]
            # om siffran med index j+1 är större än siffran med index j
            # så innebär det att den är negativ
            if j < len(roman_numbers[i]) - 1 and \
                            temp < roman_values[roman_numbers[i][j + 1]]:
                numbers[i] -= temp
            else:
                numbers[i] += temp

    return numbers


def start():
    case = input()
    while not case == "#":
        global roman_numbers
        # delar upp romarska summans tal till en lista med hjälp av
        # reguljära uttryck.
        roman_numbers = re.split('\W+', case)
        # kontrollerar om romerska summan är korrekt
        arabic_numbers = roman_to_arabic(roman_numbers)
        # skriv ut Correct alternativt Incorrect ifall summan stämmer eller ej
        if arabic_numbers[0] + arabic_numbers[1] == arabic_numbers[2]:
            print("Correct ", end="")
        else:
            print("Incorrect ", end="")
        # -----------------------------------------------------------------------

        # kontrollerar om den romerska summan kan tolkas som en arabisk summa
        # -----------------------------------------------------------------------
        # sparar alla distinkta tecken i romerska summan
        digits_dict.clear() # tecken som nyckel, tecknets värde som värde
        digits[:] = [] # endast för att ha index till de olika nycklarna i dictionaryn
        for num in roman_numbers:
            for char in num:
                if not char in digits_dict:
                    digits_dict[char] = -1
                    digits.append(char)

        arabic_sum = check_combinations()
        # skriver ut ifall det romerska talet kan tolkas som en arabisk summa
        if arabic_sum == 0:
            print("impossible")
        elif arabic_sum == 1:
            print("valid")
        elif arabic_sum > 1:
            print("ambiguous")
        # -------------------------------------------------------------------------
        case = input()
    

start()
