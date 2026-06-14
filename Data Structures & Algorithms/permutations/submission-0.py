class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for value in nums:
                if value in sol:
                    continue

                sol.append(value)
                backtrack()
                sol.pop()

        backtrack()
        return res

            
        

        
            
        
        

        


        