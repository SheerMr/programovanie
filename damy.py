import tkinter

N = int(input())
res = []
SIZE = 666/N


def solve(row=0, queens=[]):
    global N, res
    if row == N:
        res.append(queens.copy())
        return
    for i in range(N):
        
        if i in queens:
            continue
        for j, queen in enumerate(queens):
            if abs(j-row) == abs(i-queen):
                break
        else:
            solve(row+1, queens.copy()+[i])


def draw(i=0):
    global res, queens, canvas
    for queen in queens:
        canvas.delete(queen)
    for x, y in enumerate(res[i]):
        queens.append(canvas.create_text((x+0.5)*SIZE, (y+0.5)*SIZE, text='Q', font=('Franklin Gothic Book', 12)))


def nexxt(lol):
    global i
    i += 1
    draw(i)


def prev(xd):
    global i
    i -= 1
    draw(i)
    

solve()

canvas = tkinter.Canvas(width=666, height=666)
canvas.pack()
for x in range(N):
    for y in range(N):
        if (x+y)%2 == 0:
            canvas.create_rectangle(x*SIZE, y*SIZE, (x+1)*SIZE, (y+1)*SIZE, fill='White')
        else:
            canvas.create_rectangle(x*SIZE, y*SIZE, (x+1)*SIZE, (y+1)*SIZE, fill='#b4e6a9')

i = 0
queens = []
if res:
    draw()
else:
    canvas.create_text(333, 333, text='NO SOLUTIONS', font=('Microsoft Uighur', 50))
canvas.bind_all('a', nexxt)
canvas.bind_all('b', prev)


canvas.mainloop()
