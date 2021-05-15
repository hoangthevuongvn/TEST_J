c=input()
def BinToDec(a):
    b=0
    for i in range(len(a)):
       b += int(a[len(a)-1-i])*pow(2,i)
    print(b)
BinToDec(c)