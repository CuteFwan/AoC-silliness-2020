with open('input9.txt') as f:
    numbers = [int(n) for n in f.read().split()]

def find_numbers(nums, target):
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i != j:
        cur = nums[i] + nums[j]
        if cur == target:
            return nums[i], nums[j]
        elif cur < target:
            i += 1
        elif cur > target:
            j -= 1
    return False

def find_broken_numbers(numbers, offset):
    for i in range(offset, len(numbers)):
        result = find_numbers(numbers[i-offset:i], numbers[i])
        if not result:
            return numbers[i]

result = find_broken_numbers(numbers,25)
print(result)

def find_contiguous_set(numbers, target):
    for trying in range(2, len(numbers)-1):
        i = 0
        j = i + trying
        while j <= len(numbers):
            if sum(numbers[i:j]) == target:
                return min(numbers[i:j]) + max(numbers[i:j])
            else:
                i += 1
                j += 1

result2 = find_contiguous_set(numbers, result)
print(result2)