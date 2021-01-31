# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        switch = 0
        counter = -1
        for num in nums:
            if switch == 1:
                counter += 1
                if num == 1:
                    if counter < k:
                        return False
                    counter = -1
            if num == 1:
                counter = -1
                switch = 1
        return True
