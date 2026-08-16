lis = [-1,0,1,2,-1,-4]
sum = 0
lis1 = []
for i in lis:
    sum = sum + i
    if sum == 0:
        lis1.append(i)
print(sum)        
