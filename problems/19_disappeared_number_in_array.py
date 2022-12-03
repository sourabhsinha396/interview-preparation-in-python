from typing import List 


# Time O(n) Space O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Using the relation of index and the number present
        
        for element in nums:
            # print(element)
            nums[abs(element)-1] = -abs(nums[abs(element)-1]) if nums[abs(element)-1] > 0 else nums[abs(element)-1]
            # print(nums)
        
        result = []
        for index in range(len(nums)):
            if nums[index] > 0:
                result.append(index+1)
        return result

"""
Runtime: 577 ms, faster than 68.98% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.9 MB, less than 87.51% of Python3 online submissions for Find All Numbers Disappeared in an Array."""

import pytest 

iterable = (
    ([1,2,3,4,4],[5]),
    ([2,2],[1])
)


@pytest.mark.parametrize("input,result",iterable)
def test_should_identify_missing_elements_from_list(input:List,result:List):
    assert Solution().findDisappearedNumbers(input) == result


# Time O(n) Space O(n)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         element_map = {}
#         result = []
#         for i in range(1,len(nums)+1):
#             element_map[i] = 1
            
#         for element in nums:
#             if element_map.get(element):
#                 element_map.pop(element)
        
#         result = [remaining for remaining in element_map.keys()]
#         return result


"""
Runtime: 386 ms, faster than 86.92% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 26.2 MB, less than 14.19% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""



"""
Work in progress
import time
import multiprocessing
from multiprocessing import Manager


class Solution:
    @staticmethod
    def append_if_not_present(shared_memory,num,nums):
        print("here")
        if num not in nums:
            print(f"appending {num}")
            shared_memory.append(num)
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Using multiprocessing
        # shared_memory = multiprocessing.Array('i', range(len(nums)))
        processes = []
        with Manager() as manager:
            shared_memory = manager.list(range(50))
            for num in range(1,len(nums)+1):
                p = multiprocessing.Process(target=Solution().append_if_not_present,args=(shared_memory, num,nums))
                p.start()
                processes.append(p)
                
            for process in processes:
                print("process",process)
                process.join()

            # time.sleep(1)
            result = list(shared_memory)
            print("s",result)
            # for item in shared_memory:
            #     result.append(item)
            # return result

"""