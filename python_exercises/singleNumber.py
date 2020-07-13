def singleNumber(nums):
    return 2*sum(set(nums))- sum(nums)

print(singleNumber([1,1,2,2,3,4,4]))
    