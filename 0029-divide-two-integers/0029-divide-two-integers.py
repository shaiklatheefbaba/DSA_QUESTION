class Solution:
    def divide(self, dividend, divisor):
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a, b = abs(dividend), abs(divisor)
        res = 0

        while a >= b:
            temp, multiple = b, 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            res += multiple

        return sign * res