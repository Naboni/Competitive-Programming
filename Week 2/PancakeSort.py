class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        for i in range(len(arr), 1, -1):
            j = arr.index(max(arr[:i]))
            output.extend([j + 1, i])
            ## flip array using this -> array[::-1]  
            ## brings the maximum element to the front
            arr[:j + 1] = arr[:j + 1][::-1]
            ## takes the maximum element to the back
            arr[:i] = arr[:i][::-1]
        return output
