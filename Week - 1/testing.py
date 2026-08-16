# lis = [1,3,4]
# newLis = str(lis)
# print(type(newLis))

# st = "rahul"
# st = st[1].replace('a', 'b')
# print(st)


def complement(num):
    lis = []
    
    while (num>0):
        digit = num%2
        num//=2
        lis.append(digit)

    lis.reverse()
    
    print(lis)
    new_lis = []
    for i in lis:
        if i == 0: 
            new_lis.append(1)
        elif i == 1:
            new_lis.append(0)
    print(new_lis) 

    
    new_lis.reverse()
    sum = 0
    for i in range(len(new_lis)):
        
        sum += new_lis[i]*(2**i)   
    print(new_lis)    
    print(sum)
print(complement(9))



# lis = [2,3,4,5]
# # lis.sort(reverse=True)
# print(sorted(lis, reverse=True))

# lis = [1,0]
# # lis = str(lis)
# new = "".join(str(i) for i in lis)
# print(new)
# new_lis = []
# for i in lis:
#     if i == 0: 
#         new_lis.append(1)
#     elif i == 1:
#         new_lis.append(0)
# print(new_lis)

lis = [1, 1,0]
lis.reverse()
sum = 0
for i in range(len(lis)):
    # print(i)
    sum += lis[i]*(2**i)

# print(len(lis))
print(sum)
print(lis)