import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        
        while L <= R:
            k = (L + R) // 2  # Calculate midpoint at the top of each loop
            
            totalhours = 0
            for pile in piles:
                totalhours += math.ceil(pile / k)
            
            if totalhours <= h:
                # k is fast enough, try to find a smaller valid speed
                R = k - 1
            else:
                # k is too slow, we must increase speed
                L = k + 1
        
        return L