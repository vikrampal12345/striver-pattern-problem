x = 121

if x < 0:
    x = str(x)
    a = x[0]
    b = x[::-1]
    c = a + b[:-1]
    print(c)
elif x > 0:    
    lis = []
    x = int(x)
    while x>0:
        digit = x % 10
        x //= 10
        lis.append(digit)
    num = "".join(str(x) for x in lis)
    if num[0] == '0':
        print(int(num[1:]))
    else:
        print(int(num))      

