from math import atan2, sqrt, sin, cos, pi
import tkinter


def euclid_dist(x1, x2, y1, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)


def draw_arrow(startx, starty, endx, endy):
    theta = atan2(endx-startx, endy-starty)
    dist = euclid_dist(startx, endx, starty, endy)
    if dist < 30:
        return (False, False)
    else:
        rect = [startx+5*cos(pi/2-theta-pi/4), starty+5*sin(pi/2-theta-pi/4),
                startx+5*cos(pi/2-theta+pi/4), starty+5*sin(pi/2-theta+pi/4),
                startx+cos(pi/2-theta+pi/(4*((dist-30)/5)))*(dist-30),
                starty+sin(pi/2-theta+pi/(4*((dist-30)/5)))*(dist-30),
                startx+cos(pi/2-theta-pi/(4*((dist-30)/5)))*(dist-30),
                starty+sin(pi/2-theta-pi/(4*((dist-30)/5)))*(dist-30),
                ]
        triangle = [endx, endy,
                startx+cos(pi/2-theta+2*pi/(4*((dist-30)/5)))*(dist-30),
                starty+sin(pi/2-theta+2*pi/(4*((dist-30)/5)))*(dist-30),
                startx+cos(pi/2-theta-2*pi/(4*((dist-30)/5)))*(dist-30),
                starty+sin(pi/2-theta-2*pi/(4*((dist-30)/5)))*(dist-30)]

    return rect, triangle


if __name__ == '__main__':
    canvas = tkinter.Canvas(width=500, height=500)
    canvas.pack()
    angle = 0
    length = 70
    d_len = 10
    arrow = None

    def toc_sa():
        global angle, canvas, length, d_len, arrow
        if angle >= 2*pi:
            angle = 0
        if not(70<=length<=300):
            d_len *= -1
        canvas.delete('all')
        rect, triangle = draw_arrow(250, 250, 250+length*cos(angle), 250+length*sin(angle))
        canvas.create_polygon(*rect)
        canvas.create_polygon(*triangle)
        
        angle += 0.05
        length += d_len
        canvas.after(50, toc_sa)

    toc_sa()
    canvas.mainloop()
