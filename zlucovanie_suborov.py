
q1 = [int(x) for x in input().split()].sort()
q2 = []

cost = 0 
target = q2
source = q1
double = []
while len(q1) + len(q2) != 1:
    while len(double)< 2:
        if not q1:
            double.append(q2.pop(0))
        elif not q2:
            double.append(q1.pop(0))
        else:
            if q1[0] < q2[0]:
                double.append(q1.pop(0))
            else:
                double.append(q2.pop(0))
    if not source:
        pom = target
        target = source
        source = pom
    target.append(sum(double))
    cost += sum(double)
