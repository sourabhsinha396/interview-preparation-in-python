from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer
        i = len(nums)-1
        count_non_val = 0
        for j in range(len(nums)-1,-1,-1):
            print(i,j)
            if nums[j] == val:
                #need for swap
                nums[i],nums[j] = nums[j],nums[i]
                i -= 1
            else:
                count_non_val += 1
            print(i,j,nums)
        return count_non_val


import pytest


iterable = [
([3,3,3,3],3,0),
([2,3,3,2],3,2),
([3,2,2,3],3,2)
]

@pytest.mark.parametrize("input,val,result",iterable)
def test_should_return_count_of_non_val(input,val,result):
    assert Solution().removeElement(input,val) == result


"""
Problem Link: https://leetcode.com/problems/remove-element/

Runtime: 51 ms, faster than 70.79% of Python3 online submissions for Remove Element.
Memory Usage: 13.9 MB, less than 14.37% of Python3 online submissions for Remove Element.
"""