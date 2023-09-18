import random

N = int(input())
res = []


def solve(path=[random.randint(0, N-1), random.randint(0, N-1)]):
    global N, res
    if len(path) == N**2:
        res.append(path)
        return
    moves = []
    for x in find_moves(path[-1][0], path[-1][0], path):
        moves.append(x, find_moves(x[0], x[1], path+[(x[0], x[1])]))
    # TODO usortovat, move na najmensiu, a potom daco ig
    moves = sorted(moves, key=lambda x: len(x[0]))
    for move in moves:
        solve()

def find_moves(x, y, path):
    global N
    out = []
    cycle = [2, 1, -1, -2]
    for i in cycle:
        if is_legal(x+i, y+3-abs(i), path):
            out.append((x+i, y+3-abs(i)))
        if is_legal(x+i, y-(3-abs(i)), path):
            out.append((x+i, y-3+abs(i)))
    return out


def is_legal(x, y, path):
    global N
    if (x, y) not in path and 0 <= x < N and 0 <= y < N:
        return True
    return False
