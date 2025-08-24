def makearray(length):
    array = []
    print('enter', length, 'numbers:')
    for i in range(0, length):
        num = int(input())
        array.append(num)
    return array
    print(array)

def avg_func(array):
    avg = 0
    total = 0
    for i in range(0, len(array)):
        total = total+array[i]
    avg = total/len(array)
    print("average is", avg)

length = int(input("enter number of numbers to take average of:"))
makearray(length)
avg_func()