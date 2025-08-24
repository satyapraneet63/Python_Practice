num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))

print('Before swap:', num1, num2)
num2= num2 + num1
num1= num2 - num1
num2= num2 - num1
print('after swap', num1, num2)