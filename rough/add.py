nums = [1,2,3,4,5]
target = 9
List = []
class solution:
    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if (i != j and nums[i] + nums[j] ==target ):
                    return[i,j]
        
