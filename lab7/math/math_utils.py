def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error Division by Zero is not allowed!"
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y

if __name__ == '__main__':
    print(add(2,3))
    print(sub(2,3))
    print(mul(2,3))
    print(div(2,3))
    print(mod(2,3))
    print(pow(2,3))
