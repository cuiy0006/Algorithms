# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        a = 0
        b = n - 1
        while a < b:
            a_know_b = knows(a, b)
            b_know_a = knows(b, a)
            if (a_know_b and b_know_a) or (not a_know_b and not b_know_a):
                a += 1
                b -= 1
            elif a_know_b:
                a += 1
            else:
                b -= 1

        for i in range(n):
            if i != a and (knows(a, i) or not knows(i, a)):
                return -1
        return a
