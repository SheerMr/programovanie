from board import Chessboard, Piece
import multiprocessing


N = int(input())
res = []


def solve(path=[(0, 0)]):
    global N, res
    if len(path) == N**2:
        res.append(path)
        return
    moves = []
    for x in find_moves(path[-1][0], path[-1][1], path):
        moves.append((find_moves(x[0], x[1], path+[(x[0], x[1])]), path+[(x[0], x[1])]))
    moves = sorted(moves, key=lambda x: len(x[0]))
    for move in moves:
        solve(move[1])


def find_moves(x, y, path):
    global N
    out = []
    cycle = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for i in cycle:
        if is_legal(x+i[0], y+i[1], path):
            out.append((x+i[0], y+i[1]))
    return out


def is_legal(x, y, path):
    global N
    if (x, y) not in path and 0 <= x < N and 0 <= y < N:
        return True
    return False


def prev(stuff):
    global curren, drawing
    current -=1
    drawing.terminate()
    show_solution()


def next(stuff):
    global current, drawing
    current += 1
    drawing.terminate()
    show_solution()


def show_solution():
    global current, board, knight, thread
    board.delete_marks()
    board.tp_piece(knight, res[current][0][0], res[current][0][1])
    for move in res[current]:
        board.move_piece(knight, move[0], move[1])
        board.mark_square(move[0], move[1])


current = 0
solve()
board = Chessboard(N)
knight = Piece(0, 0, board)
board.canvas.bind_all('d', next)
board.canvas.bind_all('a', prev)
show_solution()
board.mainloop()
