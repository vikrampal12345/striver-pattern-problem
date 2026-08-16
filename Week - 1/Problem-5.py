digits = [1,2,3]
sum= "".join(str(x) for x in digits)
sum = int(sum) + 1
lis = []
while sum > 0 :
    digit = sum % 10
    lis.append(digit)
    sum //= 10
lis.reverse()
print(lis)
print(sum)    