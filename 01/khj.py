#1979
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = max(nums)
        y = min(nums)
        
        while y:
            x, y = y, x % y
            
        print(x)
        return x


#1980

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        length = len(nums[0])        
        # length = 4

        
        # print((2**length)-1)
        check_count = (2**length)
        check_list = []
        
        big_val = bin((2**length) - 1)[2:]
        
        
        print(big_val)
        
        for x in range(check_count):
            now = bin(x)[2:]
            if(len(now) < length):
                now.zfill(length)
                # print(now.zfill(length))
                check_list.append(now.zfill(length))
            else: 
                # print(now)
                check_list.append(now)
        
        # print(check_list)
        #ok
        
        for x in range(len(check_list)):
            if check_list[x] not in nums:
                return check_list[x]

#1981
class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        print(target)
    
        val_count = len(mat)
#         print(val_count)
        
#         for x in range(val_count):
#             print(x)
            
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums}
        
        return min(abs(target - x) for x in nums)
        
#1982