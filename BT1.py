
b = int(input())
def fib(n):
    f0=1
    f1=1
    fn=1
    if n==0:
        print(f0)
    elif n==1:
        f1=1
        print(f1)
    elif n<0:
        print(0)
    else:
        print(0)
        print(1)
        print(1)
        for i in range(2,n-1):
            f0=f1
            f1=fn
            fn=f0+f1
            print(fn)
fib(b)