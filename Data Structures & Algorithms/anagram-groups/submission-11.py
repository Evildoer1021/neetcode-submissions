class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        visited = set()
        for i in range(len(strs)):
            first = strs[i]
            if first in visited:
                continue
            else:
                
                chart = []
                chart.append(first)
                visited.add(first)
                
                
            
            for j in range(i+1, len(strs)):
                second = strs[j]
                if j in visited:
                    continue
                
            
                if (len(first) == len(second)):
                    F, S = {}, {}
                
                    for k in range(len(first)):
                        F[first[k]] = 1 + F.get(first[k], 0)
                        S[second[k]] = 1 + S.get(second[k], 0)
                    if F==S:
                        chart.append(second)
                        visited.add(second)
                            
                else:
                    continue

          
                
                            
            final.append(chart)     
        return final    


