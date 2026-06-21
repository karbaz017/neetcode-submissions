class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = {}
        for i in s:
            if i in char_count_s:
                char_count_s[i] += 1
            else:
                char_count_s[i] = 1

        char_count_t = {}
        for i in t:
            if i in char_count_t:
                char_count_t[i] += 1
            else:
                char_count_t[i] = 1

        if len(char_count_s) == len(char_count_t):
            for i in char_count_s:
                if i in char_count_t and char_count_s[i] == char_count_t[i]:
                    continue
                else:
                    return False
        else:
            return False
        
        return True
