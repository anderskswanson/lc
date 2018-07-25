class Solution():


    def generateParenthesis(self, n):
        result = []
        def parens(l, r, seq, res):
            if r < l or l == -1 or r == -1:
                return
            if l == 0 and r == 0:
                res.append(seq)
            else:
                parens(l-1, r, seq+'(', res)
                parens(l, r-1, seq+')', res)
        parens(n, n, '', result)
        return result



