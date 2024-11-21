def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num*recur_factorial(num-1)
number = int(input("enter a number"))
if number<0:
    print("the number is less than 0")
elif number ==0:
    print("the factorial is 1")
else:
    print("the factorial of",number,"is",recur_factorial(number))

