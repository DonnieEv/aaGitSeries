
for i in range(1,16):
    row = []
    for j in range(1, i+1):
        if j % 3 == 0 and j % 5==0:
            row.append("FizzBuzz")
        elif j % 3 == 0:
            row.append("Fizz")
        elif j % 5 == 0:
            row.append("Buzz")
        else:
            row.append(str(j))
    print(" ".join(row))

