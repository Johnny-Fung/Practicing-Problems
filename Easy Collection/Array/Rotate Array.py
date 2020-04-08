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