class Solution():
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        numRows = min(len(s), numRows)
        rows = [[] for i in range(numRows)]
        cur_row, direction = 0, 1

        for i in s:
            rows[cur_row].append(i)
            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1
            cur_row += direction

        return ''.join(''.join(rows[i])
                    for i in range(numRows))

