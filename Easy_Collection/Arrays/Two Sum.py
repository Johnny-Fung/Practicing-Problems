class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index, i in enumerate(nums):
            remainder = target - i
            if remainder in seen:
                return [seen[remainder],index]
            seen[i]=index
