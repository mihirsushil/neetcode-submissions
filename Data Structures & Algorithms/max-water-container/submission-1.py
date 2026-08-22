class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # we keep on moving down the lsit, move the shorter one and then hold the max and the in the end we do max(curr, and the one we held)


        l, r = 0, len(heights)-1

        max_area = 0  


        while l < r:
            height = min(heights[l] , heights[r])
            area = height * (r-l)
            max_area =max(max_area, area)
            if heights[l] > heights[r]:
                r-=1 
            elif heights[l] < heights[r]:
                l+=1 
            else:
                l+=1
                r-=1
        return max_area

      