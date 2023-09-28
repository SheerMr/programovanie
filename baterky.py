from collections import Counter

# solution = [set([int(y)-1 for y in x.split()]) for x in input().split(', ')]
n = 8
res = []


def solve(solution, comb=[]):
    global res
    if len(comb) == 4:
        res.append(comb)
        return
    if not comb:
        for i in range(n):
            solve(solution, [i])
    else:
        for i in range(comb[-1]+1, n):
            for pair in solution:
                if set(comb+[i]).issuperset(pair):
                    break
            else:
                solve(solution, comb+[i])

solution = [{0, 1}, {0, 2}]
solve(solution)
while res:
    c = Counter([tuple(k) for k in res])
    res = []
    solution.append(set([x[0] for x in c.most_common(1)]))
    print(solution)
    a = input()
    solve(solution)

print(solution)
