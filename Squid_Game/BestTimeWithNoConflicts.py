class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = list(zip(ages,scores))
        age_score.sort()
        print(age_score)
        @lru_cache(None)
        def dp(i):
            res = 0
            for j in range(i+1, len(age_score)):
                if age_score[j][1] >= age_score[i][1] or age_score[j][0] == age_score[i][0]:
                    res = max(res, dp(j))
            return age_score[i][1] + res
        return max(dp(i) for i in range(len(ages)))