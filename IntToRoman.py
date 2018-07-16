class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

            # Roman numeral characters:
        # M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1
        numeral = ""

        while num > 0:
            if num >= 1000:
                num -= 1000
                numeral += "M"
            elif num >= 900:
                num -= 900
                numeral += "CM"
            elif num >= 500:
                num -= 500
                numeral += "D"
            elif num >= 400:
                num -= 400
                numeral += "CD"
            elif num >= 100:
                num -= 100
                numeral += "C"
            elif num >= 90:
                num -= 90
                numeral += "XC"
            elif num >= 50:
                num -= 50
                numeral += "L"
            elif num >= 40:
                num -= 40
                numeral += "XL"
            elif num >= 10:
                num -= 10
                numeral += "X"
            elif num == 9:
                num -= 9
                numeral += "IX"
            elif num >= 5 and num <= 8:
                num -= 5
                numeral += "V"
            elif num == 4:
                num -= 4
                numeral += "IV"
            else:
                num -= 1
                numeral += "I"
        return numeral
