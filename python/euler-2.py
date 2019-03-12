one = 1
second = 2
count = 2
new = True


for i in range(100):
    if(new):
        new = False
        one = one + second
        item = one
    else: 
        new = True
        second = one + second
        item = second

    if item % 2 == 0 and count < 4000000:
        count += item

    
print(count)