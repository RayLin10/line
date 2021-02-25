from display import *
import math

def draw_line(x0, y0, x1, y1, screen, color):

    if (x1 < x0):
        draw_line(x1, y1, x0, y0, screen, color)
        return 
    
    x, y = int(x0), int(y0)
    yDir = 1

    deltaY = y1 - y0
    deltaX = x1 - x0

    # Vertical and Horizontal Lines
    if deltaX == 0:
        for num in range(y, y1 + 1):
            plot(screen, color, x, num)
        return
    if deltaY == 0:
        for num in range(x, x1):
            plot(screen, color, num, y)
        return

    m = deltaY / deltaX

    if deltaY < 0:
        yDir = -1
     
    A = abs(deltaY)
    B = -deltaX
    A2 = 2 * A
    B2 = 2 * B

    # Quadrant 1, 5 and 4, 8
    if abs(m) <= 1:
        d = A2 + B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += yDir
                d += B2
            x += 1
            d += A2
    # Quadrant 2, 6 and 3, 7
    else:
        d = A + B2
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += A2
            y += yDir
            d += B2