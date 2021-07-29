# leetcode solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y]) == target:
                    return [x, y]

# vscode soulution
num =  [2, 7, 11, 15]
target = 9

def addsum():
    for x in range(len(num)):
        # print("x:",x)
        for y in range(x+1, len(num)):
            # print("y:",y)
            if (num[x] + num[y]) == target:
                return [x, y]
            
print(addsum())
