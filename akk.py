n = eval(input())
a = [1,2]
for i in a:
    seq = a[-1]*2
    a.append(seq)
    if len(a) == n:
        print(a)
    else:
        continue

