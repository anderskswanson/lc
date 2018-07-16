numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return numerals[s]
        elif numerals[s[0]] < numerals[s[1]]:
            return self.romanToInt(s[1:]) - numerals[s[0]]
        return numerals[s[0]] + self.romanToInt(s[1:])
