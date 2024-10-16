//https://leetcode.com/problems/power-of-two/submissions/1424069110/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
