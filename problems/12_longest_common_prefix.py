from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        
        try:
            first_str = strs[0]
        except IndexError:
            return ""
        
        last_common_index = -1
        for index,character in enumerate(first_str):
            index_matched = 0 #number of items/words for which character is matched
            for item in strs:
                try:
                    if item[index] == character:
                        index_matched+=1
                except IndexError:
                    return first_str[:last_common_index+1]
                
                #print(index,character,item,index_matched)
            if index_matched == len(strs):
                last_common_index=index
                #print("lci",last_common_index)
                continue
            else:
                return first_str[:last_common_index+1]
            
        return first_str[:last_common_index+1]



import pytest

def test_should_return_long_prefix():
    input_list = ["flower","flow","floght"]
    result = "flo"
    assert Solution().longestCommonPrefix(input_list) == result


def test_should_fail_when_wrong_prefix_provided():
    input_list = ["flower","flow","floght"]
    result = "fl"
    with pytest.raises(AssertionError) as e:
        assert Solution().longestCommonPrefix(input_list) == result