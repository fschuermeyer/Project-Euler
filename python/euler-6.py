squares = range(0,101)
b = 0
c = 0

for i in squares:
    b += i*i
    c += i

print(c*c - b)