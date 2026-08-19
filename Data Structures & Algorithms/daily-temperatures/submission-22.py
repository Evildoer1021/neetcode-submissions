
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        number = len(temperatures)

        result = [0] * number
        stack = []
        for i in range(number):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)
        return result