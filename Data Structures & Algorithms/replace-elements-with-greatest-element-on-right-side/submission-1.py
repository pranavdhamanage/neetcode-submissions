class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        i = n - 1
        right_max = -1
        while i >= 0:
            ans[i] = right_max
            right_max = max(arr[i], right_max)
            i -= 1

        return ans