def product_except_self(nums):
  result = [1] * len(nums)

  prefix = 1
  for i in range(len(nums)):
    result[i] = prefix
    prefix = prefix * nums[i]

    

  

