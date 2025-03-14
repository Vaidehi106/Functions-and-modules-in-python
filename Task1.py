def factorial(n):
    product=1
    for i in range(1,n+1):
        product *= i
    return product

var=int(input("enter a number:"))

result=factorial(var)
print(result)
