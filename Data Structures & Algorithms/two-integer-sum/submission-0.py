class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums =[(num,i) for i, num in enumerate(nums)]
        indexed_nums.sort()
        left =0
        right = len(nums)-1
        while left < right:
            current_sum= indexed_nums[left][0]+indexed_nums[right][0]
            if current_sum == target:
                idx1 = indexed_nums[left][1]
                idx2 = indexed_nums[right][1]
                return [min(idx1,idx2),max(idx1,idx2)]
            elif current_sum > target:
                right -=1
            else:
                left+=1
                
        
        return []
