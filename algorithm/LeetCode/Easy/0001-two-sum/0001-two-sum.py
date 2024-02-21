class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)-1):
            # there always is exactly one solution, but...
            # if only one elem left, the second for will cause an error
            
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
