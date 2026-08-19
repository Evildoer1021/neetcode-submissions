class Solution:
    def isValid(self, s: str) -> bool:
        
        if s[0] not in "({[":
            return False
        if s[-1] not in ")}]":
            return False
        for i in range(len(s)):
            
            if s[i] in "{([" and len(s) > 1:
                
                if s[i] == "{":
                    if (s[-(i+1)] == "}" and not i >= (0.5*len(s))):
                        continue
                    elif s[i+1] == "}":
                        continue
                    else:
                        return False
                if s[i] == "(":
                    if (s[-(i+1)] == ")" and not i >= (0.5*len(s))):
                        continue
                    elif s[i+1] == ")":
                        continue
                    else:
                        return False
                if s[i] == "[": 
                    if (s[-(i+1)] == "]"and not i >= (0.5*len(s))):
                        continue
                    elif s[i+1] == "]":
                        continue
                    else:
                        return False
            
            elif len(s) %2 !=0:
                
                return False
            
            else:
                continue
            
            
            
            
        return True
        