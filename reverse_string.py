def reverse(string):
    gnirts=""
    for i in string:
        gnirts= i + gnirts
    return gnirts

string = input("enter whatever you want:")

print("The reverse of", string, "is", reverse(string))