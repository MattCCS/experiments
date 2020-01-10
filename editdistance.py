SCALE = 40

D = {}
for l in range(SCALE + 1):
    for e in range(l):
        v = (e / l)
        D[(l, e)] = f"{v:.2f}"

for e in range(SCALE, -1, -1):
    row = [D.get((l, e), ' -- ') for l in range(SCALE + 1)]
    print(f"{e:>2} | " + " ".join(row))
print('   +' + '----' * SCALE)
print('      ' + "   ".join(f"{i:>2}" for i in range(SCALE + 1)))
