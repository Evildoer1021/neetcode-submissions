class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right  = len(s) -1
        if len(s) == 1:
            return True
        
        while left <= right:
            print(left," ", right," ",s[left], " ", s[right])
            while not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                print("he")
                if right == 0:
                        return True
                
            while not s[left].isalpha() and not s[left].isdigit():
                left += 1
                print("haw")
                if left == 0:
                    return True
                
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                print("ha")
            else:
                
                return False
                

        return True