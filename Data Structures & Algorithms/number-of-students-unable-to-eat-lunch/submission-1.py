class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        r = n
        for s in sandwiches:
            c = 0
            while s != q[0] and c < n:
                q.append(q.popleft())
                c += 1
            
            if q[0] == s:
                q.popleft()
                r -= 1
            else:
                break
        
        return r
