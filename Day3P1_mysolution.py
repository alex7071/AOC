f = open('claims.txt', 'r')
content = [x for x in f.readlines()]
f.close()

claims = [[]]
for i in range(0, 1100):
    if i > 0:
        claims.append([])
    for j in range(0, 1100):
        claims[i].append(0)
for c in content:
    id = int(c.split('@')[0].split('#')[1].strip())
    left = int(c.split('@')[1].split(',')[0].strip()) - 1
    top = int(c.split(',')[1].split(':')[0].strip()) - 1
    width = int(c.split(':')[1].split('x')[0].strip())
    height = int(c.split('x')[1].strip())
    for i in range(left, left + width):
        for j in range(top, top + height):
            claims[i][j] = claims[i][j] + 1

inches = 0
for i in range(0, 1100):
    for j in range(0, 1100):
        if claims[i][j] > 1:
            inches += 1

print(inches)



