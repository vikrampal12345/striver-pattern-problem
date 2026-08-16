word1 = "abc"
word2 = "pqr"

# word1 = [i for i in word1]
# word2 = [i for i in word2]
# for i in range(0,len(word1),1):
#     word1.insert(i+1+i, word2[i])
    
# print("".join(word1))
lis = []
i = 0
while i < len(word1) and i < len(word2):
    lis.append(word1[i])
    lis.append(word2[i])
    i +=1

lis.extend(word1[i:])
lis.extend(word2[i:])    

print(lis)        

