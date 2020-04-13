def as_string():
    a=input()
    print(a[::-1])
def as_num():
    a=int(input())
    b=0
    while a>0:
        b*=10
        b+=a%10
        a//=10
    print (b)

as_num()
