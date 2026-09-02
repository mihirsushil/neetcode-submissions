class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = [row[0]for row in matrix]

        l,r = 0, len(arr)-1

        while l<=r:
            m =(l+r)//2
            if target <arr[m]:
                r= m-1
            elif target > arr[m]:
                l=m+1
            else:
                return True
        if r <0: 
            return False
        
        row = matrix[r]
        l, r2 = 0, len(row) - 1
        while l <= r2:
            m = (l + r2) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r2 = m - 1
            else:
                return True

        return False
                


           

        