from cmath import inf


arr = [10,9,2,5,3,7,101,18]

def LIS(nums):

    def dp(index, prev):
        if index >= len(nums):
            return 0
        incl = 0
        if prev < nums[index]:
            incl += 1 + dp(index+1, nums[index])
        return max(dp(index+1, prev), incl)
    
    return dp(0, -inf)

print(LIS(arr))