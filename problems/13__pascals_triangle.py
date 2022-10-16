from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        first_item = [1]
        second_item = [1,1]
        temp_list = second_item
        result = []
        
        if numRows == 0:
            return result
        
        if numRows == 1:
            result.append(first_item)
            return result
        
        if numRows == 2:
            result.append(first_item)
            result.append(second_item)
            return result
        
        result.append(first_item)
        result.append(second_item)
        
        for count in range(numRows-2):
            list_to_be_appended = [1,]
            for i, item in enumerate(temp_list):
                len_temp_list = len(temp_list)
                if i+1< len_temp_list:
                    list_to_be_appended.append(temp_list[i]+temp_list[(i+1)])
                
            list_to_be_appended.append(1)
            temp_list = list_to_be_appended
            result.append(list_to_be_appended)
        
        return result


import pytest 


def test_for_zero_should_return_empty_list():
    assert Solution().generate(0) == []


def test_for_three_should_have_three_items():
    assert len(Solution().generate(3)) == 3


iterable = [
    (0,[]),
    (1,[[1]]),
    (5,[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
]


@pytest.mark.parametrize("num_rows, output", iterable)
def test_shoul_pass_for_input_integers(num_rows, output):
    assert Solution().generate(num_rows) == output
        

"""
Metadata:
Runtime: 53 ms, faster than 55.46% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 66.02% of Python3 online submissions for Pascal's Triangle.
"""