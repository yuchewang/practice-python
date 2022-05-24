
def binary_search(nums, target):
    '''
    left = 0
    right = len(nums) - 1
    searching interval: [left, right]
    so while condition is left <= right
    after checking mid the interval becomes [left, mid-1] or [mid+1, right]
    '''
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

def left_bound(nums, target):
    '''
    left = 0
    right = len(nums)
    searching area: [left, right)
    so while condition is left < right
    after checking mid the interval becomes [left, mid) or [mid+1, right)
    '''
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left if nums[left] == target else -1

def right_bound(nums, target):
    '''
    left = 0
    right = len(nums)
    searching area: [left, right)
    so while condition is left < right
    after checking mid the interval becomes [left, mid) or [mid+1, right)
    since the left boundary becomes mid + 1 when nums[mid] == target,
    we need to return right - 1 
    '''
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return right - 1 if nums[right - 1] == target else -1

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,8,9,10]
    target = 5
    print(binary_search(nums, target))
    nums = [0,1,3,3,3,4,5,6,7,8,9]
    target = 3
    print(left_bound(nums, target))
    nums = [0,1,3,3,3,4,5,6,7,8,9]
    target = 3
    print(right_bound(nums, target))