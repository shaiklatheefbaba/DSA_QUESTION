class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(start, remaining, path):
            if remaining == 0:
                ans.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                dfs(i, remaining - candidates[i], path)

                path.pop()

        dfs(0, target, [])

        return ans