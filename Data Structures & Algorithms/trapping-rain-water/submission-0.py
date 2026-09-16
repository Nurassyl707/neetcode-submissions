class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        result=0
        l_height,r_height=height[l],height[r]
        while l<r:
            if l_height<r_height:
                l+=1
                l_height=max(l_height,height[l])
                result += l_height-height[l]
            else:
                r-=1
                r_height=max(r_height,height[r])
                result += r_height-height[r]
        return result
