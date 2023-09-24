import tkinter
from time import sleep
from arrow import draw_arrow
from math import atan2, sin, cos


class Chessboard:

    TRAVELTIME = 10
    DIST = 5 # arbitrary units
    FREQ = 50

    def __init__(self, n) -> None:
        self.N = n
        self.canvas = tkinter.Canvas(width = 666, height = 666)
        self.TILESIZE = 666/n
        self.canvas.pack()
        for x in range(n):
            for y in range(n):
                if (x+y) % 2 == 1:
                    self.canvas.create_rectangle(x*self.TILESIZE, y * self.TILESIZE, (x+1) * self.TILESIZE, (y+1)*self.TILESIZE, fill='white')
                else:
                    self.canvas.create_rectangle(x*self.TILESIZE, y * self.TILESIZE, (x+1) * self.TILESIZE, (y+1)*self.TILESIZE, fill='#99ff73')
        

    def move_piece(self, piece, x , y):
        if piece.pointer:
            self.canvas.delete(piece.pointer)
        
        startx = piece.x*self.TILESIZE
        starty = piece.y*self.TILESIZE
        angle = atan2(x*self.TILESIZE-startx, y*self.TILESIZE-starty)
            
        x_speed = ((x-piece.x)*self.TILESIZE)/(Chessboard.FREQ*Chessboard.TRAVELTIME)
        y_speed = ((y-piece.y)*self.TILESIZE)/(Chessboard.FREQ*Chessboard.TRAVELTIME)
        for i in range(Chessboard.TRAVELTIME*Chessboard.FREQ):
            self.canvas.move(piece.sprite, x_speed, y_speed)
            rect, arrow = draw_arrow(startx+self.TILESIZE/2, starty+self.TILESIZE/2,
                                      startx+(i+1)*x_speed+self.TILESIZE/2, starty+(i+1)*y_speed+self.TILESIZE/2)
            if rect and arrow:
                piece.pointer.append(self.canvas.create_polygon(*rect))
                piece.pointer.append(self.canvas.create_polygon(*arrow))
            board.canvas.update()
            while piece.pointer:
                self.canvas.delete(piece.pointer.pop())
            sleep(1/Chessboard.FREQ)
        piece.x = x
        piece.y = y
            

    def mainloop(self):
        self.canvas.mainloop()

    def tp_piece(self, piece, x, y):
        piece.x = x
        piece.y = y
        self.canvas.coords(piece.sprite, (x+0.5)*self.TILESIZE-piece.radius, (y+0.5)*self.TILESIZE-piece.radius,
                            (x+0.5)*self.TILESIZE+piece.radius, (y+0.5)*self.TILESIZE+piece.radius)


class Piece:

    def __init__(self, x, y, board) -> None:
        self.x = x
        self.y = y
        self.pointer = []
        self.board = board
        self.radius = board.TILESIZE/2 * 0.8
        self.sprite = board.canvas.create_oval((x+0.5)*board.TILESIZE-self.radius, (y+0.5)*board.TILESIZE-self.radius,
                        (x+0.5)*board.TILESIZE+self.radius, (y+0.5)*board.TILESIZE+self.radius, fill='blue')


if __name__ == "__main__":

    board = Chessboard(10)
    a = Piece(4, 3, board)
    board.move_piece(a, 8, 5)
    board.mainloop()
