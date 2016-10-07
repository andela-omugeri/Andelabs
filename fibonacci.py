firstNum = 0
lastNum = int(raw_input("Enter the last number:"))


def Fib(n):
    if n<2:
        return n
    else:
        return Fib(n-1) + Fib(n-2)

print map(Fib, range(firstNum, lastNum))