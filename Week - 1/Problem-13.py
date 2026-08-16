dic = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

rom = input("Enter the roman number: ")
sum = dic[rom[0]]
for i in range(1, len(rom)):
    sum += dic[rom[i]]
    if dic[rom[i]] > dic[rom[i-1]]:
        sum -= 2 * dic[rom[i-1]]
    





print(sum)        

# print(dic['I'])