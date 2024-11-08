import random, time
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

nums = []
for i in range(random.randint(5, 100)):
    nums.append(random.randint(5, 100))
print(nums)
start = time.perf_counter()
end = time.perf_counter()
print(end-start)