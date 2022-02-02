#O(nlogn)---> Time  O(n)---> Space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(len(nums)):
            new.append(nums[i]*nums[i])
            new.sort()
        return new
        #print(new)


##O(n)---> Time  O(n)---> Space

#--1

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[0]*len(nums)
        left=0
        right=len(nums)-1
        x=-1
        for i in range(len(nums)):
            if abs(nums[left])>abs(nums[right]):
                new[x]=nums[left]**2
                left+=1
            else:
                new[x]=nums[right]**2
                right-=1
            x=x-1
        return new


#--2

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[0]*len(nums)
        left=0
        right=len(nums)-1
        #x=-1
        for i in reversed(range(len(nums))):
            if abs(nums[left])>abs(nums[right]):
                new[i]=nums[left]**2
                left+=1
            else:
                new[i]=nums[right]**2
                right-=1
            #x=x-1
        return new
