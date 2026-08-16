n = int(input("Enter the number: "))
num = 0
lis = []
for i in range(0, n+1):
    if 3**i == n:
        num += i
# i = 0
# while 3**i <= n:
#     if 3**i ==n:
#         lis.append(i)
#     i +=i      

print(num)
print(lis)

if 3**num == n:
    print(True)
else:
    print(False)