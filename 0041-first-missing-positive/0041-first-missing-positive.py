class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n > 0]  
        for n in nums:
            idx = abs(n) - 1 
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] = nums[idx] * -1  
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1  
        return len(nums) + 1  
