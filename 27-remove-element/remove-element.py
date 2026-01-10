class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums)
        count = 0
        for index, element in enumerate(nums):

            if element == val:
                nums[index] = float('inf')
                count = count+1

        nums.sort()
        print(nums)
        
        return len(nums) - count

    

        