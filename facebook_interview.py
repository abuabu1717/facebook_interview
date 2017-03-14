'''
 
@author vaibhavaggarwal

Given an array of stock prices. Write a function to return maximum profit 
in a one-time only buy-sell transaction. If no profit is made, then return 0.
Example - 25,40,10,20,25,4,30,2 This array should return 26 which is difference 
between 4 and 30, meaning stock is bought at 4 and sold at 30.

'''

def maxProfit(arr):
	if len(arr)==0:
		return 0
	max_profit = 0
	minimum_stock = arr[0]
	for i in xrange(1,len(arr)):
		minimum_stock = min(minimum_stock,arr[i])
		max_profit = max(max_profit, arr[i]-minimum_stock)
	return max_profit

arr = [25,40,10,20,25,4,30,2]
print (maxProfit(arr))