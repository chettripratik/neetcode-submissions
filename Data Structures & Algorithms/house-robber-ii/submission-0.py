class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses: List[int]) -> int:
            memo = {}
            
            
            def best(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                
                rob_house = houses[i] + best(i + 2)
                skip_house = best(i + 1)
                
                memo[i] = max(rob_house, skip_house)
                return memo[i]
            
            return best(0)
        
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

            

        