class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = [0] * (n * 2)
        while(i < n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
            i += 1

        return ans