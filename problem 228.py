'''
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

nums = [1]
output = []
x = 0

for i in range(len(nums) - 1):  # for i in range(1) now i is 5
    if nums[i] + 1 == nums[i + 1]:
        if i == len(nums) - 2:
            output.append(str(nums[i - x]) + '->' + str(nums[i + 1]))
        x += 1
    else:
        if x == 0:
            output.append(str(nums[i]))
        else:
            output.append(str(nums[i - x]) + '->' + str(nums[i]))
        x = 0
        if i == len(nums) - 2:
            output.append(str(nums[-1]))

if len(nums) == 1:
    output.append(str(nums[0]))

print(output)

