class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        def play(arr,n,l):
            if len(arr) == 1:  return arr[0]
            turn = (l % n) - 1
            arr.pop(turn)
            l = turn + k if turn != -1 else k
            n -= 1
            return play(arr,n,l)
        return play(players,n,k)
