class Solution():
    ascii_offset = 48

    def multiply(self, num1, num2):
        return str(self._atoi(num1) * self._atoi(num2))


    def _atoi(self, num):
        total, place = 0, 0

        for i in range(len(num) - 1, -1, -1): 
            total += (ord(num[i]) - self.ascii_offset) * 10 ** place
            place += 1

        return total

