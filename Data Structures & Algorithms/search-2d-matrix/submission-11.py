class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        
        for i in range(N):
            L = 0
            R = len(matrix[i]) - 1
            
            while L <= R:
                M = (L + R) // 2
                if matrix[i][M] == target:
                    return True
                if matrix[i][M] < target:
                    L = M + 1
                if matrix[i][M] > target:
                    R = M - 1

        return False

    

            