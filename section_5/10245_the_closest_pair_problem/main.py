import sys

sys.stdin = open("input_data", "r")

import math

MAX_VALUE = 10000


# class for points
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# returns distance between 2 points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) +
                     (p1.y - p2.y) * (p1.y - p2.y))


# Closest pair problem solved with sweepline-ish approach
def start():
    number_of_points = int(input())
    while True:
        # list for points
        points = []
        # creating all the points from the input
        for i in range(0, number_of_points):
            new_point = [float(i) for i in input().split(" ")]
            points.append(Point(new_point[0], new_point[1]))
        # sort points on x-coordinate
        points.sort(key=lambda point: point.x)
        # minimum distance stored in min initialized to 10000
        min = MAX_VALUE
        for i in range(0, number_of_points):
            for j in range(i + 1, number_of_points):
                # no need to check distance if distance between their x-value
                # is further then current minimum distance!
                if (points[i].x + min < points[j].x):
                    break

                distance = dist(points[i], points[j])
                if distance < min:
                    min = distance

        # print minimum or INFINITY if min >= 10000
        min = round(min, 4)
        if min < MAX_VALUE:
            print("%.4f" % min)
        else:
            print("INFINITY")

        number_of_points = int(input())
        if number_of_points == 0:
            break


start()
