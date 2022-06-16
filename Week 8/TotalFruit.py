class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi, start = 0, 0
        fruitFreq = {}
        
        for win_end in range(len(fruits)):
            fruitLeft = fruits[win_end]
            if fruitLeft not in fruitFreq:
                fruitFreq[fruitLeft] = 0
            fruitFreq[fruitLeft] += 1
            
            while len(fruitFreq) > 2:
                fruitRight = fruits[start]
                fruitFreq[fruitRight] -= 1
                if fruitFreq[fruitRight] == 0:
                    del fruitFreq[fruitRight]
                start += 1
            
            maxi = max(maxi, win_end - start + 1)
        return maxi
