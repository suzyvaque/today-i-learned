class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Sort first. <- Can optimize this part with merge sort O(nlogn)
        # For a number x in index n, search for number y in index n+1, ... max. If found y, iterate until next num!=y then stop search.
        
        nums.sort(reverse = True)
        count = 0
        
        for i in range(0, len(nums) - 1):
            num_curr = nums[i]
            
            num_found = None
            
            for j in range(i+1, len(nums)):
                num_compare = nums[j]
                
                if num_found == None:
                    if num_curr - num_compare == k:
                        num_found = num_compare
                        count += 1
                elif num_found == num_compare:
                    count += 1
                else:
                    # stop search and move on to next index for curr
                    break
                    
        return count
