################# 1 ##################

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

def writefactorial(x):
    if  x > 1:
        writefactorial(x - 1)
        print("*",end="")
    print(x, end="")

num = int(input("Which number do you want to calculate the factorial of?"))

print(f"Factorial calculation steps for {num}: ", end="")
writefactorial(num)
print(f"={factorial(num)}")

################# 2 ##################

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

def writefactorial(x):
    if  x > 1:
        writefactorial(x - 1)
        print("*",end="")
    print(x, end="")

num = int(input("Which number do you want to calculate the factorial of?"))

print(f"Factorial calculation steps for {num}: ", end="")
writefactorial(num)
print(f"={factorial(num)}")


sine_term = lambda n,x: ((-1)**n * x**(2*n+1)) / factorial(2*n+1)
pi = 3.141592653589793
def sine_x(x,n):
    x_rad = x*pi/180

    sine_value = 0

    for i in range(n):
        sine_value += sine_term(i,x_rad)

    return sine_value

x = float(input("Enter the value of x in degrees: "))
n = int(input("Enter the number of terms (n) to calculate: "))

result = sine_x(x, n)

print(f"Sine({x}°) using {n} terms of the series is: {result:.6f}")

################# 3 ##################

harmonicSum=0

def harmonic(n):

    global harmonicSum

    if n==0:
        return

    harmonic(n-1)

    if n==1:
        print("1",end="")
    else:
        print(f" + 1/{n}",end="")

    harmonicSum+=1/n

num=int(input("Enter number for the harmonic series:"))

harmonic(num)

print(f"={harmonicSum:.4f}")
