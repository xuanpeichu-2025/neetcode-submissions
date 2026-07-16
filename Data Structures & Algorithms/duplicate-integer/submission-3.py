class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for i in range(len(nums)):
            if nums[i] in memory:
                return True
            else:
                memory.add(nums[i])

        return False

