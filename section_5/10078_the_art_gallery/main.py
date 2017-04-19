import sys
sys.stdin = open("input_data", "r")


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_critical_point(points):
    turn_direction = ""

    for i in range(0, len(points)):
        # calculate index of neighbor point(next) and the neighbors neighbor(next_next)
        next = (i + 1) % len(points)
        next_next = (next + 1) % len(points)
        #
        u = (points[next].x - points[i].x, points[next].y - points[i].y)
        v = (points[next_next].x - points[next].x, points[next_next].y - points[next].y)
        cross_product = u[0] * v[1] - u[1] * v[0]
        # setting default turn direction on first three node
        if i == 0:
            if cross_product > 0:
                turn_direction = "left"
            elif cross_product < 0:
                turn_direction = "right"
        # if there are turns not following the default turn direction
        # then there are critical points
        if cross_product > 0 and turn_direction == "right" or \
                                cross_product < 0 and turn_direction == "left":
            return "Yes"
    # if all turns goes clockwise or all turns go counterclockwise no
    # critical points exist in the polygon
    return "No"


def start():
    new_input = input()
    while True:
        corners = int(new_input)
        new_input = input()

        # list for points
        points = []
        # creating all the points from the input
        for i in range(0, corners):
            new_point = [int(i) for i in new_input.split(" ")]
            points.append(Point(new_point[0], new_point[1]))
            new_input = input()

        print(check_critical_point(points))

        if new_input == '0':
            break


start()
