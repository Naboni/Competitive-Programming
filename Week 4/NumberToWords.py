class Solution:
    def numberToWords(self, num: int, idx=0) -> str:
        
        if not num: return "Zero"
        return self.getWords(num)
        
    def getWords(self, num):
        units = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen '
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety '
        bosses = ['Thousand', 'Million', 'Billion', 'Trillion']
        
        s = ''
        if not num: return s
        
        if num < 20:
            return (units.split(' ')[num - 1]).strip()
        
        if num <= 99:
            return (tens.split(' ')[num // 10 - 2] + ' ' + self.getWords(num%10)).strip()
        
        if num <= 999:
            return (units.split(' ')[num // 100 - 1] + ' Hundred ' + self.getWords(num%100)).strip()
        
        for i, p in enumerate(bosses):
            if 1000**(i+1) <= num < 1000**(i+2):
                return (self.getWords(num//1000**(i+1)) + ' ' + p + ' ' + self.getWords(num%1000**(i+1))).strip()
