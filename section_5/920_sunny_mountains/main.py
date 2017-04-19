import sys
sys.stdin = open("input_data", "r")

import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def start():
    cases = int(input())
    while cases > 0:
        # list for points
        points = []
        N = int(input())
        # creating all the points from the inputpoints
        for i in range(0, N):
            new_point = [int(i) for i in input().split()]
            points.append(Point(new_point[0], new_point[1]))
        # sorting all the points on x-coordinate descending
        points.sort(key=lambda point: point.x, reverse=True)
        # variables for highest piont and length of sunny parts
        highest_point, sun = 0, 0
        # Loop through all points stating from second one comparing with
        # the previous point
        for i in range(1, len(points)):
            # check if point is higher than highest point and the previous point
            if points[i].y > highest_point and points[i].y > points[i - 1].y:
                # vector coordinates(dx, dy)
                dx = points[i].x - points[i - 1].x
                dy = points[i].y - points[i - 1].y
                # calculate length of line(magnitude)
                magnitude = math.sqrt(dx**2 + dy**2)
                # calculate the y-value that is in the sun
                sunny_part = points[i].y - highest_point
                # calculate length of the sunny part of the mountain
                sun += sunny_part * magnitude / dy
            # update the highest point reached so far
            highest_point = max(points[i].y, highest_point)
        # print result with 2 decimals
        print("%.2f" % sun)
        cases -= 1

start()
