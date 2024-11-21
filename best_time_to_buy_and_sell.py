#! /usr/bin/env python3

def soln(prices):
    l = 0
    r = 1
    profit = [0]
    while l<r and r<len(prices):
        if prices[l]>prices[r]:
            l = r
        else:
            profit.append(prices[r]-prices[l])
        r+=1
    return max(profit)

#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = [2,1,4]
print(soln(prices))
