i = 1
Sum = 0
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue

    Sum += i
    i +=1
print(Sum)