# def sumNum(num):
# num = 38   
# count = 0
# for i in str(num):
#     count += int(i)

# sum = 0
# for i in str(count):
#     sum += int(i)

# print(sum)    


# sumNum(38)

def sum(num):
    count = 0 
    for i in str(num):
        count += int(i)

    if len(str(count)) == 1:
        return int(count)
    else:
        return sum(count)       
print(sum(98765))   