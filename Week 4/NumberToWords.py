class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        words = {
            1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9: "Nine",
            10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",
            100:"Hundred", 1000:"Thousand", 1000000:"Million", 1000000000:"Billion"
        }
        output = ""
        result = self.change(num, words, output)
        return " ".join(result.split())
    
    def change(self, num, words, output):
        if num == 0:
            return output
        elif num < 20:
            output += words[num]
            return output
        elif 20 <= num < 100:
            output += words[(num//10)*10] + " " + self.change(num%10, words, output)
            return output
        elif 100 <= num < 1000:
            output += words[num//100] + " " + words[100] + " " + self.change(num%100, words, output)
            return output
        elif 1000 <= num < 1000000:
            output += self.change(num//1000, words, output) + " " + words[1000] + " " + self.change(num%1000, words, output)
            return output
        elif 1000000 <= num < 1000000000:
            output += self.change(num//1000000, words, output) + " " + words[1000000] + " " + self.change(num%1000000, words, output)
            return output
        else:
            output += self.change(num//1000000000, words, output) + " " + words[1000000000] + " " + self.change(num%1000000000, words, output)
            return output
