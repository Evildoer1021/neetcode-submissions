class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        thing = {}
        for num in nums:
            
            if num not in thing:
                thing[num] = 1
            else:
                thing[num] += 1
        top_keys = heapq.nlargest(k, thing, key=thing.get)
        return top_keys
            
        