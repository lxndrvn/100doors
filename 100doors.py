def doors (n):
    doors = [False] * n

    for i in range(n):
        for j in range(i, 100, i+1):
            doors[j] = not doors[j]

    print("The following doors are open:")
    open_doors = []
    for k, door in enumerate(doors, start=1):
        if door == True:
           open_doors.append(str(k))
    print(','.join(open_doors))

doors(100)