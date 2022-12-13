class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankgenes = set(bank)
        queue = deque([startGene])
        visited = set([startGene])
        count = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene: return count
                for i in range(9):
                    for char in "ACGT":
                        newGene = gene[:i] + char + gene[i+1:]
                        if newGene in bankgenes and newGene not in visited:
                            queue.append(newGene)
                            visited.add(newGene)
            count += 1
        return -1