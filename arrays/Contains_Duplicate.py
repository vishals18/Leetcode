class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        sets=set()
        for num in nums:
            if num not in sets:
                sets.add(num)
            else:
                return True
        return False