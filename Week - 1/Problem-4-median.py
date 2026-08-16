num1 = [1,3]
num2 = [3,4]
num3 = sorted(num1 + num2)
numl = len(num3)
sum1 = 0
while numl > 0:
    if numl % 2 != 0:
        sum1 += (numl + 1) / 2
    else:
        sum1 += ((numl/2) + ((numl/2) + 1))/2    

print(sum1)    