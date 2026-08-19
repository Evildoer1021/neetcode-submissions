class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = [0, 0]
        leftcorrect = False
        rightcorrect = False
        while left < right:
            if target - numbers[left] in numbers:
                leftcorrect = True
                print("Left is correct")
                answer[0] = left + 1
                if numbers[right] == target - numbers[left]:
                    answer[1] = right + 1
                else:
                    right -= 1
                    print("Right moved down")
            else:
                left += 1

                

            if target - numbers[right] in numbers:
                rightcorrect = True
                print("Right is correct")
                answer[1] = right + 1
                if numbers[left] == target - numbers[right]:
                    answer[0] = left + 1
                else:
                    left += 1
                    print("Left moved up")
            else:
                right -= 1
            
            if leftcorrect == True and rightcorrect == True:
                return answer
        
