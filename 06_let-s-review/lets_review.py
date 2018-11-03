t = eval(input())
while t:
    t -= 1
    y = []
    z = []
    x = str(input())
    for i in range(len(x)):
        if (not int(i)%2):
            y.append(x[i])
        else:
            z.append(x[i])
    print("".join(y) + " " + "".join(z))
