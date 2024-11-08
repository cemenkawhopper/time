import random, time

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

nums = []
for i in range(random.randint(5, 100)):
    nums.append(random.randint(5, 100))
print(nums)
start = time.perf_counter()
end = time.perf_counter()
print(end-start)
