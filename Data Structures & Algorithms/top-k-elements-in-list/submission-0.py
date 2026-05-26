class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for number in nums:
            if number in hashmap:
                hashmap[number] += 1
            else:
                hashmap[number] = 1

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result

        
      
        