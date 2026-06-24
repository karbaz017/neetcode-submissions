class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for ele in strs:
            key = "".join(sorted(ele))
            if key in anagram:
                anagram[key].append(ele)
            else:
                anagram[key] = [ele]

        # result = []
        # # for ele in strs:
        # #     result.append(ele)

        # return result

        return list(anagram.values())