from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_seen = 0
        semaphore = 0
        
        for element in nums:
            if semaphore == 0:
                max_seen = element
                semaphore = 1
            elif element == max_seen:
                semaphore += 1
            elif element != max_seen:
                semaphore -= 1
        return max_seen


import pytest 

iterable = (
    ([0,0,0,0,1,1],0),
    ([4,3,4,3,4,3,4],4)
)


@pytest.mark.parametrize("input,result",iterable)
def test_should_find_majority_element(input,result):
    """Majority element means the one that occurs atleat [n/2] times"""
    assert Solution().majorityElement(input) == result