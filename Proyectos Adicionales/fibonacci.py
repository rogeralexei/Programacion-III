def fibonacci(n):
    a=0
    b=1
    while a+b<=n:
        print(a+b)
        a,b=b,a+b


if __name__=="__main__":
    fibonacci(100)