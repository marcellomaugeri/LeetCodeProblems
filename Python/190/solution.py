class Solution:
    def reverseBits(self, n: int) -> int:
        nBits = bin(n)[2:].zfill(32)[::-1]
        return int(nBits, 2)