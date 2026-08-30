class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights)-1 # pointers 

        max_area = 0 # set max value 

        while l <r:
            height = min(heights[l], heights[r]) # take only the min height of the two pointers
            area = height * (r-l) # area calc
            max_area = max(max_area, area) # take bigger area 
            # loop through get the bigger bar 
            if heights[l] < heights[r]: 
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else: # if same move both 
                l+=1
                r-=1
           
        return max_area


        

      