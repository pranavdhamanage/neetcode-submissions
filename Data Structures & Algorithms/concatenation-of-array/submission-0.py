class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0 
        ans = []
        n = len(nums)
        count = 2
        while (count > 0):
            i = 0
            while(i < n):
                ans.append(nums[i])
                i += 1
            count -= 1
        
        return ans