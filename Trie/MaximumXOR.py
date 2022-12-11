class Trie():
    def __init__(self,x):
        self.child = {}
        # height of Trie initialized with largest 
        # number's binary length
        # self.b to keep track of root level's binary
        # value, so we don't have to calculate 2**x every
        # time
        self.b = 2**x
        
    # default insertion method for trie,
    # note to convert str and int accordingly
    def insert(self,x):
        cur = self
        for c in x:
            cc = int(c)
            if cc not in cur.child:
                cur.child[cc] = Trie(0)
            cur = cur.child[cc]
        
    def xor(self,x,res):
        cur,ans,b0 = self,0,self.b
        # b0 keep tracks of current binary digit's value
        for c in x:
            # we always takes the binary path that's different
            # than x's current binary digit, to achieve max XOR
            # 1-0 = 1; 1-1 = 0 complement
            cc = 1-int(c)
            b0 /= 2
            # if we found complement, go down that path to add
            # possibly more to XOR's value
            if cc in cur.child:
                cur = cur.child[cc]
                ans += b0
                # simple optimization, notice that in binary rep.
                # 16,8,4,2,1; 8+4+2+1<16, 4+2+1<8 ... so if anytime
                # ans is not at least half of current found result,
                # this path has already lost
                if 2*ans < res: return 0
            # if we cannot find complement, go down available
            # path and don't accumulate anything to XOR
            else:
                cur = cur.child[1-cc]
        return ans

    
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) to find max
        m = max(nums)
        # O(n) to create set
        nums = list(set(nums) - {m})
        
        if not nums: return 0
        
        # convert max to binary, remove '0b' prefix
        m = str(bin(m)[2:]); m_len = len(m)
        
        # insert max number first, initialize Trie
        # with the maximum length of binary, this 
        # becomes height of Trie
        t = Trie(m_len); t.insert(m)
        
        res,bi_nums = 0,[]
        
        # O(n) time to create list of binary nums
        for i in nums:
            bi_nums.append(str(bin(i)[2:]).zfill(m_len))
            
        # O(n) time to insert all binary nums into Trie
        for i in bi_nums:
            t.insert(i)
        
        # O(n) to find xor, each search runs down Trie once
        for i in bi_nums:
            res = max(t.xor(i,res),res)
        return int(res)
        
        