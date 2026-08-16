n = 5
lis = []
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print("")    


# print(lis)

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = lis[i-1][j-1] + lis[i-1][j]
    lis.append(row)

print(lis)