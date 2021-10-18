class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        min_val = float('inf');
        max_profit = 0;

        for i in range(len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
            else:
                max_profit = max(arr[i] - min_val, max_profit)

        return max_profit
