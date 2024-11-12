def maxProfit(prices):

#prices where price[i] is price on ith day
#if you choose on day from prices to buy and one to sell
#find the max profit

#min profit can be 0 (no  transactions)
#lowest profit must appear first

#define l r buy and sell pointers
#iterate through n incrementing l and r
	buy = 0
	sell = 1
	maxP = 0
	while sell < len(prices):
		if prices[buy] < prices[sell]:
			trade = prices[sell] - prices[buy]
			maxP = max(trade,maxP)
		else:
			buy = sell
		sell += 1
	return maxP