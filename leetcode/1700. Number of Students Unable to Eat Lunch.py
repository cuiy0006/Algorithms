class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students)
        zeros = len(students)-ones

        for i in range(len(sandwiches)):
            if sandwiches[i] == 0:
                if zeros == 0:
                    return ones
                zeros -= 1
            else:
                if ones == 0:
                    return zeros
                ones -= 1
        return 0
