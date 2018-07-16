class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haysize = len(haystack)
        needlesize = len(needle)

        if needlesize > haysize:
            return -1

        for i in range(haysize - needlesize + 1):
            if haystack[i:i+needlesize] == needle:
                return i
        return -1
