import numpy as np
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = b + 1
nums = np.arange(a,c)
print("Original array: ")
print()
print(nums)
d = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(d))
new_nums[::d+1] = nums
print("\nNew array: ")
print()
print(new_nums)

