class Solution:
    @staticmethod
    def get_bottleneck_character(char_map):
        min_single_char = min(char_map.get('b',0),char_map.get('a',0),char_map.get('n',0))
        min_double_char = min(char_map.get('l',0)//2,char_map.get('o',0)//2)
        return min(min_single_char,min_double_char)
    
    def maxNumberOfBalloons(self, text: str) -> int:
        char_map = {}
        for item in text:
            char_map[item] = char_map.get(item,0) + 1
        
        bottleneck = Solution().get_bottleneck_character(char_map)
        return bottleneck
        