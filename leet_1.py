class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic= {}
        for i in nums:
            ys = target -i
            if ys in dic:
                print(dic)
                return [nums.index(i),dic[ys]]
            else:            
                dic[i] = nums.index(i)
        print(dic)
    
    
