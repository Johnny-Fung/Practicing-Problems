#Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i+=1
        return len(nums)

#Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowest = float("inf")
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit

#Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        while k>0:
            nums.insert(0,nums[-1])
            del nums[-1]
            k-=1
        return nums

#Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

#Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

#Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in nums1:
            if i in nums2:
                out.append(i)
                nums2.remove(i)
        return out

#Plus One
print ("test")