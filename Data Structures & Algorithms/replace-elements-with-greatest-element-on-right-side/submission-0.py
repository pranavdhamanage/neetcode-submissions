class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        n = len(arr)
        
        while i < n:
            if i == n - 1:
                arr[i] = -1
            else:
                max_num = float('-inf')
                for k in range(i + 1, len(arr)):
                    if max_num <= arr[k]:
                        max_num = arr[k]
                
                arr[i] = max_num
            
            i += 1
        
        return arr