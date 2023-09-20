import random

N = int(input())
res = []


def solve(path=[(0, 0)]):
    global N, res
    if len(path) == N**2:
        res.append(path)
        return
    moves = []
    print(len(path))
    for x in find_moves(path[-1][0], path[-1][0], path):
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

solve()
print(res)
