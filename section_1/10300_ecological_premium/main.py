import sys
sys.stdin = open("input_data", "r")

# calculate the premium. Animals not needed because we divide and then
# multliply with them. It evens out
def calculate_premium(farm_data):
    farm_size = int(farm_data[0])
    env_friendliness = int(farm_data[2])
    return int(farm_size * env_friendliness)


def sum_of_burden(farmers):
    sum = 0
    for farmer in range(farmers):
        farm_data = input().split()
        sum += calculate_premium(farm_data)
    return sum


def start():
    nbr_of_test_cases = int(input())
    for test in range(nbr_of_test_cases):
        nbr_of_farmers = int(input())
        print(sum_of_burden(nbr_of_farmers))

start()
