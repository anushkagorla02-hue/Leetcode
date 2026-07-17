class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        string=""
        i=0
        while i<len(strs[0]):
            if strs[0][i]==strs[len(strs)-1][i]:
                string+=strs[0][i]
            else:
                break
            i=i+1
        return string
        