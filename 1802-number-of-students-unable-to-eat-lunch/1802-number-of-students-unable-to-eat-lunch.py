'''
return the number of student unable to eat 

compare the prefer swich of student and the having sandwcih type 
the remain student after subtract the sandwich type count 

if the prefer SW of student > 0 (still want), 

still have need of SW type, have the match SW type, student # -=1 bc they have want they want 

still have need but not SW -> the remain student 
'''
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not students or not sandwiches:
            return -1
        cnt = Counter(students)
        res = len(students)

        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1 
                res -= 1
            else: #no remain need for that type of SW - deadlock
                break 
        return res

        
        
