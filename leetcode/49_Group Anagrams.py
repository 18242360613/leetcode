class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ansd={}
        for str in strs:
            key = "".join(sorted(list(str)))
            if key in ansd:
                value = ansd[key]
                value.append(str)
            else:
                ansd[key] = [str]

        return ansd.values()