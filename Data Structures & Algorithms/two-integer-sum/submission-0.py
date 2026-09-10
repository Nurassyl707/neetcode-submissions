class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    new_list.append(i)
                    new_list.append(j)
        return new_list