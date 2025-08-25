def makefib(length):
    fib = [0,1]
    if length <=2:
        print(fib[:length])
    else:
        for i in range(2,length):
            fib.append(fib[i-1] + fib[i-2])
    print(fib)

length = int(input("length of the sequence to be printed:"))
makefib(length)