n = int(input("enter your index: "))
while n < 0:
    print("Please enter a number >=0")
    n = int(input("enter a proper index this time: "))
result = (n*(n+1))//2
print("sum to the given index is: ", result)