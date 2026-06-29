class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        dp = {}
        def f(i, j):
            if (i, j) in dp: return dp[(i, j)]
            if i == len(s1) and j == len(s2): return True
            dp[(i, j)] = (i < len(s1) and s1[i] == s3[i+j] and f(i+1, j)) or \
                         (j < len(s2) and s2[j] == s3[i+j] and f(i, j+1))
            return dp[(i, j)]
        return f(0, 0)