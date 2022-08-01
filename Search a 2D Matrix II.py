#Approach 1
#TC O(n*m)
#SC O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    return True
        
        return False

#Approach 1
#TC O(n+m)
#SC O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        row = m-1
        col = 0
        
        while col < n and row >= 0:
            if matrix[row][col] > target:
                row = row - 1
            elif matrix[row][col] < target:
                col = col+1
            else:
                return True
        
        return False