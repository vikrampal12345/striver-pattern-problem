num = int(input("Enter the number: "))
perfect = 0
for i in range(num):
    if i*i == num:
        perfect +=i
        break
print(perfect)
if num == 1:
    print(True)
elif perfect* perfect == num:
    print(True)
else:
    print(False)    

