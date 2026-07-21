class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == val:
                nums[j] = '_'
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
                
        return i