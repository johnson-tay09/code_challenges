# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

# The function should return the number of arithmetic slices in the array A.
class Solution:
    def numberOfArithmeticSlices(self, A):
        count = 0
        ans = 0
        diff = None
        # [1,2,3,4,8,9,10]
        # loop i from 1 to end
        for i in range(1, len(A)):
            # set the newDiff value
            newDiff = A[i] - A[i-1]  # --second pass evals to 1
            # compare newDiff to diff
            if newDiff == diff:
                ans += count
                # increase the counters value by 1
                count += 1
            # set diff = newDiff
            else:
                diff = newDiff
                # increase counter variable which is not our return value
                count = 1
        return ans
