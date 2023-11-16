#BruteForce Approach

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0 ;
        for l in range(len(height)):
          for r in range(l+1, len(height)):
            area = (r-l) * min(height[l] , height[r]) 
            res = max(area, res)
  
        return res 
          


        
