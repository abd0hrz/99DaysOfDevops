class Solution(object):
] % 3) << i)
    #     return res.value

    def singleNumber(self, nums):
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
