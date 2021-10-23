1295. Find Numbers with Even Number of Digits
--------------------------------------------

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
                
                --------------------------------------
              
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num) )% 2 == 0])
