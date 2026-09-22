class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col=len(matrix[0])
        low=0
        high=row*col-1
        while low<=high:
            mid=low+(high-low)//2
            row_1=mid//col
            col_1=mid%col
            if target>matrix[row_1][col_1]:
                low=mid+1
            elif target<matrix[row_1][col_1]:
                high=mid-1
            else:
                return True
        return False
                