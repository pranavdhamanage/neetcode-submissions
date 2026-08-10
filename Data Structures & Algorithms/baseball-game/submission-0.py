class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            if o == '+':
                num1_idx = len(record) - 1
                num2_idx = len(record) - 2 
                record.append(record[num1_idx] + record[num2_idx])
            elif o == 'C':
                record.pop()
            elif o == 'D':
                top = record[len(record) - 1]
                record.append(top * 2)
            else:
                record.append(int(o))

        ans = 0
        for el in record:
            ans += el

        return ans
