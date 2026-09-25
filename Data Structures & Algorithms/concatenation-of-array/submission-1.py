class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dup = []
        for num in nums:
            dup.append(num)
        return nums+dup
        