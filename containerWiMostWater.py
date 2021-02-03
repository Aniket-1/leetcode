//Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two 
//endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxarea = 0
        while(l<=r):
            temparea = min(height[l], height[r])*(r-l)
            maxarea = max(temparea, maxarea)
            
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxarea
