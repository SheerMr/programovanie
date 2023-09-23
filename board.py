import tkinter
from time import sleep

class Chessboard:

    TRAVELTIME = 1
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
            
        x_speed = ((x-piece.x)*self.TILESIZE)/(Chessboard.FREQ*Chessboard.TRAVELTIME)
        y_speed = ((y-piece.y)*self.TILESIZE)/(Chessboard.FREQ*Chessboard.TRAVELTIME)
        for x in range(Chessboard.TRAVELTIME*Chessboard.FREQ):
            self.canvas.move(piece.sprite, x_speed, y_speed)
            board.canvas.update()
            sleep(1/Chessboard.FREQ)
            

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
        self.pointer = None
        self.board = board
        self.radius = board.TILESIZE/2 * 0.8
        self.sprite = board.canvas.create_oval((x+0.5)*board.TILESIZE-self.radius, (y+0.5)*board.TILESIZE-self.radius,
                                                     (x+0.5)*board.TILESIZE+self.radius, (y+0.5)*board.TILESIZE+self.radius, fill='blue')


if __name__ == "__main__":

    board = Chessboard(10)
    a = Piece(4, 3, board)
    board.move_piece(a, 8, 5)
    board.mainloop()
