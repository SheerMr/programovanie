import tkinter, time
from arrow import draw_arrow
from math import atan2, sin, cos


class Chessboard:

    TRAVELTIME = 1
    DIST = 5 # arbitrary units
    FREQ = 80

    def __init__(self, n) -> None:
        self.N = n
        self.canvas = tkinter.Canvas(width = 666, height = 666)
        self.TILESIZE = 666/n
        self.canvas.pack()
        self.marked = []
        self.marked_objects = []
        for x in range(n):
            for y in range(n):
                if (x+y) % 2 == 1:
                    self.canvas.create_rectangle(x*self.TILESIZE, y * self.TILESIZE, (x+1) * self.TILESIZE,
                                                  (y+1)*self.TILESIZE, fill='white')
                else:
                    self.canvas.create_rectangle(x*self.TILESIZE, y * self.TILESIZE, (x+1) * self.TILESIZE,
                                                  (y+1)*self.TILESIZE, fill='green')
        

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
            self.canvas.update()
            while piece.pointer:
                self.canvas.delete(piece.pointer.pop())
            time.sleep(1/Chessboard.FREQ)
        piece.x = x
        piece.y = y

    def mark_square(self, x, y):
        if (x, y) in self.marked:
            return False
        self.marked.append((x, y))
        left = None
        right = None
        iters = Chessboard.TRAVELTIME*Chessboard.FREQ//2
        for i in range(iters):
            time.sleep(0.5/Chessboard.FREQ)
            if left and right:
                self.canvas.delete(left)
                self.canvas.delete(right)
            left = self.canvas.create_line(x*self.TILESIZE, y*self.TILESIZE,
                                            (x+(i+1)/iters)*self.TILESIZE, (y+(i+1)/iters)*self.TILESIZE, width=5, tags='mark')
            right = self.canvas.create_line(x*self.TILESIZE, (y+1)*self.TILESIZE,
                                                (x+(i+1)/iters)*self.TILESIZE, (y+1-(i+1)/iters)*self.TILESIZE, width=5, tags='mark')
            self.canvas.update()
        self.marked_objects.append(left)
        self.marked_objects.append(right)


    def delete_marks(self):
        for x in self.marked_objects:
            self.canvas.delete('mark')
        self.marked_objects = []
        self.marked = []

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
