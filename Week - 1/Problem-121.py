prices = [7,6,4,3,1]

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         if prices[i] - prices[j] != 0:
#             print(prices[i] - prices[j])
#         else:
#             print(0)    

def maxprofit(prices):
    min_no = prices[0]
    max_no = 0

    for i in prices:
        min_no = min(min_no, i)
        profit = i - min_no
        max_no = max(max_no, profit)

    return max_no

print(maxprofit(prices))        