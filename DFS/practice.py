def factorial(x):
    if(x==1):
        return 1
    return x*factorial(x-1)

def factorial2(x):
    result = 1
    for i in range(1,x+1):
        result = result*i

    return result


print(factorial(5))