class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_list[sorted_word].append(word)
        return anagram_list.values()
        