class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def best(i):
            if i >= len(nums):
                return  0

            if i in memo:
                return memo[i]

            rob = nums[i] + best(i+2)
            skip = best(i+1)

            memo[i] = max(rob,skip)
            return memo[i]
        return best(0)
            