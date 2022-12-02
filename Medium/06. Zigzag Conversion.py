class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        # calculate period
        p = 2 * (numRows - 1)
        result = [""] * numRows
        for i in xrange(len(s)):
            floor = i % p
            if floor >= p//2:
                floor = p - floor
            result[floor] += s[i]
        return "".join(result)


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
