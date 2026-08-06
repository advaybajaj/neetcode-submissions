class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        max_length = 0
        used = set()
        curr_length = 0

        while right < len(s): 
            
            while s[right] in used:
                used.remove(s[left])
                curr_length -= 1
                left += 1

            used.add(s[right])
            curr_length += 1 
            max_length = max(max_length, curr_length) 
            right += 1

        return max_length
        