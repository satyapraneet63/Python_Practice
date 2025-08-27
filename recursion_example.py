def func_a(n):
    if n <= 0:
        return
    print("function A:", n)
    func_b(n-1)

def func_b(n):
    if n <= 0:
        return
    print("function B:", n)
    func_a(n-1)

func_a(int(input("enter an integer: ")))