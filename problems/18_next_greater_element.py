from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        key_mapping = {}
        for index,element in enumerate(nums2):
            key_mapping[element] = index
            
        result = []
        for element in nums1:
            element_index = key_mapping.get(element)
            for search_index in range(element_index,len(nums2)):
                if nums2[search_index] > element:
                    result.append(nums2[search_index])
                    break
                if search_index == len(nums2)-1:
                    result.append(-1)
        return result



import pytest

iterable = (
    ([1,2,3],[1,2,3,4],[2,3,4]),
    ([2,4],[1,2,3,4],[3,-1]),
)

@pytest.mark.parametrize("nums1,nums2,result",iterable)
def test_should_return_next_greater_element_from_nums2(nums1,nums2,result):
    assert Solution().nextGreaterElement(nums1,nums2) == result
            
        

"""
Runtime: 58 ms, faster than 87.29% of Python3 online submissions for Next Greater Element I.
Memory Usage: 14.1 MB, less than 96.07% of Python3 online submissions for Next Greater Element I.
"""