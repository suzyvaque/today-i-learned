class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        length = len(str(x))
        for pos in range(0, length//2 + 1):
            if (x//(10**(length-pos-1)))%10 == (x%(10**(pos+1)))//(10**pos):
                continue
            else:
                return False
        return True
