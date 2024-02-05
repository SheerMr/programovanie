import tkinter, random
from math import pi, sin, cos
velocity_multiplier = 0.1


def colorgen(velocity):
    velocity /= 100 * velocity_multiplier
    blue = int(255 - 255 * velocity)
    red = int(510 * velocity)
    green = int(255 * velocity)
    return f'#{hex(red)}{hex(green)}{hex(blue)}'


def loop():
    global t, zrna, text
    if t == 1:
        t += 1
    elif t == 100:
        t -= 1
    else:
        t += random.randint(-1, 1)
    purge = []
    for i, zrno in enumerate(zrna):
        if zrno.move(t):
            purge.append(i)
            n -= 1
    purge = purge[::-1]
    for i in purge: zrna.pop(i)
    canvas.coords(text, text=n)
    canvas.after(5, loop)




class Zrno:

    def __init__(self):
        self.pos = [random.randint(0, 1000), random.randint(0, 800)]
        self.sprite = canvas.create_oval(self.pos[0] + 5, self.pos[1] + 5, self.pos[0] - 5, self.pos[1] - 5, fill='blue')

    def move(self, velocity):
        velocity *= velocity_multiplier  # Aby to vyzeralo smooooth
        angle = random.random() * 2 * pi
        self.pos[0] += velocity * cos(angle)
        self.pos[1] += velocity * sin(angle)
        canvas.coords(self.sprite, self.pos[0] + 5, self.pos[1] + 5, self.pos[0] - 5, self.pos[1] - 5, fill=colorgen(velocity))
        if not (0 <= self.pos[0] <= width) or not (0 <= self.pos[1] <= height):
            canvas.delete(self.sprite)
            return 1
        return 0


width = 1000
height = 800

canvas = tkinter.canvas(width=width, height=height)
canvas.pack()
n = 1000
t = 50
text = canvas.create_text(500, 25, text = n)

# Create stuff
zrna = []

for i in range(n):
    zrna.append(Zrno)

loop()

canvas.mainloop()
