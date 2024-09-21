class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # create a list of [val, freq] list
        # sort with lambda

        dict_count = {}

        for num in nums:
            if dict_count.get(num, None) == None:
                dict_count[num] = 1
            else:
                dict_count[num] += 1
        
        nums.sort(key = lambda num: (dict_count[num], -num))

        return nums
