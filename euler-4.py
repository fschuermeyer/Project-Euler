liste = []
for i in range(100,999):
    for b in range(100,999):
        x = b*i
        if str(x)[::-1] == str(x):
           liste.append(x)


print(sorted(liste)[-1])