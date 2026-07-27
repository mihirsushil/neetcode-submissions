class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for z in range(i+1,len(numbers)):
                if numbers[i] != numbers[z]:
                    if numbers[i] + numbers[z] == target:
                        return [i+1, z+1] 
