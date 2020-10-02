def isPrime(x):
    c = 0

    for i in range(1,x + 1):
        if (x/i).is_integer():
            c += 1

    if c == 2:
        return True
    else:
        return False


step = 10001
x = 1
primes = []

while len(primes) < step:
    x = x + 1
    c = isPrime(x)

    if c:
        primes.append(x)

print(primes)
print(len(primes)) 