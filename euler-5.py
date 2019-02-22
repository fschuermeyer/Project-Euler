k = False;
i = 80;
while True:
    for b in range(1,20):
        if (i/b).is_integer() is not True:
            k = True;
            break;

    if k is not True:
        print(i)
        break;
    else:
        k = False;
    i += 80

