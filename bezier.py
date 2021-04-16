import decimal

import matplotlib.pyplot as plt
import numpy


def bezier_curve_2d(t, points: list):
    degree = len(points) - 1
    if degree < 0:
        print(Warning("Unsufficient amount of points for bezier interpolation"))
        exit(-1)

    # Basically the point itself for the whole range of t values
    if degree == 0:
        return points[0]

    # Linear bezier interpolation
    if degree == 1:
        x = (1 - t) * points[0][0] + t * points[1][0]
        y = (1 - t) * points[0][1] + t * points[1][1]
        return x, y

    # Quadratic bezier interpolation
    if degree == 2:
        x = (1 - t) ** 2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t ** 2 * points[2][0]
        y = (1 - t) ** 2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t ** 2 * points[2][1]
        return x, y

    # Cubic interpolation
    if degree == 3:
        x = (1 - t) ** 3 * points[0][0] + 3 * (1 - t) ** 2 * t * points[1][0] + 3 * (1 - t) * t ** 2 * points[2][
            0] + t ** 3 * points[3][0]
        y = (1 - t) ** 3 * points[0][1] + 3 * (1 - t) ** 2 * t * points[1][1] + 3 * (1 - t) * t ** 2 * points[2][
            1] + t ** 3 * points[3][1]
        return x, y

    # TODO: Implement higher degrees of bezier interpolation
    if degree > 3:
        return NotImplemented


def drange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)


control_points = [[0, 0], [0.2, 0.8], [0.8, 0.2], [1, 1]]
x_points = []
y_points = []

for i in drange(0, 1, '0.001'):
    x, y = bezier_curve_2d(i, control_points)
    x_points.append(x)
    y_points.append(y)

x_points = numpy.array(x_points)
y_points = numpy.array(y_points)

plt.plot(x_points, y_points)

for point in control_points:
    plt.scatter(point[0], point[1])

plt.show()
