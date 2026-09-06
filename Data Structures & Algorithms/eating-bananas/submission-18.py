import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        k = (L + R) // 2
        
        while L <= R:
            totalhours = 0
            k = (L + R) // 2
            for pile in piles:
                
                totalhours += math.ceil(pile / k)
                
                
            if totalhours > h:
                L = k+ 1
                
                
            if totalhours <= h:
                R = k - 1
                
           
            
                    
            

            
            
        
        return L
    