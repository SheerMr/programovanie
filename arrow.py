import tkinter
from math import atan2, sqrt, sin, cos

def draw_arrow(startx, endx, starty, endy):
    theta = atan2(endx, endy)
    if euclid_dist(startx, endx, starty, endy) < 30:
        return
    else:
        rect = [sin(theta)*(startx + 5)
            

def euclid_dist(x1, x2, y1, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)
