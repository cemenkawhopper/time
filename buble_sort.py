import random, time
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

nums = []
for i in range(random.randint(5, 100)):
    nums.append(random.randint(5, 100))
    bubble_sort(nums)
print(nums)
start = time.perf_counter()
end = time.perf_counter()
print(end-start)