class Solution:
    def countSeniors(self, details: List[str]) -> int:
        arr= []
        for num in details:
            k = int(num[11]) * 10+ int(num[12])
            if k > 60:
                arr.append(k)
        return len(arr)

        


        