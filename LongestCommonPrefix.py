class Solution():
    maxint = 9223372036854775807

    def longestCommonPrefix(self, strs):
        prefix = ''
        if len(strs) == 0:
            return prefix
        short = self._shortestString(strs)
        for i in range(len(short)):
            for j in strs:
                if j[i] != short[i]:
                    return prefix
            prefix += short[i]

        return prefix


    def _shortestString(self, strs):
        minlen, index = self.maxint, -1
        for i in range(len(strs)):
            size = len(strs[i])
            if minlen > size:
                minlen = size
                index = i

        return strs[index]


