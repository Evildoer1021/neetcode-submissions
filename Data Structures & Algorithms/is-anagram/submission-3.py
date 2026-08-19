class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = []
        second = []

        for i in range(len(s)):
            first += s[i]
        for i in range(len(t)):
            second += t[i]

        first.sort()
        second.sort()

        if (len(first) != len(second)):
            return False

        count = 0
        for i in range(len(first)):
            if (first[i] == second[i]):
                count += 1

        if (count == len(first)):
            return True
        else:
            return False

        
        