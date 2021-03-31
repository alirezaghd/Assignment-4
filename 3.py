def multiplication():

    a = int(input())
    b = int(input())
    for i in range(a,b+1):
        for j in range(a,b+1):
            print(i * j,end=" ")
        print()

multiplication()